from django.db import models
from django.contrib import admin
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Poll(models.Model):
    question = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.slug

class Choice(models.Model):
    answer = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer

# class ChoiceInLine(admin.TabularInline):
#     model = Choice
#
# class PollAdmin(admin.ModelAdmin):
#     inlines = [
#         ChoiceInLine
#     ]

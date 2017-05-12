from django.contrib import admin
from polls.models import Poll, Choice, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug')

@admin.register(Poll)
class BlogAdmin(admin.ModelAdmin):
  list_display = ('question', 'slug')

@admin.register(Choice)
class PostAdmin(admin.ModelAdmin):
  list_display = ('answer', 'votes', 'poll')

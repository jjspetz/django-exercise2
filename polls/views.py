from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from polls.models import Poll, Choice, Category

def polls(request):
    polls = Poll.objects.all()
    
    context = {
        'polls' : polls
    }
    return TemplateResponse(request, 'poll.html', context)

def polls_by_category(request):
    categories = Category.objects.all()

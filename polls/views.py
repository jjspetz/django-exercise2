from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from polls.models import Poll, Choice, Category

def polls(request):
    polls = Poll.objects.all()

    category = request.GET.get('category', '')
    if category:
        polls = polls.filter(categories__slug=category)

    context = {
        'polls' : polls,
        'categories' : Category.objects.all(),
    }
    return TemplateResponse(request, 'poll.html', context)

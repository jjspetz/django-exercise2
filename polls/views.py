from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from polls.models import Poll, Choice, Category, PizzaAnswerForm

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

def pizza(request):
    form = PizzaAnswerForm(request.POST or None)
    poll = get_object_or_404(Poll, slug='pizza-topping-poll')
    answers = Choice.objects.filter(poll=poll)

    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data['answer'].lower()

            for answer in answers:
                if answer.answer == data:
                    answer.votes += 1
                    answer.save()
                    context = {
                        'results': answers,
                        'poll' : poll,
                    }
                    return TemplateResponse(request, 'results.html', context)

            Choice.objects.create(answer=data, votes=1, poll=poll)
            context = {
                'results': Choice.objects.filter(poll=poll),
                'poll' : poll,
            }
            return TemplateResponse(request, 'results.html', context)

    content = {
        'form' : form,
        'poll' : poll,
    }
    return TemplateResponse(request, 'pizzapoll.html', content)

def answerpoll(request, poll_slug):
    poll = get_object_or_404(Poll, slug=poll_slug)
    answers = Choice.objects.filter(poll=poll)

    if request.method == 'POST':
        for answer in answers:
            if answer.answer == request.POST.get('ans', ''):
                answer.votes += 1
                answer.save()
                context = {
                    'results': answers,
                    'poll' : poll,
                }
                return TemplateResponse(request, 'results.html', context)


    content = {
        'poll' : poll,
        'answers' : answers,
    }
    return TemplateResponse(request, 'answerpoll.html', content)

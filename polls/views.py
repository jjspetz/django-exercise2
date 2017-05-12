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
    poll = Poll.objects.filter(slug='pizza-topping-poll')
    answers = Choice.objects.filter(poll=poll)

    if request.method == 'POST':
        if form.is_valid():
            for answer in answers:
                if answer.answer == form.cleaned_data['answer']:
                    answer.votes += 1
                    answer.save()
                    context = {
                        'results': answers,
                    }
                    return TemplateResponse(request, 'results.html', context)

            Choice.objects.create(answer=form.cleaned_data['answer'], votes=1, poll=poll.get())
            context = {
                'results': Choice.objects.filter(poll=poll),
            }
            return TemplateResponse(request, 'results.html', context)

    content = {
        'form' : form
    }
    return TemplateResponse(request, 'testform.html', content)

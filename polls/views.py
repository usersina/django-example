from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question


# Fetch all questions and display them
def index(request):
    return render(request, 'polls/index.html', {
        'questions': Question.objects.order_by('-pub_date')[:5]
    })


# Fetch a question and display it
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    return render(request, 'polls/detail.html', {
        'question': question
    })


# Fetch a question and display the results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html', {
        'question': question
    })

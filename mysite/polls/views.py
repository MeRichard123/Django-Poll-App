from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question

# Create your views here.


def index(req):
    # Rendering a template
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_questions': latest_questions,
    }
    return render(req, "polls/index.html", context)


def detail(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/detail.html", {"question": question})


def results(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/results.html', {'question': question})


def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=req.POST["choice"])
    except:
        return render(req, "polls/detail.html", {"question": question, "error_message": "Please Select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

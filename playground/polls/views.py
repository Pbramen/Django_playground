from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Choice, Question
from django.db.models import F
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# This contains only the content of the page (for styling, look for template.py)
# Create your views here.
def index(request):
    # return limit of 5 questions, sorted by decending published date (newest first)! 
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }
    return HttpResponse(template.render(context, request))

# def detail(request, question_id):
#     return HttpResponse("Your looking at question %s" % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {"question": question})

def vote(request, question_id):
    # if get_object_or_404 fails, stops the rest of the function.
    question = get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request, 
            'polls/detail.html',
            {
                "question": question,
                "error_message": "You didn't select a choice"
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

#get_object_or_404 is great for DRY and loose coupling, but we should probably have a 404.html page to redirect to!
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

# def handler_404(request, exception):
#     return render(request, "polls/404_page.html")



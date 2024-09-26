from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Choice, Question
from django.db.models import F
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic 
from django.utils import timezone
##############################################################
# Basic building block for views (non generic/ not DRY)

# This contains only the content of the page (for styling, look for template.py)
# Create your views here.
# def index(request):
     # return limit of 5 questions, sorted by decending published date (newest first)! 
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list
#     }
#     return HttpResponse(template.render(context, request))

# def detail(request, question_id):
#     return HttpResponse("Your looking at question %s" % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {"question": question})

#get_object_or_404 is great for DRY and loose coupling, but we should probably have a 404.html page to redirect to!
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

# def handler_404(request, exception):
#     return render(request, "polls/404_page.html")

##############################################################


# defining the template_name ensures different views will be rendered even if they have the same generic views.
# ListView context is defined via get_queryset(self) and by default renamed question_list.
#   you can override this by setting context_object_name = "something_else".
class IndexView(generic.ListView):
    template_name= "polls/index.html"
    context_object_name= "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

# DetailView - remember in url, we passed in <int:pk> in the url parameters.
# context now automatically passes the context question into the model by default.
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

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




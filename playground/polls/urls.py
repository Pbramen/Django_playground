from . import views
from django.urls import path

# namespaceing urls
app_name="polls"
# django will traversal these routes in order! 
# try to keep frequently hit routes in earlier indexes. 

# to use generic views, call the function .as_view()
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),    
]

# notice that the argument <int:pk> is used for generic view urls. See the implementation in views.py
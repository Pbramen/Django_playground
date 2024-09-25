from . import views
from django.urls import path

# namespaceing urls
app_name="polls"
# django will traversal these routes in order! 
# try to keep frequently hit routes in earlier indexes. 
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),    
]

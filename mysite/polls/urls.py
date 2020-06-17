from django.urls import path
from django.conf.urls import url
from . import views

# app names allow for a name space so in urls you can have a path:[]
app_name = "polls"
urlpatterns = [
    path('', views.index, name="index"),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
]

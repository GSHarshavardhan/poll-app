from django.urls import path
from . import views

urlpatterns = [
    path('polls/', views.polls_view),
    path('vote/', views.vote_view),
]
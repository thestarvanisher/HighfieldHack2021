from django.urls import path

from HighfieldHack2021.apps.debates import views

urlpatterns = [
    path("create/", views.create_debate),
    path("view/", views.view_debates),
    path("createpoll/", views.create_poll),
    path("", views.view_index),
]

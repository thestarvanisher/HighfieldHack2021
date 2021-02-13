from django.urls import path

from HighfieldHack2021.apps.debates import views

urlpatterns = [
    path("", views.view_index),
]

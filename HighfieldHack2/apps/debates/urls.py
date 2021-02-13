from django.urls import path

from HighfieldHack2.apps.debates import views

urlpatterns = [
    path("create/", views.create_debate),
    path("view/<int:pk>/", views.view_debate),
    path("view/<int:pk>/create_arg/<int:is_for>/", views.create_argument),
    path("", views.view_index),
]

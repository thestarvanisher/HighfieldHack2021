from django.urls import path

from HighfieldHack2.apps.debates import views

urlpatterns = [
    path("create/debate/", views.create_debate),
    path("debate/view/<int:pk>/", views.view_debate),
    path("debate/view/<int:pk>/create_arg/<int:is_for>/", views.create_argument),
    path("create/poll/", views.create_poll),
    path("poll/view/<int:pk>/", views.view_poll),
    path("poll/view/<int:pk>/create_choice/", views.create_poll_choice),
    path("", views.view_index),
]

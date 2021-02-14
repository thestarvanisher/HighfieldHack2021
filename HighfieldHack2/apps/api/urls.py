from django.urls import path, include

from HighfieldHack2.apps.api import views

urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("debates/", views.DebateList.as_view()),
    path("debates/<str:pk>/", views.DebateDetail.as_view()),
    path("arguments/", views.ArgumentList.as_view()),
    path("arguments/<str:pk>/", views.ArgumentDetail.as_view()),
    path("votes/", views.VoteList.as_view()),
    path("votes/<str:pk>/", views.VoteList.as_view()),
]

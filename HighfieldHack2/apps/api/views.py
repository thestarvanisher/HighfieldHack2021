# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from HighfieldHack2.apps.api.permissions import IsOwner
from HighfieldHack2.apps.core.serializers import DebateSerializer
from HighfieldHack2.apps.core.models import Debate


class CustomRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated & (IsOwner | IsAdminUser)]


class CustomListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        serializer.save(owner=user)


class DebateList(CustomListCreateAPIView):
    serializer_class = DebateSerializer

    def get_queryset(self):
        return queryset(self.request, Debate)


class DebateDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DebateSerializer

    def get_queryset(self):
        return queryset(self.request, Debate)


class ArgumentList(CustomListCreateAPIView):
    serializer_class = DebateSerializer

    def get_queryset(self):
        return queryset(self.request, Debate)


class ArgumentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DebateSerializer

    def get_queryset(self):
        return queryset(self.request, Debate)


def queryset(request, Model):
    user = request.user

    models = Model.objects.all()

    return models if user.is_staff else models.filter(owner=user.id)

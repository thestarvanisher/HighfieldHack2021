from rest_framework import serializers

from HighfieldHack2021.apps.core.models import Debate, TextArgument


class DebateSerializer(serializers.ModelSerializer):
    expires_at = serializers.DateTimeField()

    class Meta:
        model = Debate
        fields = ("title", "description", "owner", "posted_at", "expires_at")


class TextArgumentSerializer(serializers.ModelSerializer):
    debate = DebateSerializer()

    class Meta:
        model = TextArgument
        fields = ("title", "description", "owner", "debate", "posted_at")

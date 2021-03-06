from rest_framework import serializers

from HighfieldHack2.apps.core.models import Debate, DebateTextArgument, DebateVote, PollChoiceVote, PollChoice, Poll


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebateVote
        fields = "__all__"


class TextArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebateTextArgument
        fields = "__all__"


class DebateSerializer(serializers.ModelSerializer):
    expires_at = serializers.DateTimeField()
    debate_votes = VoteSerializer(many=True)
    debate_arguments = TextArgumentSerializer(many=True)

    class Meta:
        model = Debate
        fields = ("title", "description", "owner", "debate_votes", "debate_arguments", "posted_at", "expires_at")
        read_only_fields = ("debate_votes", "debate_arguments")


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollChoice
        fields = ()


class ChoiceVoteSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer()

    class Meta:
        model = PollChoiceVote
        fields = ("choice",)


class PollSerializer(serializers.ModelSerializer):
    poll_choices = ChoiceSerializer(many=True)

    class Meta:
        model = Poll
        fields = ("title", "description", "owner", "poll_choices", "posted_at", "expires_at")
        read_only_fields = ("poll_choices",)

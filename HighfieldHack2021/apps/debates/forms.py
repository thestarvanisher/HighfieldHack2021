from django.forms import forms

from HighfieldHack2021.apps.core.models import Debate, Poll, PollChoice, PollChoiceVote, DebateTextArgument


class DebateForm(forms.Form):
    class Meta:
        model = Debate
        fields = ("title", "description", "expires_at")


class PollChoiceVoteForm(forms.Form):
    class Meta:
        model = PollChoiceVote
        fields = ("choice",)


class PollForm(forms.Form):
    class Meta:
        model = Poll
        fields = ("title", "description", "expires_at")


class PollChoiceForm(forms.Form):
    class Meta:
        model = PollChoice


class DebateTextArgumentForm(forms.Form):
    class Meta:
        model = DebateTextArgument
        fields = ("title", "description")

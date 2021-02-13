from django import forms

from HighfieldHack2021.apps.core.models import Debate, Poll, PollChoice, PollChoiceVote, DebateTextArgument


class DebateForm(forms.ModelForm):
    class Meta:
        model = Debate
        fields = ("title", "description", "expires_at")
        


class PollChoiceVoteForm(forms.ModelForm):
    class Meta:
        model = PollChoiceVote
        fields = ("choice",)


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ("title", "description", "expires_at")


class PollChoiceForm(forms.ModelForm):
    class Meta:
        model = PollChoice
        fields = ("title",)


class DebateTextArgumentForm(forms.ModelForm):
    class Meta:
        model = DebateTextArgument
        fields = ("title", "description")

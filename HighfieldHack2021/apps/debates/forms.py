from django.forms import forms

from HighfieldHack2021.apps.core.models import Debate, Poll, PollChoice


class DebateForm(forms.Form):
    class Meta:
        model = Debate


class ChoiceVote(forms.Form):
    class Meta:
        model = Debate


class PollForm(forms.Form):
    class Meta:
        model = Poll


class PollChoiceForm(forms.Form):
    class Meta:
        model = PollChoice

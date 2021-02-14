from bulma_widget import widgets
from django import forms
from django.forms import ModelForm

from HighfieldHack2.apps.core.models import Debate, DebateTextArgument, Poll, PollChoice


class DebateForm(ModelForm):
    expires_at = forms.DateField(widget=widgets.BulmaDateInput)

    class Meta:
        model = Debate
        fields = ("title", "description", "expires_at")


class DebateTextArgumentForm(ModelForm):
    class Meta:
        model = DebateTextArgument
        fields = ("title", "description", "is_for")


class PollForm(DebateForm):
    class Meta:
        model = Poll
        fields = ("title", "description", "expires_at")


class PollChoices(ModelForm):
    class Meta:
        model = PollChoice
        fields = ("title",)

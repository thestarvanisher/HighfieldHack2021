from django.conf import settings
from django.db import models

# Create your models here.
from HighfieldHack2021.apps.core.helpers import date_in_future


class Debate(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(validators=[date_in_future])


class DebateTextArgument(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE, related_name="debate_arguments")
    posted_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("title", "debate")


class Poll(Debate):
    pass


class Choice(models.Model):
    title = models.CharField(max_length=50)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices")

    class Meta:
        unique_together = ("title", "poll")


class ChoiceVote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="choice_votes")

    class Meta:
        unique_together = ("choice", "owner")


class DebateVote(models.Model):
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE, related_name="debate_votes")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("debate", "owner")

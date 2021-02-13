from django.conf import settings
from django.db import models


# Create your models here.
class Debate(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField()


class DebateTextArgument(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_for = models.BooleanField()
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE, related_name="debate_arguments")
    posted_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("title", "debate")


class Poll(Debate):
    pass


class PollChoice(models.Model):
    title = models.CharField(max_length=50)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices")

    class Meta:
        unique_together = ("title", "poll")


class PollChoiceVote(models.Model):
    choice = models.ForeignKey(PollChoice, on_delete=models.CASCADE, related_name="choice_votes")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("choice", "owner")


class DebateVote(models.Model):
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE, related_name="debate_votes")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("debate", "owner")

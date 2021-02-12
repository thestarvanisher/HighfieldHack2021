from django.contrib import admin

# Register your models here.
from HighfieldHack2021.apps.core.models import Debate, DebateTextArgument, DebateVote, Poll, ChoiceVote, Choice


class DebateAdmin(admin.ModelAdmin):
    model = Debate
    list_display = ("title", "description", "owner", "posted_at", "expires_at")
    list_filter = ("title", "owner")
    search_fields = ("title", "owner")


class DebateTextArgumentAdmin(admin.ModelAdmin):
    model = DebateTextArgument
    list_display = ("title", "description", "owner", "debate", "posted_at")
    list_filter = ("title", "owner", "debate")
    search_fields = ("title", "owner", "debate")


class DebateVoteAdmin(admin.ModelAdmin):
    model = DebateVote
    list_display = ("debate", "owner")
    list_filter = ("debate", "owner")
    search_fields = ("debate", "owner")


class PollAdmin(DebateAdmin):
    model = Poll


class ChoiceAdmin(admin.ModelAdmin):
    model = DebateTextArgument
    list_display = ("title", "poll")
    list_filter = ("title", "poll")
    search_fields = ("title", "poll")


class ChoiceVoteAdmin(admin.ModelAdmin):
    model = DebateTextArgument
    list_display = ("choice", "owner")
    list_filter = ("choice", "owner")
    search_fields = ("choice", "owner")


admin.site.register(Debate, DebateAdmin)
admin.site.register(DebateTextArgument, DebateTextArgumentAdmin)
admin.site.register(DebateVote, DebateVoteAdmin)

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(ChoiceVote, ChoiceVoteAdmin)

from django.contrib import admin

# Register your models here.
from HighfieldHack2021.apps.core.models import Debate, DebateTextArgument, DebateVote, Poll, PollChoiceVote, PollChoice


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


class PollChoiceInline(admin.StackedInline):
    model = PollChoice
    extra = 2


class PollAdmin(DebateAdmin):
    model = Poll
    inlines = [PollChoiceInline]


class PollChoiceAdmin(admin.ModelAdmin):
    model = DebateTextArgument
    list_display = ("title", "poll")
    list_filter = ("title", "poll")
    search_fields = ("title", "poll")


class PollChoiceVoteAdmin(admin.ModelAdmin):
    model = PollChoiceVote
    list_display = ("choice", "owner")
    list_filter = ("choice", "owner")
    search_fields = ("choice", "owner")


admin.site.register(Debate, DebateAdmin)
admin.site.register(DebateTextArgument, DebateTextArgumentAdmin)
admin.site.register(DebateVote, DebateVoteAdmin)

admin.site.register(Poll, PollAdmin)
admin.site.register(PollChoice, PollChoiceAdmin)
admin.site.register(PollChoiceVote, PollChoiceVoteAdmin)

from django.contrib import admin

# Register your models here.
from HighfieldHack2021.apps.core.models import Debate, TextArgument


class DebateAdmin(admin.ModelAdmin):
    model = Debate
    list_display = ("title", "description", "owner", "posted_at", "expires_at")
    list_filter = ("title", "owner")
    search_fields = ("title", "owner")


class TextArgumentAdmin(admin.ModelAdmin):
    model = TextArgument
    list_display = ("title", "description", "owner", "debate", "posted_at")
    list_filter = ("title", "owner", "debate")
    search_fields = ("title", "owner", "debate")


admin.site.register(Debate, DebateAdmin)
admin.site.register(TextArgument, TextArgumentAdmin)

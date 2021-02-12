from django.contrib.auth.decorators import login_required
# Create your views here.
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render

from HighfieldHack2021.apps.core.models import Poll, PollChoice
from HighfieldHack2021.apps.debates.forms import DebateForm


def create(request, Form):
    if request.method == "POST":
        form = Form(request.POST)

        if form.is_valid():
            form = form.save(commit=False)

            form.owner = request.user
            form.save()

            return None
    else:
        return Form()


@login_required
def create_debate(request):
    form = create(request, DebateForm)

    if form is not None:
        return redirect("/")

    context = {
        "form": form
    }

    return render(request, "create_debate.html", context=context)


@login_required
def create_poll(request):
    form = create(request, inlineformset_factory(Poll, PollChoice))

    if form is not None:
        return redirect("/")

    context = {
        "form": form
    }

    return render(request, "create_poll.html", context=context)

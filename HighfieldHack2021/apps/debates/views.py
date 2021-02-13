from django.contrib.auth.decorators import login_required
# Create your views here.
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render, get_object_or_404

from django.forms.models import BaseInlineFormSet
from HighfieldHack2021.apps.core.models import Poll, PollChoice, Debate
from HighfieldHack2021.apps.debates.forms import DebateForm
from HighfieldHack2021.apps.debates.helpers import get_page, get_objects


def create(request, Form):
    if request.method == "POST":
        form = Form(data=request.POST)

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

    print(form)

    if form is None:
        return redirect("/")

    context = {
        "form": form
    }

    return render(request, "create_debate.html", context=context)


@login_required
def create_poll(request):
    form = create(request, inlineformset_factory(Poll, PollChoice, formset=BaseInlineFormSet))

    if form is None:
        return redirect("/")

    context = {
        "form": form
    }

    return render(request, "create_poll.html", context=context)


@login_required
def view_debates(request):
    page = get_page(request)

    debates,_ = get_objects(Debate, page)

    context = {
        "debates": debates
    }

    return render(request, "view_debates.html", context=context)


@login_required
def view_polls(request):
    page = get_page(request)

    polls = get_objects(Poll, page)

    context = {
        "polls": polls
    }

    return render(request, "view_polls.html", context=context)


@login_required
def view_debate(request, pk=None):
    debate = get_object_or_404(Debate, id=pk)

    context = {
        "debate": debate
    }

    return render(request, "view_debate.html", context=context)


@login_required
def view_poll(request, pk=None):
    poll = get_object_or_404(Poll, id=pk)

    context = {
        "poll": poll
    }

    return render(request, "view_poll.html", context=context)


def view_index(request):
    context = {
        "user": request.user
    }
    return render(request, "index.html", context=context)

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from HighfieldHack2.apps.core.models import Debate, DebateTextArgument, Poll, PollChoice
from HighfieldHack2.apps.debates.forms import DebateForm, DebateTextArgumentForm, PollForm, PollChoices


@login_required
def create_debate(request):
    if request.method == "POST":
        form = DebateForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)

            form.owner = request.user
            form.save()

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'event_senddebate',
                {
                    'type': 'sendDebate',
                    'id': form.id,
                    'desc': form.description,
                    'title': form.title
                }
            )

            return redirect("/")
    else:
        form = DebateForm()

    context = {
        "form": form,
        "back": "/debates/"
    }

    return render(request, "create_debate.html", context=context)


@login_required
def view_debate(request, pk=None):
    debate = get_object_or_404(Debate, pk=pk)

    relevant_arguments = DebateTextArgument.objects.all().filter(debate=debate)

    context = {
        "debate": debate,
        "arguments_for": relevant_arguments.filter(is_for=True),
        "arguments_against": relevant_arguments.filter(is_for=False),
        "back": "/debates/"
    }

    return render(request, "view_debate.html", context=context)


@login_required
def view_index(request):
    context = {
        "debates": Debate.objects.order_by("-posted_at"),
        "polls": Poll.objects.order_by("-posted_at")
    }

    return render(request, "index.html", context=context)


@login_required
def create_argument(request, pk=None, is_for=None):
    if is_for == 1:
        is_for = True
    else:
        is_for = False

    debate = get_object_or_404(Debate, pk=pk)

    if request.method == "POST":
        form = DebateTextArgumentForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)

            form.owner = request.user
            form.debate = debate

            form.save()

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'event_sendarg',
                {
                    'type': 'sendArg',
                    'is_for': form.is_for,
                    'id': pk,
                    'desc': form.description,
                    'title': form.title
                }
            )

            return redirect("/debates/debate/view/{}/".format(pk))
    else:
        form = DebateTextArgumentForm()

    form.fields["is_for"].initial = is_for

    context = {
        "debate": debate,
        "form": form,
        "back": "/debates/debate/view/{}/".format(pk)
    }

    return render(request, "add_argument.html", context=context)


@login_required
def create_poll(request):
    if request.method == "POST":
        form = PollForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)

            form.owner = request.user
            form.save()

            return redirect("/")
    else:
        form = PollForm()

    context = {
        "form": form,
        "back": "/"
    }

    return render(request, "create_poll.html", context=context)


def create_poll_choice(request, pk=None):
    poll = get_object_or_404(Poll, pk=pk)

    if request.method == "POST":
        form = PollChoices(request.POST)

        if form.is_valid():
            form = form.save(commit=False)

            form.poll = poll

            form.save()

            return redirect(f"/debates/poll/view/{pk}/")
    else:
        form = PollChoices()

    context = {
        "poll": poll,
        "choices": PollChoice.objects.all().filter(poll=poll),
        "form": form,
        "back": f"/debates/"
    }

    return render(request, "add_choice.html", context=context)


def view_poll(request, pk=None):
    poll = get_object_or_404(Poll, pk=pk)

    context = {
        "poll": poll,
        "choices": PollChoice.objects.all().filter(poll=poll),
        "back": f"/debates/"
    }

    return render(request, "view_poll.html", context=context)

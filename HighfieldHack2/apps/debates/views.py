from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import redirect, render, get_object_or_404

from HighfieldHack2.apps.core.models import Debate, DebateTextArgument
from HighfieldHack2.apps.debates.forms import DebateForm, DebateTextArgumentForm


@login_required
def create_debate(request):
    if request.method == "POST":
        form = DebateForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)

            form.owner = request.user
            form.save()

            return redirect("/")
    else:
        form = DebateForm()

    context = {
        "form": form
    }

    return render(request, "create_debate.html", context=context)


@login_required
def view_debate(request, pk=None):
    debate = get_object_or_404(Debate, pk=pk)

    relevant_arguments = DebateTextArgument.objects.all().filter(debate=debate)

    context = {
        "debate": debate,
        "arguments_for": relevant_arguments.filter(is_for=True),
        "arguments_against": relevant_arguments.filter(is_for=False)
    }

    return render(request, "view_debate.html", context=context)


@login_required
def view_index(request):
    context = {
        "debates": Debate.objects.order_by("-posted_at")
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

            return redirect("/")
    else:
        form = DebateTextArgumentForm()

    form.fields["is_for"].initial = is_for

    context = {
        "debate": debate,
        "form": form
    }

    return render(request, "add_argument.html", context=context)

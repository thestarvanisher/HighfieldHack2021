from django.contrib import messages
from django.contrib.auth import logout as django_logout, login as django_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
def login(request, next_page="/"):
    if request.user.is_authenticated:
        return redirect(next_page)

    print(request.method)
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                django_login(request, user)
                messages.info(request, f"You are logged in as {username}.")

                return redirect(next_page)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    context = {
        "form": form
    }

    return render(request, "login.html", context=context)


@login_required
def logout(request):
    django_logout(request)
    return redirect("/")

def index(request):
    return render(request, "index.html")
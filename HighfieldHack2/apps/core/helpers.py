import datetime

from django.forms import forms


def date_in_future(date):
    if date <= datetime.datetime.today():
        raise forms.ValidationError("The date cannot be in the past!")

    return date

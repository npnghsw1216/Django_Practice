from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

signup = CreateView.as_view(
    form_class=UserCreationForm,
    success_url=reverse_lazy("accounts:login"),
    # template_name="",
)


def signup(request):
    pass


def login(request):
    pass


def profile(request):
    pass


def logout(request):
    pass
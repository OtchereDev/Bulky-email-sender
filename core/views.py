from django.shortcuts import render
from django.views.generic import CreateView
from .forms import EmailCreateFom
from .models import Emailer


class EmailCreateView(CreateView):
    model = Emailer
    template_name = "emailer.html"
    form_class=EmailCreateFom

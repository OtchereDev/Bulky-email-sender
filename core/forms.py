from .models import Emailer,EmailContacts
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _


class EmailCreateFom(ModelForm):
    email_list=forms.CharField()

    class Meta:
        model=Emailer
        exclude=['date_sent','email_reciever']

    def save(self,*args, **kwargs):
        # loop over the email list with split on "," and create email contact
        # then the create the emailer object
        pass
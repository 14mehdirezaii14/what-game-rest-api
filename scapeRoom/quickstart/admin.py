from django import forms
from django.contrib import admin
from whatGame.views import TicketView

class PersonForm(forms.ModelForm):

    class Meta:
        model = TicketView
        exclude = ['name']

class PersonAdmin(admin.ModelAdmin):
    exclude = ['age']
    form = TicketView

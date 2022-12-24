from django.contrib import admin
from django.apps import apps
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('date','timee','nameGame')

# model registered with custom admin
admin.site.register(Ticket, TicketAdmin)

# all other models
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

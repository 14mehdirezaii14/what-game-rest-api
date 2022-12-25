from django.contrib import admin
from django.apps import apps
from .models import Ticket
from .models import EscapeRoom
from .models import disableDate


class TicketAdmin(admin.ModelAdmin):
    list_display = ('date', 'timee', 'nameGame')


class EscapeRoomAmin(admin.ModelAdmin):
    list_display = ('name',)


class disableDateAmin(admin.ModelAdmin):
    list_display = ('date',)


# model registered with custom admin
admin.site.register(Ticket, TicketAdmin)
admin.site.register(EscapeRoom, EscapeRoomAmin)
admin.site.register(disableDate,disableDateAmin)

# all other models
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

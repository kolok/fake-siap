from django.contrib import admin

from .models import (
    Administration,
    Bailleur,
    Operation,
)

admin.site.register(Administration)
admin.site.register(Bailleur)
admin.site.register(Operation)

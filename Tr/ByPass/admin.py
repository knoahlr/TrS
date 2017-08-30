from django.contrib import admin

from .models import ByPassRequest


class ByPassAdmin(admin.ModelAdmin):
    list_display = ('CommitNO', 'GerritLink', 'Pub_date')

admin.site.register(ByPassRequest, ByPassAdmin)

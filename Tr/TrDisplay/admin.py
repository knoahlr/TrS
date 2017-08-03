from django.contrib import admin

from .models import TrClass


class TrAdmin(admin.ModelAdmin):
    list_display = ('Tr_NO', 'FromTeam', 'ToTeam', 'Prior_Int', 'Pub_date', 'owner', 'comments')

admin.site.register(TrClass, TrAdmin)
# Register your models here.

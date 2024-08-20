from django.contrib import admin
from .models import *

class MatabaseAdmin(admin.ModelAdmin):
    list_filter = [
        'status',
        'createdDate'
    ]
    search_fields = [
        'title',
        'year'
    ]

admin.site.register(Matabase, MatabaseAdmin)
admin.site.register(Footer)
# admin.site.register(Mag)
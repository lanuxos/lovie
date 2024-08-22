from django.contrib import admin
from django.apps import apps
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

# register every models at once
# app = apps.get_app_config('matabase')
# for model_name, model in app.models.items():
#     admin.site.register(model)
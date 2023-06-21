from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.
"""
    Register all models at once
"""
from django.apps import apps

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        continue

from django.contrib import admin

# Register your models here.
"""
    Register all models at once
"""
from django.apps import apps


models = apps.get_models()

for model in models:
    admin.site.register(model)
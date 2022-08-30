from django.contrib import admin
from django.db.models import Model
import inspect
from . import models

# Register your models here.
model_classes = []
for _, v in inspect.getmembers(models, inspect.isclass):
    if isinstance(v, Model):
        model_classes.append(v)

admin.site.register(model_classes)
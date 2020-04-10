from django.contrib import admin
from .import models
# Register your models here.
admin.site.register(models.Photocard)
admin.site.register(models.Project)
admin.site.register(models.Certificate)
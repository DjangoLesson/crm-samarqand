from django.contrib import admin

from . import models


admin.site.register(models.District)
admin.site.register(models.Family)
admin.site.register(models.FamilyMember)
admin.site.register(models.House)
admin.site.register(models.Mahalla)
admin.site.register(models.Person)
admin.site.register(models.Street)
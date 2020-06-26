from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Contact)
admin.site.register(models.Entry)
admin.site.register(models.EntryContent)
admin.site.register(models.NewsLetter)
admin.site.register(models.SiteInfo)
admin.site.register(models.SocialAccounts)
admin.site.register(models.Speaker)




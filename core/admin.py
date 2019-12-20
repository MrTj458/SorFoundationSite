from django.contrib import admin
from . import models

admin.site.site_header = 'Shool Of Rock Foundation Administration'
admin.site.site_title = 'SOR Foundation'

admin.site.register(models.Sponsor)

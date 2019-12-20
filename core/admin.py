from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models

admin.site.site_header = 'Shool Of Rock Foundation Administration'
admin.site.site_title = 'SOR Foundation'


class RecipientModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(models.Sponsor)
admin.site.register(models.Recipient, RecipientModelAdmin)

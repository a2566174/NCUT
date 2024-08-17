from django.contrib import admin
from mysite.models import post

class postadmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')
admin.site.register(post)
# Register your models here.

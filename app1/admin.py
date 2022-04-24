from django.contrib import admin
from .models import email_user, emai_l, schedule_task
# Register your models here.

admin.site.register(email_user)
admin.site.register(emai_l)
admin.site.register(schedule_task)
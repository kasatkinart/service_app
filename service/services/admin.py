from django.contrib import admin

from services.models import Plan, Subscription, Service

# Register your models here.
admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(Service)

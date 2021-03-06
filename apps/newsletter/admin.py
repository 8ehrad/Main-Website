from django.contrib import admin
from apps.newsletter.models import *

# Register your models here.

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    fields = ['email', 'date_joint', 'unsubscribed', 'date_unsubscribed']


@admin.register(EmailText)
class EmailTextAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields':['subject', 'text', 'link', 'link_text'] ,
            'description': "دقت کنید! پس از اولین بار کلیک بر روی دکمه ذخیره، محتوای این صفحه قابل ویرایش نیست."
        }),
    )
    # fields = ['subject', 'text', 'link']



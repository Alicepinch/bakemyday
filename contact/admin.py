from django.contrib import admin
from .models import ContactInquiry


class ContactAdmin(admin.ModelAdmin):

    list_display = (
            "name",
            "email",
            "subject",
            "message",
            "created_on"
    )

    readonly_fields = (
            "name",
            "email",
            "subject",
            "message",
            "created_on"
    )


admin.site.register(ContactInquiry, ContactAdmin)

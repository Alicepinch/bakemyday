from django import forms
from .models import ContactInquiry


class ContactForm(forms.ModelForm):
    """Create Contact form for users to contact admin"""

    class Meta:
        model = ContactInquiry
        fields = (
            'name',
            'email',
            'subject',
            'message',
            )

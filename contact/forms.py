from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Create Contact form for users to contact admin"""

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message',
            )

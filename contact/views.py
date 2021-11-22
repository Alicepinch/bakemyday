from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact_us(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():

            # Fetches user informaion from form
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']

            # Fetches default email from settings
            admin_email = settings.DEFAULT_FROM_EMAIL

            # Saves contact details to database
            contact_details = contact_form.save(commit=False)
            contact_details.save()

            # Sends Email to store owner's email
            subject = render_to_string(
                'contact/emails/email-subject.txt',
                {'subject': subject})
            body = render_to_string(
                'contact/emails/email-body.txt',
                {'message': message, 'email': email, 'name': name})
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [admin_email]
            )
            messages.info(
                request, 'Thank you for getting in touch! \
                    Someone will get back to you shortly')
            return redirect(reverse('contact_us'))
        else:
            messages.error(
                request, 'Sorry! Something went wrong with \
                    your form please try again')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }
    template = 'contact/contact-us.html'
    return render(request, template, context)

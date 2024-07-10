from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactRequestForm

def contact(request):
    """
    A view to return the contact page with the form
    """
    form = ContactRequestForm()

    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)

def contact_form(request):
    """Send contact form"""
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            contact_request = form.save()
            messages.success(request, 'Your message has been sent!')

            # Send the user a confirmation email
            user_email = contact_request.email
            subject = render_to_string(
                'contact/contact_form_confirmation_subject.txt')
            body = render_to_string(
                'contact/contact_form_confirmation_body.txt',
                {'contact_email': settings.DEFAULT_FROM_EMAIL})

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [user_email]
            )

            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Failed to send message. Please try again.')
    else:
        form = ContactRequestForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

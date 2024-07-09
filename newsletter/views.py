from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import NewsletterSubscription
from .forms import NewsletterSubscriptionForm


def subscribe(request):
    """ Subscribe to a newsletter """
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            member = form.save()
            messages.success(request, 'Thank you for subscribing!')

            """Send a confirmation email"""
            subject = render_to_string(
                'newsletter/subscription_subject.txt')
            body = render_to_string(
                'newsletter/subscription_body.txt',
                {'contact_email': settings.DEFAULT_FROM_EMAIL})

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [member.email]
            )

        else:
            messages.error(request, 'There was an error with your submission. Please try again.')

    return redirect(request.META.get('HTTP_REFERER', '/'))

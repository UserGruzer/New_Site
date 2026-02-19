
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Главные страницы
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# Для отображения самой страницы (GET)
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # локальный тест — письмо в консоль
        send_mail(
            subject=f"Сообщение с сайта от {name}",
            message=f"Email: {email}\n\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        messages.success(request, "Message sent successfully!")

    return render(request, "contact.html")

def reviews(request):
    return render(request, 'reviews.html')

def hire_us(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()
        website_url = request.POST.get("website_url", "").strip()

        if website_url:
            messages.success(request, "Your request has been received!")
            return redirect("hire-us")

        if not name or not email or not message:
            messages.error(request, "Please fill in all required fields.")
            return render(request, "hire-us.html", locals())

        try:
            send_mail(
                subject=f"Новый запрос Hire Us от {name}",
                message=f"Имя: {name}\nEmail: {email}\nТелефон: {phone}\n\nСообщение:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            send_mail(
                subject="We received your request",
                message=f"Dear {name},\n\nThank you for contacting us. We will review your request and get back to you shortly.\n\nYour message:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=True,
            )

            messages.success(request, "Your request has been sent successfully! We will contact you soon.")
        except Exception:
            messages.error(request, "Failed to send your request. Please try again or email us directly.")

        return redirect("hire_us")

    return render(request, "hire-us.html")

def crypto_recovery(request):
    return render(request, 'crypto-recovery.html')

def wallet_access(request):
    return render(request, 'wallet-access.html')

def fund_tracing(request):
    return render(request, 'fund-tracing.html')

# Ethical Hack
def phone_email_access(request):
    return render(request, 'phone-email-access.html')

def track_and_trace(request):
    return render(request, 'track-and-trace.html')

def social_media_removal(request):
    return render(request, 'social-media-content-removal.html')
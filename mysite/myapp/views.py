
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

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
    return render(request, 'hire-us.html')  # ваша адаптированная страница "Start For Free"

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
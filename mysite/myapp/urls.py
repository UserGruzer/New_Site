# mysite/urls.py

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Главная страница
    path('', views.home, name='home'),  # index.html


    # Основные страницы
    path('about/', views.about, name='about'),  # about.html

    path('contact/', views.contact, name='contact'),  # GET — показ страницы
    # contact.html

    path('reviews/', views.reviews, name='reviews'),  # reviews.html
    path('hire-us/', views.hire_us, name='hire_us'),


    # Crypto Recovery
    path('crypto-recovery/', views.crypto_recovery, name='crypto_recovery'),
    path('wallet-access/', views.wallet_access, name='wallet_access'),
    path('fund-tracing/', views.fund_tracing, name='fund_tracing'),

    # Ethical Hack
    path('phone-email-access/', views.phone_email_access, name='phone_email_access'),
    path('track-and-trace/', views.track_and_trace, name='track_and_trace'),
    path('social-media-content-removal/', views.social_media_removal, name='social_media_removal'),
]
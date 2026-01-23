from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    class Meta:
        verbose_name = "Сообщение с сайта"
        verbose_name_plural = "Сообщения с сайта"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.email} ({self.created_at:%d.%m.%Y %H:%M})"
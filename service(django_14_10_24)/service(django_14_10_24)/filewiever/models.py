from django.db import models
from django.utils.translation import gettext_lazy as _

class Image(models.Model):
    image = models.ImageField(upload_to='filewiever/gallery_images/')  # Путь для хранения изображений
    title = models.CharField(_('Title'), max_length=255, blank=True)
    description = models.TextField(_('Description'), blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title or f"Image {self.pk}"

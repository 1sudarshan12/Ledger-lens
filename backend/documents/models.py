from django.conf import settings
from django.db import models   


# Create your models here.
class Document(models.Model):
    class Status(models.TextChoices):
        READY = "READY", "Ready"
        PROCESSING = "PROCESSING", "Processing"
        FAILED = "FAILED", "Failed"
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PROCESSING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "documents"
        ordering= ["-created_at"]
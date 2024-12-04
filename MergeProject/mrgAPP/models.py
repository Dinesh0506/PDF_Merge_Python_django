from django.db import models

from django.db import models

class PDFDocument(models.Model):
    name = models.CharField(max_length=100)  # File name
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp of upload
    file = models.FileField(upload_to='documents/')  # File upload location

    def __str__(self):
        return self.name

from django.db import models
from cryptography.fernet import Fernet

class Snippet(models.Model):
    content = models.TextField()
    encrypted = models.BooleanField(default=False)
    encryption_key = models.CharField(max_length=44, blank=True)
    

    def save(self, *args, **kwargs):
        if self.encrypted and self.encryption_key:
            fernet = Fernet(self.encryption_key.encode())
            self.content = fernet.encrypt(self.content.encode()).decode()
        super().save(*args, **kwargs)

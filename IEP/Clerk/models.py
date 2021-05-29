from django.contrib.auth.models import AbstractUser
from django.db import models 

class Document(models.Model):
    document_name = models.CharField(
        max_length=30,
        null=False,
        unique=True
    )     

    def __str__(self):
        return self.document_name
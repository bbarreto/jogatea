from django.conf import settings
from django.db import models

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your models here.
class BoardButton(models.Model):
    identifier = models.CharField(max_length=32)
    button_text = models.CharField(max_length=200)
    button_label = models.CharField(max_length=30)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
import uuid
from django.conf import settings
from django.db import models

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

def user_directory_path(instance, filename):
    return "static/uploads/user_{0}/{1}_{2}".format(instance.author.id, str(uuid.uuid4()), filename)

# Create your models here.
class BoardButton(models.Model):
    identifier = models.CharField(max_length=32)
    button_text = models.CharField(max_length=200)
    button_label = models.CharField(max_length=30)
    button_image = models.ImageField(upload_to=user_directory_path, null=True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
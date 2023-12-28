from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    document = models.FileField(upload_to='')
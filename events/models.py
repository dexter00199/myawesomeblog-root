from django.db import models

# Create your models here.
class Events(models.Model):
    event_image = models.ImageField(upload_to='')
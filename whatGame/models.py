from django.db import models

# Create your models here.
class Ticket(models.Model):
    date = models.TextField()
    
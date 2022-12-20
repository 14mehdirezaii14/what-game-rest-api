from django.db import models

# Create your models here.


class Ticket(models.Model):
    date = models.TextField(max_length=140, blank=False,null=False)
    timee = models.TextField(max_length=140, blank=False,null=False)
    numberOfPersons = models.TextField(max_length=140, blank=False,null=False)
    name = models.TextField(max_length=140, blank=False,null=False)
    lastName = models.TextField(max_length=140, blank=False,null=False)
    email = models.TextField(max_length=140, blank=False,null=False)
    phone = models.TextField(max_length=140, blank=False,null=False)

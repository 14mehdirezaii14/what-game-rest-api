from django.db import models

# Create your models here.


class Ticket(models.Model):
    nameGame = models.TextField(max_length=140, blank=False, null=False)
    date = models.TextField(max_length=140, blank=False, null=False)
    timee = models.TextField(max_length=140, blank=False, null=False)
    numberOfPersons = models.TextField(max_length=140, blank=False, null=False)
    name = models.TextField(max_length=140, blank=False, null=False)
    lastName = models.TextField(max_length=140, blank=False, null=False)
    email = models.TextField(max_length=140, blank=False, null=False)
    phone = models.TextField(max_length=140, blank=False, null=False)
    price = models.TextField(max_length=140, blank=False, null=False)


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class EscapeRoom(models.Model):
    genre = models.CharField(max_length=30, blank=False, null=False)
    name = models.CharField(max_length=300, blank=False, null=False)
    timee = models.CharField(max_length=30, blank=False, null=False)
    capacity = models.CharField(max_length=30, blank=False, null=False)
    degreeOfDifficulty = models.CharField(
        max_length=30, blank=False, null=False)
    age = models.CharField(max_length=30, blank=False, null=False)
    price = models.CharField(max_length=30, blank=False, null=False)
    scenario = models.TextField(max_length=540, blank=False, null=False)
    gameTips = models.TextField(max_length=540, blank=False, null=False)
    viewMoreGameTips = models.TextField(
        max_length=540, blank=False, null=False)
    img = models.ImageField(upload_to=upload_to, blank=True, null=True)
    
    
    
class disableDate(models.Model):
    date = models.CharField(max_length=30, blank=False, null=False)

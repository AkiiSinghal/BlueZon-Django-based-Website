from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Match(models.Model):
    TYPE_CHOICES = (('Solo','Solo'), ('Duo','Duo'), ('Squad','Squad'),)
    VERSION_CHOICES = (('TPP','TPP'), ('FPP','FPP'),)
    MAP_CHOICES = (('Erangel','Erangel'), ('Miramar','Miramar'), ('Sanhok','Sanhok'), ('Vikendi','Vikendi'),)
    name = models.CharField(max_length=20, blank=False)
    slug = models.SlugField(max_length=20, blank=False)
    time = models.TimeField(blank=False)
    date = models.DateField(blank=False)
    available = models.BooleanField(blank=True, default=True)
    prize = models.IntegerField(blank=False)
    kills = models.IntegerField(blank=False)
    fees = models.IntegerField(blank=False)
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='Solo')
    version = models.CharField(max_length=4, choices=VERSION_CHOICES, default='TPP')
    map = models.CharField(max_length=8, choices=MAP_CHOICES, default='Erangel')
    entry = models.IntegerField(default=0)
    pay = models.CharField(max_length=30, blank=True)
    users = models.CharField(max_length=2000, blank=True)
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    GENDER_CHOICES = (('MALE','MALE'), ('FEMALE', 'FEMALE'),)
    phone = models.CharField(max_length=11, blank=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='MALE')
    match_played = models.IntegerField(default=0)
    total_kills = models.IntegerField(default=0)
    amount_won = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username
class FreePayUser(models.Model):
    matchid = models.IntegerField()
    users = models.CharField(max_length=30, blank=False)
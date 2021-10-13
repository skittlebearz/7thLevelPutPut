from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type= models.CharField(max_length=1)
    account_balance = models.DecimalField(decimal_places=2, max_digits=12)

class Score(models.Model):
    user = models.ManyToManyField(User)
    day = models.DateField()
    num_strokes = models.IntegerField()
    hole = models.IntegerField()
    
class Drink(models.Model):
    name = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.CharField(max_length=240)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


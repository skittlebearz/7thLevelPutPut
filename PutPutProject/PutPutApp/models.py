from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(decimal_places=2, max_digits=12, default=0)

    #def __str__(self):
    #    return str(self.user) + " - " + self.user_type
      
    # TODO: check for users with same name. Maybe unique=True?


    # allow users to be multiple types simultaneously
    player = models.BooleanField(default=True) # default user type
    barkeep = models.BooleanField(default=False) # admin approved by Manager
    sponsor = models.BooleanField(default=False) # admin approved by Manager
    manager = models.BooleanField(default=False) # a superuser


    def get_balance(self):
        return self.account_balance

    @property
    def is_player(self):
        return self.player

    @property
    def is_barkeep(self):
        return self.barkeep

    @property
    def is_sponsor(self):
        return self.sponsor

    @property
    def is_manager(self):
        return self.manager

class Score(models.Model):
    user = models.ManyToManyField(User)
    day = models.DateField()
    num_strokes = models.IntegerField()
    hole = models.IntegerField()
    par = models.IntegerField()
    def save(self, *args, **kwargs):
        self.par = int(self.num_strokes) - 3
        super(Score, self).save(*args, **kwargs)

class Drink(models.Model):
    name = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.CharField(max_length=240)

    def __str__(self):
        return self.name

class Orders(models.Model):
    name = models.CharField(max_length=30)
    drink = models.CharField(max_length=240)
    location = models.PositiveIntegerField()

class SponsorRequest(models.Model):
    #sponsor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    day = models.DateField()
    tournament_name = models.CharField(max_length=60)

class Calendar(models.Model):
    #sponsor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    day = models.DateField()
    tournament_name = models.CharField(max_length=60)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

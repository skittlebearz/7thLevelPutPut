from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type= models.CharField(max_length=1, default='P')
    account_balance = models.DecimalField(decimal_places=2, max_digits=12, default=0)

    def isManager(self):
        if self.user_type == 'M':
            return True
        return False

    def __str__(self):
        return str(self.user) + " - " + self.user_type
      
    # user_type= models.CharField(max_length=1)
    firstname = models.CharField(max_length=30, default='default')
    lastname = models.CharField(max_length=30, default='default')
    # TODO: check for users with same name. Maybe unique=True?
    # username = models.CharField(user_firstname + " " + user_lastname)

    UserTypes = models.TextChoices('User Type', 'Player Bartender Sponsor Manager')
    user_type = models.CharField(blank=True, choices=UserTypes.choices, max_length=30)

    # allow users to be multiple types simultaneously
    player = models.BooleanField(default=True) # default user type
    bartender = models.BooleanField(default=False) # admin approved by Manager
    sponsor = models.BooleanField(default=False) # admin approved by Manager
    manager = models.BooleanField(default=False) # a superuser

    account_balance = models.DecimalField(decimal_places=2, max_digits=12, default=0)

    def get_firstname(self):
        return self.firstname

    def get_balance(self):
        return self.account_balance

    @property
    def is_player(self):
        return self.player

    @property
    def is_bartender(self):
        return self.bartender

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

class Drink(models.Model):
    # TODO: get username from Profile
    name = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.CharField(max_length=240)

    def __str__(self):
        return self.name

class Orders(models.Model):
    # TODO: get username from Profile
    name = models.CharField(max_length=30)
    drink = models.CharField(max_length=240)
    location = models.PositiveIntegerField()

class Calandar(models.Model):
    sponsor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    day = models.DateField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

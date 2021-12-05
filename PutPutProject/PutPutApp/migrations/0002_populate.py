from django.db import migrations
from django.utils import timezone
import datetime


def populate_db(apps,schema_editor):
    Drink = apps.get_model('PutPutApp', 'Drink')
    Orders = apps.get_model('PutPutApp', 'Orders')
    SponsorRequest = apps.get_model('PutPutApp', 'SponsorRequest')
    Calendar = apps.get_model('PutPutApp', 'Calendar')
    Profile = apps.get_model('PutPutApp', 'Profile')
    User = apps.get_model('auth', 'User')


    #TEST USER ALL PERMISSIONS
    master_test_user = User.objects.create_user('testmaster', 'test@test.com', 'gotest123')
    master_test_user.first_name = 'testmaster'
    master_test_user.last_name = 'testman'
    master_test_user.save()

    master_testprofile = Profile.objects.create(
            user=master_test_user,
            account_balance=3,
            player=True,
            barkeep=True,
            sponsor=True,
            manager=True) 
    master_testprofile.save()


    #PLAYER TEST USER
    player_test_user = User.objects.create_user('playertest', 'test@test.com', 'gotest123')
    player_test_user.first_name = 'playertest'
    player_test_user.last_name = 'testman'
    player_test_user.save()

    player_testprofile = Profile.objects.create(
            user=player_test_user,
            account_balance=3,
            player=True,
            barkeep=False,
            sponsor=False,
            manager=False) 
    player_testprofile.save()


    #BARKEEP TEST USER
    barkeep_test_user = User.objects.create_user('barkeeptest', 'test@test.com', 'gotest123')
    barkeep_test_user.first_name = 'barkeeptest'
    barkeep_test_user.last_name = 'testman'
    barkeep_test_user.save()

    barkeep_testprofile = Profile.objects.create(
            user=barkeep_test_user,
            account_balance=3,
            player=True,
            barkeep=True,
            sponsor=False,
            manager=False) 
    barkeep_testprofile.save()

    #SPONSOR TEST USER
    sponsor_test_user = User.objects.create_user('sponsortest', 'test@test.com', 'gotest123')
    sponsor_test_user.first_name = 'sponsortest'
    sponsor_test_user.last_name = 'testman'
    sponsor_test_user.save()

    sponsor_testprofile = Profile.objects.create(
            user=sponsor_test_user,
            account_balance=3,
            player=True,
            barkeep=True,
            sponsor=True,
            manager=False) 
    sponsor_testprofile.save()

    #MANAGER TEST USER
    manager_test_user = User.objects.create_user('managertest', 'test@test.com', 'gotest123')
    manager_test_user.first_name = 'managertest'
    manager_test_user.last_name = 'testman'
    manager_test_user.save()

    manager_testprofile = Profile.objects.create(
            user=manager_test_user,
            account_balance=3,
            player=True,
            barkeep=True,
            sponsor=True,
            manager=True) 
    manager_testprofile.save()

    drink_a = Drink(
            name="Dirty Diet Coke",
            cost="2",
            description="Diet coke with a shot of coconut"
            )
    drink_a.save()

    drink_b = Drink(
            name="Hawaiian Mountain Dr",
            cost="2",
            description="Mtn dew + Dr Pepper + Coconut"
            )
    drink_b.save()

    drink_c = Drink(
            name="Hot Cocoa Delight",
            cost="2.5",
            description="Hot Cocoa with marshmallows, whipped cream, and cinnamon"
            )
    drink_c.save()

    drink_d = Drink(
            name="Diet Lime Ricky",
            cost="2.5",
            description="Diet sprite + grape + fresh limes"
            )
    drink_d.save()

    drink_e = Drink(
            name="Strawberry Lemonade",
            cost="2.85",
            description="Fresh lemonade with added real strawberrys"
            )
    drink_e.save()

    drink_f = Drink(
            name="Great Ginger Beer",
            cost="2",
            description="(Non-alchoholic) Ginger beer, locally brewed"
            )
    drink_f.save()

    drink_g = Drink(
        name="Honey Mead",
        cost="4.75",
        description="(Non-alchoholic) Sparkling water, honey, apple, and cinnamon"
    )
    drink_g.save()

    drink_h = Drink(
        name="Currant Melomel",
        cost="2.45",
        description="(Non-alchoholic) Black currant juice with honey and spices"
    )
    drink_h.save()

    drink_i = Drink(
        name="Aqua Vitae",
        cost="1.20",
        description="Sparkling water"
    )
    drink_i.save()




    order_a = Orders(
            name="Phil",
            drink="Hawaiian Mountain Dr",
            location="5"
            )
    order_a.save()


    order_b = Orders(
            name="Sara",
            drink="Dirty Diet Coke",
            location="9"
            )
    order_b.save()



    order_c = Orders(
            name="Jen",
            drink="Diet Lime Ricky",
            location="3"
            )
    order_c.save()



    order_d = Orders(
            name="Bryson",
            drink="Great Ginger Beer",
            location="12"
            )
    order_d.save()

    order_e = Orders(
            name="Ambrose",
            drink="Honey Mead",
            location="9"
            )
    order_e.save()

    order_f = Orders(
            name="Viola",
            drink="Currant Melomel",
            location="3"
            )
    order_f.save()


    sr_a = SponsorRequest(
            day=datetime.date(2021,11,20),
            tournament_name="USU tournament"
            )
    sr_a.save()


    sr_b = SponsorRequest(
            day=datetime.date(2021,12,15),
            tournament_name="Samsung tournament"
            )
    sr_b.save()


    sr_c = SponsorRequest(
            day=datetime.date(2022,1,10),
            tournament_name="Ford Cup"
            )
    sr_c.save()



    tournament_a = Calendar(
            day=datetime.date(2021,12,12),
            tournament_name="Nike Cup"
            )
    tournament_a.save()



    tournament_a = Calendar(
            day=datetime.date(2021,12,20),
            tournament_name="Walmart Tournament"
            )
    tournament_a.save()



    tournament_a = Calendar(
            day=datetime.date(2022,1,9),
            tournament_name="Campbell Soup Cup"
            )
    tournament_a.save()


    tournament_a = Calendar(
            day=datetime.date(2021,12,8),
            tournament_name="Apple tournament"
            )
    tournament_a.save()


    tournament_a = Calendar(
            day=datetime.date(2021,12,1),
            tournament_name="FedEx cup"
            )
    tournament_a.save()









class Migration(migrations.Migration):
    dependencies = [
        ('PutPutApp', '0001_initial'),
    ]

    operations = [
            migrations.RunPython(populate_db)
            ]

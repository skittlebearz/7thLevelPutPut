
from django.db import migrations
from django.utils import timezone
import datetime


def populate_db(apps,schema_editor):
    Drink = apps.get_model('PutPutApp', 'Drink')
    Orders = apps.get_model('PutPutApp', 'Orders')
    SponsorRequest = apps.get_model('PutPutApp', 'SponsorRequest')
    Calendar = apps.get_model('PutPutApp', 'Calendar')


    drink_a = Drink(
            name="Dirty Diet Coke",
            cost="2",
            description="Diet coke with a shot of cocunut"
            )
    drink_a.save()



    order_a = Orders(
            name="Phil",
            drink="Dirty Diet Coke",
            location="9"
            )
    order_a.save()



    sr_a = SponsorRequest(
            day=datetime.date(2021,11,20),
            tournament_name="USU tournament"
            )
    sr_a.save()




    tournament_a = Calendar(
            day=datetime.date(2021,12,12),
            tournament_name="Nike Cup"
            )
    tournament_a.save()






class Migration(migrations.Migration):
    dependencies = [
        ('PutPutApp', '0001_initial'),
    ]

    operations = [
            migrations.RunPython(populate_db)
            ]

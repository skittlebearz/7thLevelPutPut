# Generated by Django 3.2.7 on 2021-10-13 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PutPutApp', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calandar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PutPutApp.profile')),
            ],
        ),
    ]
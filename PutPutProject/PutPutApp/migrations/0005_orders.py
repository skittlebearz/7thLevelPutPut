# Generated by Django 3.2.8 on 2021-11-08 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PutPutApp', '0004_alter_profile_account_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('drink', models.CharField(max_length=240)),
                ('location', models.PositiveIntegerField()),
            ],
        ),
    ]
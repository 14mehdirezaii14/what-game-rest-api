# Generated by Django 4.1.3 on 2022-12-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatGame', '0009_ticket_namegame'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.TextField(default=100, max_length=140),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatGame', '0002_alter_ticket_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='email',
            field=models.TextField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name='ticket',
            name='name',
            field=models.TextField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name='ticket',
            name='numberOfPersons',
            field=models.TextField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name='ticket',
            name='phone',
            field=models.TextField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name='ticket',
            name='watch',
            field=models.TextField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.TextField(blank=True, max_length=140),
        ),
    ]

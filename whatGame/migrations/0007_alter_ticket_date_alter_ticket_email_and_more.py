# Generated by Django 4.1.3 on 2022-12-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatGame', '0006_rename_watch_ticket_timee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.TextField(default='', max_length=140),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='email',
            field=models.TextField(default='', max_length=140),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='lastName',
            field=models.TextField(default='', max_length=140),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='name',
            field=models.TextField(default='', max_length=140),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='numberOfPersons',
            field=models.TextField(default='', max_length=140),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='phone',
            field=models.TextField(default='', max_length=140),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='timee',
            field=models.TextField(default='', max_length=140),
        ),
    ]
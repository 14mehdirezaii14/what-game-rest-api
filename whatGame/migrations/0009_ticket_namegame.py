# Generated by Django 4.1.3 on 2022-12-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatGame', '0008_alter_ticket_date_alter_ticket_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='nameGame',
            field=models.TextField(default=1, max_length=140),
            preserve_default=False,
        ),
    ]

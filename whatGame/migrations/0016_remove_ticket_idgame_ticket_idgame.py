# Generated by Django 4.1.3 on 2022-12-26 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whatGame', '0015_ticket_idgame'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='idGame',
        ),
        migrations.AddField(
            model_name='ticket',
            name='idGame',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='whatGame.escaperoom'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-26 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whatGame', '0016_remove_ticket_idgame_ticket_idgame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='idGame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whatGame.escaperoom'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-25 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatGame', '0012_alter_escaperoom_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='escaperoom',
            old_name='src',
            new_name='img',
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-25 11:22

from django.db import migrations, models
import whatGame.models


class Migration(migrations.Migration):

    dependencies = [
        ('whatGame', '0010_ticket_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='EscapeRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.TextField(max_length=30)),
                ('name', models.CharField(max_length=300)),
                ('timee', models.CharField(max_length=30)),
                ('capacity', models.CharField(max_length=30)),
                ('degreeOfDifficulty', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('scenario', models.TextField(max_length=540)),
                ('gameTips', models.TextField(max_length=540)),
                ('viewMoreGameTips', models.TextField(max_length=540)),
                ('src', models.ImageField(blank=True, null=True, upload_to=whatGame.models.upload_to)),
            ],
        ),
    ]

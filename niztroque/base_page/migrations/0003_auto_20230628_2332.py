# Generated by Django 3.1.2 on 2023-06-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0002_remove_event_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='adress',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='event',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='link',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.CharField(default='', max_length=100),
        ),
    ]

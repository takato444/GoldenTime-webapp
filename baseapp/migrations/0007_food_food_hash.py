# Generated by Django 4.2.6 on 2023-12-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0006_food_hit_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='food_hash',
            field=models.CharField(default='0', max_length=64),
        ),
    ]
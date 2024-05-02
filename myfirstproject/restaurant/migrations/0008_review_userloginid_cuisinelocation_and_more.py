# Generated by Django 5.0.1 on 2024-04-18 01:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_cuisine_tag_remove_location_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='userLoginID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.userlogin'),
        ),
        migrations.CreateModel(
            name='CuisineLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisineID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.cuisine')),
                ('locationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.location')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHoursLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.location')),
                ('openingHoursID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.openinghours')),
            ],
        ),
    ]

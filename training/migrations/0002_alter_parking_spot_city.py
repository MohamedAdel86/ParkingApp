# Generated by Django 4.1.7 on 2023-05-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking_spot',
            name='city',
            field=models.CharField(max_length=52),
        ),
    ]
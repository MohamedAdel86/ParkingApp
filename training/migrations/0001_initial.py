# Generated by Django 4.1.7 on 2023-05-05 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomin_sd', models.DateTimeField(max_length=30, null=True)),
                ('nomin_ed', models.DateTimeField(max_length=30, null=True)),
                ('vote_sd', models.DateTimeField(max_length=30, null=True)),
                ('vote_ed', models.DateTimeField(max_length=30, null=True)),
                ('con_sd', models.DateTimeField(max_length=30, null=True)),
                ('con_ed', models.DateTimeField(max_length=30, null=True)),
                ('nominations_period_id', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parking_spot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('parkingphoto', models.FileField(max_length=254, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('phone_no', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('birthdate', models.DateField(null=True)),
                ('reservation_status', models.BooleanField(default=False)),
                ('Userkey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.parking_spot')),
                ('worker_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='training.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(max_length=30, null=True)),
                ('price', models.IntegerField(max_length=10)),
                ('User_Model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_to_foreign_key_2', to='training.user_model')),
                ('parking_spot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_to_foreign_key_1', to='training.parking_spot')),
            ],
        ),
        migrations.CreateModel(
            name='Contention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('nominee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.worker')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.user_model')),
            ],
        ),
        migrations.CreateModel(
            name='Admin_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Userkey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

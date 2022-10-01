# Generated by Django 3.2.15 on 2022-09-29 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='One_Off_Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingID', models.CharField(max_length=20)),
                ('bookdate', models.DateField(auto_now_add=True)),
                ('starttime', models.TimeField(auto_now=True)),
                ('duration', models.IntegerField()),
                ('owntool', models.BooleanField(default=False)),
                ('feelist', models.CharField(max_length=20)),
            ],
        ),
    ]
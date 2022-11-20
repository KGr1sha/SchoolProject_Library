# Generated by Django 4.1.3 on 2022-11-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('class_number', models.IntegerField(choices=[(7, 7), (8, 8), (9, 9), (10, 10), (11, 11)])),
            ],
        ),
    ]

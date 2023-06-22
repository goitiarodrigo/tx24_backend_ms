# Generated by Django 4.2.2 on 2023-06-19 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto_Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.URLField(max_length=300)),
                ('abbreviation', models.TextField(max_length=15)),
                ('old_price', models.FloatField()),
                ('current_price', models.FloatField()),
                ('preivous_day_price', models.FloatField()),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-03 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooked', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='price',
            field=models.IntegerField(default=9.99),
            preserve_default=False,
        ),
    ]
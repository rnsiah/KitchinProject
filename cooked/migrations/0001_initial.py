# Generated by Django 3.0.8 on 2020-08-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_name', models.CharField(max_length=50, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('vendor_email', models.EmailField(max_length=254, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('review', models.CharField(blank=True, max_length=100, null=True)),
                ('image_url', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-01 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('massage', models.TextField()),
                ('created_date', models.DateTimeField()),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-18 13:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='Phone Numbers Must Start With 01 & all Are Numbers', regex='^01\\d{9}')])),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numbers', to='contact.contact')),
            ],
        ),
    ]

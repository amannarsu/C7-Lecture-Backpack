# Generated by Django 5.0.6 on 2024-05-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='registration_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="stripe_token",
            field=models.CharField(max_length=200),
        ),
    ]

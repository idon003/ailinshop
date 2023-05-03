# Generated by Django 4.2 on 2023-05-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0004_alter_drink_drink_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='drink',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

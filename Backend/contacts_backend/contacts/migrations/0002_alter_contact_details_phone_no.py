# Generated by Django 4.2.2 on 2023-07-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_details',
            name='phone_no',
            field=models.BigIntegerField(),
        ),
    ]

# Generated by Django 3.2.1 on 2021-05-06 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0002_auto_20210505_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-28 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rickmorty', '0004_auto_20200328_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='characters',
            field=models.CharField(default='frodo', max_length=200),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.12 on 2022-03-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardening', '0008_auto_20220304_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='seed',
            name='provider',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='seed',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-31 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_carinventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

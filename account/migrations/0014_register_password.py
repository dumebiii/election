# Generated by Django 3.2.9 on 2021-11-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_register_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

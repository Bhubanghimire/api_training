# Generated by Django 4.0.2 on 2024-07-12 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_user_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserType',
        ),
    ]

# Generated by Django 4.2 on 2023-05-02 12:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0003_item_image'),
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Converation',
            new_name='Conversation',
        ),
    ]

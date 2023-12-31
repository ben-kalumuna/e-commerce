# Generated by Django 4.2 on 2023-05-16 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('prof_image', models.ImageField(blank=True, null=True, upload_to='profile_images')),
                ('degree', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('product_selling', models.CharField(max_length=500)),
                ('decription', models.TextField()),
            ],
        ),
    ]

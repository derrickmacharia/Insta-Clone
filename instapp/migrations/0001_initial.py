# Generated by Django 2.0 on 2021-12-02 15:41

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('title', models.CharField(max_length=50)),
                ('caption', models.TextField(max_length=1500)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]

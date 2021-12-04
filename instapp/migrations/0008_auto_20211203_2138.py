# Generated by Django 3.2.9 on 2021-12-03 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instapp', '0007_auto_20211203_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_caption',
            new_name='caption',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='image',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_date',
        ),
        migrations.RemoveField(
            model_name='image',
            name='like_count',
        ),
        migrations.AddField(
            model_name='image',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

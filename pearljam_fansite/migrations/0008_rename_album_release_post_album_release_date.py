# Generated by Django 3.2.15 on 2022-08-24 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pearljam_fansite', '0007_post_album_release'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='album_release',
            new_name='album_release_date',
        ),
    ]

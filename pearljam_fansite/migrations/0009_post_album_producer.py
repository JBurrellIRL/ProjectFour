# Generated by Django 3.2.15 on 2022-08-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pearljam_fansite', '0008_rename_album_release_post_album_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='album_producer',
            field=models.TextField(blank=True),
        ),
    ]

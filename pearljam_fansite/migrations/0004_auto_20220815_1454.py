# Generated by Django 3.2.15 on 2022-08-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pearljam_fansite', '0003_rename_post_albumreview'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.AlterField(
            model_name='albumreview',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

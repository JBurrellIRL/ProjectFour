# Generated by Django 3.2.15 on 2022-08-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pearljam_fansite', '0005_rename_albumreview_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
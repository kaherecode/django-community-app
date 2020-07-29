# Generated by Django 3.0.8 on 2020-07-29 16:47

from django.db import migrations, models
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20200729_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=members.models.upload_picture),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-24 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_rename_image_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='emotion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
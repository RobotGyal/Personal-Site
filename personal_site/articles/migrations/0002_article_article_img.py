# Generated by Django 3.0 on 2020-03-11 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_img',
            field=models.ImageField(default=None, upload_to='pics/'),
        ),
    ]

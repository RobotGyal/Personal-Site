# Generated by Django 3.0 on 2020-03-13 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webiste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='pics/')),
                ('live_url', models.URLField()),
                ('repo_url', models.URLField()),
                ('summary', models.TextField()),
                ('created_on', models.DateTimeField()),
                ('built_with', models.TextField()),
            ],
        ),
    ]

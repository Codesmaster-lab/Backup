# Generated by Django 3.0.1 on 2020-02-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0003_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]

# Generated by Django 2.2 on 2021-06-24 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0023_auto_20210624_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecollect',
            name='unique_iden',
            field=models.TextField(default='null', unique=True, verbose_name='唯一标识'),
        ),
    ]

# Generated by Django 2.2 on 2020-11-27 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0005_auto_20201128_0143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',), 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
    ]
# Generated by Django 2.2 on 2020-11-26 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.ArticlePost', verbose_name='文章'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]

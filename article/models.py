from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import User
# reserse() 反向解析 URL 地址
from django.urls import reverse
# timezone 用于处理时间相关事务。
from django.utils import timezone


# Create your models here.
class ArticleColumn(models.Model):
    """
    文章栏目的 Model
    """
    # 栏目标题
    title = models.CharField('栏目名称', max_length=100, blank=True)
    # 创建时间
    created = models.DateTimeField('创建时间', default=timezone.now)

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # '-created' 表明数据应该以创建时间倒序排列
        # ordering = ('-created', )
        # 定义 Model在数据库中的表名，默认为 app名_模型名
        db_table = "tb_column"
        verbose_name = '栏目'  # 管理后台中显示的模型名
        verbose_name_plural = verbose_name  # 管理后台中显示的模型名复数形式

    def __str__(self):
        return self.title


class ArticlePost(models.Model):
    """ 博客文章数据模型 """
    # 文章作者。参数 on_delete 用于指定数据删除的方式（级联删除）
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='作者')
    # 文章标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField('标题', max_length=100)
    # 文章正文。保存大量文本使用 TextField
    body = models.TextField('正文')
    # 文章创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField('创建时间', default=timezone.now)
    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间（不可编辑字段）
    updated = models.DateTimeField('更新时间', auto_now=True)
    # 文章浏览量，PositiveIntegerField是用于存储正整数的字段
    total_views = models.PositiveIntegerField('浏览量', default=0)
    # 文章栏目的 “一对多” 外键
    column = models.ForeignKey(ArticleColumn,
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE,
                               related_name='article',
                               verbose_name='栏目')

    # 获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以创建时间倒序排列
        ordering = ('-created', )
        # 定义 Model在数据库中的表名，默认为 app名_模型名
        db_table = "tb_article"
        verbose_name = '文章'  # 管理后台中显示的模型名
        verbose_name_plural = verbose_name  # 管理后台中显示的模型名复数形式

    def __str__(self):
        # 将文章标题返回
        return self.title

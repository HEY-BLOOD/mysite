from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import User
# reserse() 反向解析 URL 地址
from django.urls import reverse
# timezone 用于处理时间相关事务。
from django.utils import timezone
# Django-taggit 标签功能模块
from taggit.managers import TaggableManager
# 图像处理
from PIL import Image
# 引入imagekit，处理图片
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


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
    # 文章标签，多对多关系
    tags = TaggableManager(verbose_name='标签', help_text="如：文学,诗歌,青春", blank=True)
    # 文章标题图，使用 django-imagekit，不用自己在save方法中处理图片了
    avatar = ProcessedImageField(
        upload_to='article/%Y%m%d',  # 上传路径（如：media/article/20190226/）
        processors=[ResizeToFit(width=400)],  # 处理规则
        format='JPEG',  # 存储格式
        options={'quality': 100},  # 图片质量
        null=True,
        blank=True,
    )
    # 点赞数统计
    likes = models.PositiveIntegerField('点赞数', default=0)

    # 获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])

    # def save(self, *args, **kwargs):
    #     """  model实例每次保存时调用，保存时处理文章标题图  """
    #     # 调用原有的 save() 的功能，将model中的字段数据保存到数据库中。因为图片处理是基于已经保存的图片的，
    #     article = super(ArticlePost, self).save(*args, **kwargs)

    #     # 固定宽度缩放图片大小
    #     if self.avatar and not kwargs.get('update_fields'):
    #         image = Image.open(self.avatar)
    #         (x, y) = image.size
    #         if x > 400:
    #             new_x = 400
    #             new_y = int(new_x * (y / x))
    #             resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
    #             resized_image.save(self.avatar.path)

    #     return article

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

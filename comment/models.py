from django.db import models
from django.contrib.auth.models import User

from article.models import ArticlePost

# django-ckeditor 富文本编辑器
from ckeditor.fields import RichTextField
# django-mptt 多级评论扩展
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Comment(MPTTModel):
    """
    博文的评论，继承自 django-mptt的 MPTTModel
    """
    # 被评论的博文，由于一篇文章可以有很多评论，所以是一对多的外键关系
    article = models.ForeignKey(ArticlePost,
                                on_delete=models.CASCADE,
                                related_name='comments',
                                verbose_name='文章')
    # 评论的发布者，任何登录的用户都可以进行评论，
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='用户')
    # 评论内容，改为使用富文本编辑器
    # body = models.TextField('评论内容')
    body = RichTextField('评论内容')
    created = models.DateTimeField('评论时间', auto_now_add=True)
    # 新增，mptt树形结构
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )
    # 新增，记录二级评论回复给谁, str
    reply_to = models.ForeignKey(User,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE,
                                 related_name='replyers',
                                 verbose_name='用户')

    # 替换 Meta 为 MPTTMeta
    class MPTTMeta:
        order_insertion_by = ['-created']  # 降序排列
        # 原 Meta的元数据
        # db_table = "tb_comment"
        # verbose_name = '评论'  # 管理后台中显示的模型名
        # verbose_name_plural = verbose_name  # 管理后台中显示的模型名复数形式

    def __str__(self):
        return self.body[:20]

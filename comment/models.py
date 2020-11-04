from django.db import models
from django.contrib.auth.models import User
from article.models import ArticlePost


# Create your models here.
class Comment(models.Model):
    """
    博文的评论
    """
    # 被评论的博文，由于一篇文章可以有很多评论，所以是一对多的外键关系
    article = models.ForeignKey(ArticlePost, on_delete=models.CASCADE, related_name='comments')
    # 评论的发布者，任何登录的用户都可以进行评论，
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    # 评论内容
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return self.body[:20]

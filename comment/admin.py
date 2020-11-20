from django.contrib import admin
from .models import Comment


# 自定义模型管理类
class CommentAdmin(admin.ModelAdmin):
    """  ArticlePost 博客文章后台管理模型  """

    # 表格显示的字段
    list_display = ['article', 'body', 'user', 'created']

    # 表单字段，不要包含不可编辑的字段（如：auto_now_add=True的 created字段）
    fields = ['user', 'article', 'body']


# Register your models here.
admin.site.register(Comment, CommentAdmin)

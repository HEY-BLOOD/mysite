from django.contrib import admin
from .models import ArticlePost


# 自定义模型管理类
class ArticlePostAdmin(admin.ModelAdmin):
    """  ArticlePost 博客文章后台管理模型  """

    # 表格显示的字段
    list_display = ['title', 'total_views', 'created', 'updated']

    # 表单字段，不要包含不可编辑的字段（如：auto_now=True的 updated字段）
    fields = ['author', 'title', 'body']


# Register your models here.
admin.site.register(ArticlePost, ArticlePostAdmin)

from django.contrib import admin
from .models import ArticlePost, ArticleColumn


# 自定义模型管理类
class ArticlePostAdmin(admin.ModelAdmin):
    """  ArticlePost 博客文章后台管理模型  """
    # 添加栏目字段的显示

    # 表格显示的字段
    list_display = [
        'title', 'column', 'tags', 'total_views', 'likes', 'created', 'updated'
    ]

    # 表单字段，不要包含不可编辑的字段（如：auto_now=True的 updated字段）
    fields = ['avatar', 'author', 'title', 'column', 'tags', 'body']


class ArticleColumnAdmin(admin.ModelAdmin):
    """  文章栏目（分类）模型管理   """
    list_display = ['title', 'created']

    fields = []  # 默认全部


# Register your models here.
admin.site.register(ArticlePost, ArticlePostAdmin)
admin.site.register(ArticleColumn, ArticleColumnAdmin)

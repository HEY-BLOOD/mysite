from django.contrib import admin
from .models import ArticlePost, ArticleColumn, ArticleCollect


# Register your models here.
@admin.register(ArticlePost)
class ArticlePostAdmin(admin.ModelAdmin):
    """  ArticlePost 博客文章后台管理模型  """
    # 表格显示的字段
    list_display = ['title', 'column', 'tags', 'total_views', 'likes', 'created', 'updated']
    # 表单字段，不要包含不可编辑的字段（如：auto_now=True的 updated字段）
    fields = ['avatar', 'author', 'title', 'column', 'tags', 'body']
    # 每页显示个数
    list_per_page = 20


@admin.register(ArticleColumn)
class ArticleColumnAdmin(admin.ModelAdmin):
    """  文章栏目（分类）模型管理   """
    list_display = ['title', 'created']
    fields = []  # 默认全部
    list_per_page = 20


@admin.register(ArticleCollect)
class ArticleCollectAdmin(admin.ModelAdmin):
    # 表格显示的字段
    list_display = ['article', 'user', 'collected_time']
    list_per_page = 20

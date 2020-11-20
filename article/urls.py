from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    # path函数将url映射到视图
    path('', views.article_list, name='article_list'),
    path('article-list/', views.article_list, name='article_list'),
    # 文章详情，Django2.0的 path新语法用尖括号<>定义需要传递的参数。
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    # 写文章
    # path('article-create/', views.article_create, name='article_create'),

    # 删除文章
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    # 安全删除文章
    path('article-safe-delete/<int:id>/',
         views.article_safe_delete,
         name='article_safe_delete'),
    # 更新文章
    path('article-update/<int:id>/', views.article_update, name='article_update'),

    # 列表类视图，TODO 未实现分页
    #     path('', views.ArticleListView.as_view(), name='article_list'),
    #     path('article-list/', views.ArticleListView.as_view(), name='article_list'),
    # 详情类视图，TODO 不能显示文章的评论
    #     path('article-detail/<int:pk>/',
    #          views.ArticleDetailView.as_view(),
    #          name='article_detail'),
    # 创建类视图
    path('article-create/', views.ArticleCreateView.as_view(), name='article_create'),
]

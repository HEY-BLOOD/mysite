from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
    # 文章详情，Django2.0的 path新语法用尖括号<>定义需要传递的参数。
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
]

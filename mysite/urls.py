"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# django-notifications-hq 消息通知扩展的路由
import notifications.urls

admin.site.site_title = '管理后台'
admin.site.site_header = '系统管理后台'

urlpatterns = [
    path('admin/', admin.site.urls),
    # 配置 article 应用的分发路由，只能二选一，否则生成数据库迁移文件时会提示 “URL namespace 'article' isn't unique.”
    path('', include('article.urls', namespace='article')),
    # path('article/', include('article.urls', namespace='article')),
    # 用户管理
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    # 密码重置
    path('password-reset/', include('password_reset.urls')),
    # 评论
    path('comment/', include('comment.urls', namespace='comment')),
    # django-notifications-hq 消息通知扩展的路由
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    # notice 消息通知的未读与已读
    path('notice/', include('notice.urls', namespace='notice')),
    # django-allauth 用户登录
    path('accounts/', include('allauth.urls')),
    # django-mdeditor 编辑器
    path('mdeditor/', include('mdeditor.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

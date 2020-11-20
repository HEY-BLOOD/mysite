from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


# Register your models here.
class ProfileInline(admin.StackedInline):
    """ 定义一个行内 admin，可以被内嵌到其它 Admin """
    model = Profile
    can_delete = False
    verbose_name = '扩展信息'
    verbose_name_plural = '扩展信息'


# 将 Profile 关联到 User 中
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )


# 重新注册 User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

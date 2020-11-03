from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    """ 登录表单，继承自 forms.Form 类 """
    username = forms.CharField()
    password = forms.CharField()

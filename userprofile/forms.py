from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserLoginForm(forms.Form):
    """ 登录表单，继承自 forms.Form 类 """
    username = forms.CharField()
    password = forms.CharField()


class UserRegisterForm(forms.ModelForm):
    """ 注册用户表单 """
    # 复写 User 的密码
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    # def clean_[字段]这种写法Django会自动调用，来对单个字段的数据进行验证清洗。
    def clean_password2(self):
        """ 对两次输入的密码是否一致进行检查 """
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致,请重试。")


class ProfileForm(forms.ModelForm):
    """ 用户扩展信息表单 """
    class Meta:
        model = Profile
        fields = ('phone', 'avatar', 'bio')

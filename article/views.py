from django.shortcuts import render
# 导入 HttpResponse 模块
from django.http import HttpResponse


# Create your views here.
# 视图函数
def article_list(request):
    return HttpResponse("Hello World!")

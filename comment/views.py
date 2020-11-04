from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

from article.models import ArticlePost
from .forms import CommentForm


# Create your views here.
@login_required(login_url='/userprofile/login/')
def post_comment(request, article_id):
    """ 发布评论 """
    article = get_object_or_404(ArticlePost, id=article_id)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # 暂时保持不提交到数据库
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            # 重定向 URL，自动调用这个Model对象的get_absolute_url()方法
            return redirect(article)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")

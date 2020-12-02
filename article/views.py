from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# 引入分页模块
from django.core.paginator import Paginator
# 引入 Q 对象，用于同时对模型多个字段进行搜索
from django.db.models import Q
# 通用类视图
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
# 消息闪现模块
from django.contrib import messages
from .models import ArticlePost, ArticleColumn
from comment.models import Comment
from .forms import ArticlePostForm
from comment.forms import CommentForm
import markdown


# Create your views here.
class ContextMixin(View):
    """
    Mixin
    """
    def get_context_data(self, **kwargs):
        # 获取原有的上下文
        context = super().get_context_data(**kwargs)
        # 增加新上下文
        context['order'] = 'total_views'

        return context


class ArticleListView(ContextMixin, ListView):
    """
    文章列表类视图
    """
    # 查询集的名称（上下文的名称）
    context_object_name = 'articles'
    # 查询集
    # queryset = ArticlePost.objects.all()
    # 模板位置
    template_name = 'article/list.html'

    # def get_queryset(self):
    #     """
    #     查询集
    #     """
    #     queryset = ArticlePost.objects.filter(title='Python')
    #     return queryset

    def get_queryset(self):
        # 获取请求中的搜索关键字和排序参数
        search = self.request.GET.get('search')
        order = self.request.GET.get('order')
        # 用户搜索逻辑
        if search:
            if order == 'total_views':
                # 用 Q对象对所有文章的标题和内容进行联合搜索；icontains不区分大小写，对应的contains区分大小写
                article_list = ArticlePost.objects.filter(Q(title__contains=search)
                                                          | Q(body__contains=search)).order_by('-total_views')
            else:
                article_list = ArticlePost.objects.filter(Q(title__contains=search) | Q(body__contains=search))
        else:
            # 将 search 参数重置为空，因为 search参数为空的时值为 None，传递到模板中会错误地转换成"None"字符串
            search = ''
            if order == 'total_views':
                article_list = ArticlePost.objects.all().order_by('-total_views')
            else:
                article_list = ArticlePost.objects.all()

        return article_list


def article_list(request):
    """ 文章列表 """
    # 从 url 中提取查询参数
    search = request.GET.get('search')  # 标题和正文查询关键字
    order = request.GET.get('order')  # 排序
    column = request.GET.get('column')  # 栏目、类别
    tag = request.GET.get('tag')  # 标签

    # 初始化查询集
    article_list = ArticlePost.objects.all()

    # 搜索查询集
    if search:
        article_list = article_list.filter(Q(title__icontains=search) | Q(body__icontains=search))
    else:
        search = ''

    # 栏目查询集
    if column is not None and column.isdigit():
        article_list = article_list.filter(column=column)

    # 标签查询集；
    # 注意Django-taggit中标签过滤的写法：filter(tags__name__in=[tag])，意思是在tags字段中过滤name为tag的数据条目。赋值的字符串tag用方括号包起来。
    # 之所以这样写是因为Django-taggit还支持多标签的联合查询，比如：Model.objects.filter(tags__name__in=["tag1", "tag2"])
    if tag and tag != 'None':
        article_list = article_list.filter(tags__name__in=[tag])

    # 查询集排序
    if order == 'total_views':
        article_list = article_list.order_by('-total_views')

    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    # 需要传递给模板（templates）的对象
    context = {
        'articles': articles,
        'articles_length': len(article_list),
        'order': order,
        'search': search,
        'column': column,
        'tag': tag,
    }

    return render(request, 'article/list.html', context)


class ArticleDetailView(DetailView):
    """
    文章详情类视图
    """
    queryset = ArticlePost.objects.all()
    context_object_name = 'article'
    template_name = 'article/detail.html'

    def get_object(self):
        """
        获取需要展示的对象
        """
        # 首先调用父类的方法
        obj = super(ArticleDetailView, self).get_object()
        # 浏览量 +1
        obj.total_views += 1
        # 提交更改
        obj.save(update_fields=['total_views'])
        return obj


def article_detail(request, id):
    """ 文章详情 """
    # 取出相应的文章
    # article = ArticlePost.objects.get(id=id)
    # logger.warning('Something went wrong!')
    article = get_object_or_404(ArticlePost, id=id)

    # 取出文章评论
    comments = Comment.objects.filter(article=id)

    # 浏览量 +1
    article.total_views += 1
    article.save(update_fields=['total_views'])

    # 相邻发表文章的快捷导航
    pre_article = ArticlePost.objects.filter(id__lt=article.id).order_by('-id')
    next_article = ArticlePost.objects.filter(id__gt=article.id).order_by('id')
    if pre_article.count() > 0:
        pre_article = pre_article[0]
    else:
        pre_article = None

    if next_article.count() > 0:
        next_article = next_article[0]
    else:
        next_article = None

    # Markdown 语法渲染
    md = markdown.Markdown(extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        # 目录扩展
        'markdown.extensions.toc',
    ])
    article.body = md.convert(article.body)

    # 为评论引入表单
    comment_form = CommentForm()

    # 需要传递给模板的对象
    context = {
        'article': article,
        'toc': md.toc,
        'comments': comments,
        'pre_article': pre_article,
        'next_article': next_article,
        'comment_form': comment_form,
    }
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)

    # 创建含有扩展的 Markdown实例；之前是 markdown，现在改为 Markdown
    md = markdown.Markdown(extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        # 目录扩展
        'markdown.extensions.toc',
    ])
    # 将正文渲染为 html文本
    article.body = md.convert(article.body)
    # 引入评论表单
    comment_form = CommentForm()
    # 模板上下文；文章、正文目录、文章评论
    context = {
        'article': article,
        'toc': md.toc,
        'comments': comments,
        'comment_form': comment_form,
    }
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)


class ArticleCreateView(CreateView):
    """
    创建文章的类视图
    """
    model = ArticlePost
    fields = '__all__'
    # 或者有选择的提交字段，比如：
    # fields = ['title']
    template_name = 'article/create.html'


@login_required(login_url='/userprofile/login/')
def article_create(request):
    """ 添加文章 """
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中，增加 request.FILES
        article_post_form = ArticlePostForm(request.POST, request.FILES)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_article.author = User.objects.get(id=request.user.id)
            # 新增的代码
            if request.POST['column'] != 'none':
                new_article.column = ArticleColumn.objects.get(id=request.POST['column'])
            # 将新文章保存到数据库中
            new_article.save()
            # 新增代码，保存文章标签 tags 的多对多关系
            article_post_form.save_m2m()
            messages.warning(request, "文章发表成功！")
            # 完成后返回到新发布的文章页面，反向解析 URL地址
            return redirect(new_article.get_absolute_url())
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # GET，如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 返回模板，新增文章栏目上下文
        columns = ArticleColumn.objects.all()
        context = {'article_post_form': article_post_form, 'columns': columns}

        return render(request, 'article/create.html', context)


@login_required(login_url='/userprofile/login/')
def article_delete(request, id):
    """ 删除文章 """
    # 根据 id（主键）获取需要删除的文章
    article = ArticlePost.objects.get(id=id)
    # 过滤已登录、但非文章作者的用户
    if request.user != article.author:
        return HttpResponse("抱歉，你无权修改这篇文章。")
    # 调用.delete()方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    return redirect("article:article_list")


@login_required(login_url='/userprofile/login/')
def article_safe_delete(request, id):
    """ 安全删除文章 """
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许post请求")


@login_required(login_url='/userprofile/login/')
def article_update(request, id):
    """
    更新文章的视图函数
    通过POST方法提交表单，更新title、body字段
    GET方法进入初始表单页面
    id： 文章的 id
    """
    # 获取需要修改的具体文章对象
    article = ArticlePost.objects.get(id=id)

    # 过滤已登录、但非文章作者的用户
    if request.user != article.author:
        return HttpResponse("抱歉，你无权修改这篇文章。")

    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 文章标题图
            if request.FILES.get('avatar'):
                article.avatar = request.FILES.get('avatar')
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            # 新增栏目验证的代码
            if request.POST['column'] != 'none':
                article.column = ArticleColumn.objects.get(id=request.POST['column'])
            else:
                article.column = None
            # 标签
            article.tags.set(*request.POST.get('tags').split(','), clear=True)
            article.save()
            
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            messages.warning(request, "文章修改成功！")
            return redirect("article:article_detail", id=id)
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文， 当前文章、栏目、标签，修改前的展示
        columns = ArticleColumn.objects.all()
        context = {
            'article': article,
            'article_post_form': article_post_form,
            'columns': columns,
            'tags': ','.join([x for x in article.tags.names()]),
        }
        # 将响应返回到模板中
        return render(request, 'article/update.html', context)


class IncreaseLikesView(View):
    """  文章点赞  """
    def post(self, request, *args, **kwargs):
        article = ArticlePost.objects.get(id=kwargs.get('id'))
        article.likes += 1
        article.save()
        return HttpResponse('success')

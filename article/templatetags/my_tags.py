from .register import register

import datetime


# simple_tag就是最重要的标签类型。标签的注册方法跟过滤器非常类似：
@register.simple_tag
def change_http_to_https(url):
    """  将http链接替换为https链接。  """
    new_url = url.replace('http://', 'https://')
    return new_url


@register.simple_tag
def current_time(format_string):
    """ 返回指定格式的时间字符串：
    {% current_time "%Y-%m-%d %I:%M %p" as the_time %}
    <p>The time is {{ the_time }}.</p>
    <p>Again, the time is {{ the_time }}.</p>
    """
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    """  注册标签时传入takes_context参数: 使模板标签能够访问当前的上下文 """
    timezone = context['timezone']
    return current_time(timezone, format_string)


@register.simple_tag
def my_tag(a, b, *args, **kwargs):
    """  与过滤器不同的是，标签可以接受任意数量的位置或关键字参数。  """
    warning = kwargs['warning']
    profile = kwargs['profile']
    '...'
    return '...'


# 包含标签
@register.inclusion_tag('article/_tags/comments_created.html')
def show_comments_pub_time(article):
    """显示文章评论的发布时间"""
    comments = article.comments.all()
    return {'comments': comments}

from .register import register

from django.utils import timezone
from django.utils.html import strip_tags  # 去除HTML标签

import markdown
import math


@register.filter(name='time_since_zh')
def time_since_zh(value):
    """ 获取文章发布相对时间 """
    now = timezone.now()
    diff = now - value

    if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
        return '刚刚'

    if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
        return str(math.floor(diff.seconds / 60)) + "分钟前"

    if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
        return str(math.floor(diff.seconds / 3600)) + "小时前"

    if diff.days >= 1 and diff.days < 30:
        return str(diff.days) + "天前"

    if diff.days >= 30 and diff.days < 365:
        return str(math.floor(diff.days / 30)) + "个月前"

    if diff.days >= 365:
        return str(math.floor(diff.days / 365)) + "年前"


@register.filter(name='to_abstract')
def to_abstract(body):
    """
    根据正文生成文章摘要
    """
    # 首先实例化一个 Markdown 类，用于渲染 body 的文本。
    # 由于摘要并不需要生成文章目录，所以去掉了目录拓展。
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
    ])

    # 先将 Markdown 文本渲染成 HTML 文本
    # strip_tags 去掉 HTML 文本的全部 HTML 标签
    # 从文本摘取前 100 个字符赋给 excerpt
    excerpt = strip_tags(md.convert(body))[:130] + '…………'

    return excerpt

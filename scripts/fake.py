import os
import sys

import django
import faker
from django.utils import timezone

# 将项目根目录添加到 Python 的模块搜索路径中
back = os.path.dirname
BASE_DIR = back(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()  # 启动django

    from article.models import ArticlePost
    from django.contrib.auth.models import User

    print('clean database')
    ArticlePost.objects.all().delete()
    User.objects.all().delete()

    print('create a superuser')
    user = User.objects.create_superuser('admin', '', 'admin')

    print('create some faked posts published within the past year')
    fake = faker.Faker()  # English
    for _ in range(100):
        created = fake.date_time_between(  # 返回 2 个指定日期间的随机日期。三个参数分别是起始日期，终止日期和时区。
            start_date='-1y',  # 1 年前
            end_date="now",  # 终止日期为当下
            tzinfo=timezone.get_current_timezone())
        post = ArticlePost.objects.create(
            title=fake.sentence().rstrip('.'),
            # 用 2 个换行符连起来是为了符合 Markdown 语法，Markdown 中只有 2 个换行符分隔的文本才会被解析为段落
            body='\n\n'.join(fake.paragraphs(10)),  # 10 个段落文本
            created=created,
            author=user,
        )
        post.save()

    fake = faker.Faker('zh_CN')
    for _ in range(100):  # Chinese
        created = fake.date_time_between(start_date='-1y', end_date="now", tzinfo=timezone.get_current_timezone())
        post = ArticlePost.objects.create(
            title=fake.sentence().rstrip('.'),
            body='\n\n'.join(fake.paragraphs(10)),
            author=user,
        )
        post.save()

    print('done!')

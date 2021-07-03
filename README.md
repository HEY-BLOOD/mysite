![mysite](https://socialify.git.ci/HEY-BLOOD/mysite/image?description=1&pattern=Plus&theme=Light)

使用 Django 框架开发的博客系统。基于 Python 3.7、Django 2.2、Bootstrap 4

[![simpleui](https://img.shields.io/badge/developing%20with-Simpleui-2077ff.svg)](https://github.com/newpanjing/simpleui)

## 主要功能：

- 用户登录与注册。
- 用户密码找回，邮箱验证。
- 首页查看全部文章，支持模糊搜索文章。
- 文章详情页，黏性侧边栏目录。
- 文章编辑和删除，集成 [django-mdeditor](https://github.com/pylixm/django-mdeditor) 插件。
- 文章详情页，文章及页面支持`Markdown`，支持代码高亮。
- 文章评论功能，以及评论的通知提醒，支持富文本编辑器。
- 我的收藏页面，查看已登录用户收藏的全部文章。
- 日志系统。

## 配置

**邮件服务：**

将 `.env.example` 文件拷贝一份并保存为 `.env`，并根据你自己的邮件服务进行配置。

说明：

1. 配置文件中的 `EMAIL_HOST`（SMTP 服务器地址）在这里并没有作用（具体是什么原因还不知道），所以请直接在 `mysite/mysite/settings/common.py` 文件中找到 `EMAIL_HOST` 常量为其赋值即可，如：`EMAIL_HOST = 'smtp.qq.com'`。
2. `.env` 文件中的 `EMAIL_HOST_PASSWORD` （邮箱密码或授权码）需要注意，确定你所使用的 SMTP 服务器使用需要邮箱密码还是授权码。
3. 其余的配置跟着改成自己的就行了，`.env`文件中最好不要出现中文。

> **注意：**`.env` 一定要有，否则在迁移数据库的时候会报错。

## 安装


**1. 克隆仓库：**

```sh
$ git clone https://github.com/HEY-BLOOD/mysite.git
$ cd mysite
```

**2. 使用虚拟环境：**

你也可以完全使用你自己的方式来创建环境，比如 conda 或直接使用默认的 Python3

```sh
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
```

**3. 安装项目依赖：**

```sh
$ pip install -r requirements.txt
```

**4. 迁移数据库：**

```sh
$ python manage.py migrate
```

**5. 生成虚拟数据：**

```sh
$ python -m scripts.fake
```

生成的虚拟数据中除了一些文章和评论外，还创建一个管理员帐户，用户名和密码均为 `admin`，可以直接使用它来登录后台。


## 运行
内置服务器运行：

```sh
$ python manage.py runserver 127.0.0.1:8000
```

在浏览器中输入地址 http://127.0.0.1:8000 来访问网站。

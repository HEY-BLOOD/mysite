# mysite

使用Django框架开发的博客系统，从 [杜赛的博客](https://www.dusaiphoto.com/) 学来的。

基于 Python 3.7、Django 2.2、Bootstrap 4

## 安装

**克隆仓库：**

```
$ git clone https://github.com/HEY-BLOOD/mysite.git
$ cd mysite
```

**使用虚拟环境：**

```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
```

**安装项目依赖：**

```
$ pip install -r requirements.txt
```

**迁移数据库：**

```
$ python manage.py migrate
```

**生成虚拟数据：**

```
$ python -m scripts.fake
```

除了一些文章和评论外，还创建一个管理员帐户，用户名为admin，密码为admin。

**邮件服务：**

如果需要配置邮件服务的话，可以将 `.env.example` 文件拷贝一份并保存为 `.env`，并根据你自己的邮件服务进行配置。

## 运行

内置服务器运行：

```
$ python manage.py runserver 127.0.0.1:8000
```

在浏览器中输入地址 http://127.0.0.1:8000 来访问它。


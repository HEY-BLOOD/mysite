![mysite](https://socialify.git.ci/HEY-BLOOD/mysite/image?description=1&pattern=Plus&theme=Light)

使用Django框架开发的博客系统，从 [杜赛的博客](https://www.dusaiphoto.com/) 学来的。

基于 Python 3.7、Django 2.2、Bootstrap 4

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

## 配置

**邮件服务：**

如果需要配置邮件服务的话，可以将 `.env.example` 文件拷贝一份并保存为 `.env`，并根据你自己的邮件服务进行配置。

```
# 密钥
SECRET_KEY=your_secret_key

# SMTP服务器配置，以 QQ邮箱为例
# django.core.exceptions.ImproperlyConfigured: Set the EMAIL_HOST environment variable
EMAIL_HOST=smtp.qq.com
# 改为自己的邮箱名
EMAIL_HOST_USER=your_email_account@xxx.com
# 邮箱密码（授权码）
EMAIL_HOST_PASSWORD=your_password
# 发送邮件的端口，不通请尝试 465 或 587 端口。
EMAIL_PORT=25
# 是否使用 TLS
EMAIL_USE_TLS=True
# 默认的发件人
DEFAULT_FROM_EMAIL=发件人昵称<your_email_account@xxx.com>'
```

说明：

1. 配置文件中的 `EMAIL_HOST`（SMTP 服务器地址）在这里并没有作用（具体是什么原因还不知道），所以请直接在 `mysite/mysite/settings/common.py` 文件中找到 `EMAIL_HOST` 常量未其赋值即可，如：`EMAIL_HOST = 'smtp.aliyun.com'`。
2. `.env` 文件中的 `EMAIL_HOST_PASSWORD` （邮箱密码或授权码）需要注意，确定你所使用的 SMTP 服务器使用需要邮箱密码还是授权码。
3. 其余的配置跟着改成自己的就行了。

## 运行

内置服务器运行：

```sh
$ python manage.py runserver 127.0.0.1:8000
```

在浏览器中输入地址 http://127.0.0.1:8000 来访问它。


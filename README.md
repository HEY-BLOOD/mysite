# mysite

A blog application developed using the Django framework.

Based on the Python 3.7、Django 2.2、Bootstrap 4

Learn [Django搭建个人博客](https://www.dusaiphoto.com/article/2/) from [杜赛的博客](https://www.dusaiphoto.com/)

## Installation

clone:

```
$ git clone https://github.com/HEY-BLOOD/mysite.git
$ cd mysite
```

create & active virtual environment:

```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
```

install dependencies:

```
$ pip install -r requirements.txt
```

migrate database:

```
$ python manage.py migrate
```

create virtual data:

In addition to some virtual article data, and an administrator account with the user name admin and password admin.

```
$ python -m scripts.fake
```

## Run

run by default:

```
$ python manage.py runserver
```

Enter the address http://127.0.0.1:8000 in the browser to access it.


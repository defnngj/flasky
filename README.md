# flasky
"pop up" web app

项目从分支页来：
https://github.com/miguelgrinberg/flasky

虽然是[《Flask Web Development》](https://www.flaskbook.com/) 一书中的练习项目，但实现的功能相当完整。

### 安装

flask是一个微型Web框架，所以，他依赖了大量的第三方扩展。在 requirements.txt 查看。


1、通过以下命令，一次性安装所有依赖包：

    pip install -r requirements.txt

2、执行数据库迁移

    python manage.py db upgrade

3、安装uwsgi

    pip install uwsgi

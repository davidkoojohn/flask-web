## flask-note

```
# Restart app
$ python app.py --help
$ python app.py
||
$ python app.py runserver
$ python app.py runserver --help
```

##### Flask上下文全局变量

* 程序上下文
    1. current_app: 当前激活程序
    1. g: 处理请求时用作临时储存的对象，每次请求都会重设
* 请求上下文
    1. request: 请求对象封装了http
    1. session: 用户会话

##### 请求钩子

1. before_first_request:注册一个函数，在处理第一个请求之前运行。
1. before_request:注册一个函数，在每次请求之前运行。
1. after_request:注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
1. teardown_request:注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。

##### 响应

```
# 状态码视图返回的第二个参数，默认200
@app.route('/')
     def index():
         return '<h1>Bad Request</h1>', 400

# 第三个参数 header，返回Response
from flask import make_response
@app.route('/')
     def index():
         response = make_response('<h1>This document carries a cookie!</h1>')
         response.set_cookie('answer', '42')
         return response

# 重定向302，redirect()辅助函数
from flask import redirect
@app.route('/')
def index():
    return redirect('http://www.example.com')

# abort 函数生成，用于处理错误, 404
from flask import abort
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name
```

##### 渲染模板（render_template）

```
from flask import render_template
```

##### 过滤器，`Hello, {{ name|capitalize }}`

1. safe: 渲染值时不转义
1. capitalize: 把值的首字母转换成大写，其他字母转换成小写
1. lower: 把值转换成小写形式
1. upper: 把值转换成大写形式
1. title: 把值中每个单词的首字母都转换成大写
1. trim: 把值的首尾空格去掉
1. striptags: 渲染之前把值中所有的HTML标签都删掉

##### Jinja2


##### Link

* `url_for ('user', name='john', _external=True)`
* `app.add_url_route()`

##### 表单`flask-wtf
* WTForms支持的HTML标准字段
* WTForms验证函数



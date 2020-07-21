# Flask视图和URL

## url_for

进行反转，把函数名字转成URL

```
url_for('函数名字', 参数1, 参数2)
如果参数2在函数中不存在，则会以?形式当做参数
```

- url_for会进行转码
- 修改了URL地址，对代码影响不大，比硬编码的方式更好



## url末尾的反斜线

## 改变端口

app.run(debug=True, port=端口号, host='IP地址')

## 指定HTTP方法

```
@app.route('路由', methods=['请求方法'])

GET请求
request.args.get('xxx')

POST请求
request.form.get('xxx')
```

## 重定向

```
return redirect(url_for('函数名字', code='xxx'))
code：301永久重定向
		302 暂时重定向
```



## 函数的返回值

- 字符串

  - ```
    return '字符串'
    ```

- 元组

  - ```
    return '字符串',状态码
    ```

- Response

  - ```
    return Response('字符串', '状态码', mimetype='xxx')
    ```

- make_response

  

# 模板

## 模板渲染

先创建一个目录，templates，将模板文件放入目录中，默认查找templates目录下的模板文件

```
return render_template('模板文件名字')
```

## 指定模板目录

```
app = Flask(__name__, template_folder=r'模板存放目录路径')
```

## 模板传参

```
视图中传递参数：
context = {
	xxx: 'xxx'
}
return render_template('index.html', **context)
模板中引用参数：
{{ xxx }}

其他方式：
return render_template('index.html', username='xxx')
{{ username }}

or:
context = {
	xxx:'xxx'
}
return render_template('index.html', context=context)
{{ context.xxx }}
```

## 模板过滤器

###  内置模板过滤器

```
abs
default
last
first
upper
lower
safe
length
truncate
trim
striptags
int/float/string
wordcount
replace
```

## 自定义过滤器

```
@app.template_filter('自定义过滤器名字')
```

## 控制语句

### if

```
{% if 判断条件 %}
	xxxx
{% endif %}
```

### for

```
{% for xx in xxx%}
	{{ xx }}
{% endfor %}
```

## 宏和import语句

### 宏

```
{% macro 宏名字(参数) %}
	xxxx
{% endmacro %} 
```

### import

import一般用于导入宏文件

```
{% import 'xxx.html' as xxx%}
{% from 'xxx.html' import 宏名字%}
{% from 'xxx.html' import 宏名字 as xxx%}
{% import 'xxx.html' as xxx with context%} 将参数传入宏模板中
```

## include

一般用于导入模板文件

导入写好的模板，避免重复写代码

```
{% include 'xxx.html' %}
```

## set 赋值语句

```
{% set name='xxx' %}  定义全局变量name

{% with name='xxx' %}  定义局部变量name，只有在with语句中生效
	{{ name }}
{% endwith %}

{% with %}			也是定义局部变量name，和上面一样
	{% set name='xxx' %}    
{% endwith %}
```

## 模板继承

代码的复用

```
{% extends '父模板.html' %}
```

### 继承的注意点

1、`{% extends '父模板.html' %}`放到block模块最上面

2、不可多继承

3、子模版只能重写父模板中的block，自己定义的block和标签不会现在在网页中

4、父模板中的嵌套block也可以调用

5、继承父模板中的block:{% super() %}

## 加载静态资源文件

创建static文件夹，静态资源文件（css、js、images）放在里面

```
<link rel="stylesheet" href="{{ url_for('static', filename='css/xxx.css') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='css/xxx.jpg') }}">
<link rel="stylesheet" href="{{ url_for('static', filename='css/xxx.js') }}">
```

还可以修改资源文件存放的目录

```
app = Flask(__name__, static_folder='路径')
```

# 案例

思路：

```
1、先看效果图
2、拿到对应的静态资源文件
3、先实现大概功能  # 利用好Bootstrap
4、查看哪些地方可以简化，使用宏、模板的继承技巧、过滤器、set语句、蓝图
5、定义宏、基础的模板文件（用来被继承）

```

# 视图高级

## 类视图

### 标准类视图

```
from flask import views

class XxxXxx(views.View):
	# 必须重写的方法
	def dispatch_request(self):
		return xxx

app.add_url_rule('对应的url', view_func=XxxXxx.as_view('名字')) #这个名字用与被重定向的时候使用，比如名字叫：news，其他视图类中使用redirect(url_for('news')) 来进行重定向
```



## 基于调度方法的类视图

```
from flask import views

class XxxXxx(views.MethodView): #继承MethodView
	def get(self):
		pass
	
	def post(self):
		pass

app.add_url_rule('对应的url', view_func=XxxXxx.as_view('名字')) #这个名字用与被重定向的时候使用，比如名字叫：news，其他视图类中使用redirect(url_for('news')) 来进行重定向
```



## 蓝图

作用：拆分主程序中的功能，把每个功能都作为一个模块独立出来

1、创建blueprints文件夹

2、把模块放进blueprints目录中

news.py蓝图文件

```
fron flask import Blueprint

xxx = Blueprint('蓝图名字',__name__)

@xxx.route('/')
def xxxx():
	return xxxx
```

项目目录下的app.py主文件

```
from blueprints.news import xxx  #这里的xxx指的是蓝图文件中定义的变量

app.register_blueprint(xxx) #导入的蓝图变量需要注册
```

### 寻找模板文件

```
news_bp = Blueprint('new',__name__, url_prefix='/news/', template_folder='blue_templates', static_folder='blue_static')
1、首先会寻找默认的templates目录下的模板文件
2、其次如果找不到templates目录中的模板文件，才会去templte_folder定义的目录中去寻找
```

### 寻找静态资源文件

```
news_bp = Blueprint('new',__name__, url_prefix='/news/', template_folder='blue_templates', static_folder='blue_static')
1、首先会寻找默认的static目录下的模板文件
2、其次如果找不到static目录中的模板文件，才会去static_folder定义的目录中去寻找

# 在默认的static目录中寻找静态资源文件
<link rel="stylesheet" href="{{ url_for('static',filename='news.css') }}">

# 在static_folder指定的目录下去寻找静态资源文件
<!--    这里的new是指对应的蓝图中的名字,查看news.py文件-->
<link rel="stylesheet" href="{{ url_for('new.static',filename='news.css') }}">
```



## 子域名

1.创建蓝图

```
from flask import Blueprint

cms_bp = Blueprint('cms',__name__, subdomain='cms')

@cms_bp.route('/')
def cms():
	return '子域名页面'
```

2.主app中设置

```
app.config['SERVER_NAME'] = 'xxx.com:port'
```

3.修改HOSTS文件

```
127.0.0.1 xxxx.com
127.0.0.1 cms.xxxx.com
```

# 数据库

## 数据库介绍

### 数据库特点

- 读写速度快
- 持久化存储
- 扩展性好
- 数据的有效性

### 数据库结构

- 表
  - 字段
  - 记录

## 通过SQLAlchemy连接

连接库

```
pip install pymysql
pip install sqlalchemy
pip install mysql-connector
```

连接数据库

```
from sqlalchemy import create_engine

DB_URL = 'mysql+pymysql://user:pass@host:port/dbname?charset=utf8'

engine = create_engine(DB_URL)

```

执行原生的SQL语句

```
with engine.connect() as con:
	con.execute('SQL语句')
```



# ORM模型(SQLAlchemy)

ORM：object relational mapping 把关系数据库中的表结构映射到对象上

ORM优点

- 安全
- 封装好了原生的SQL语句
- 简介、易用

ORM映射

- 类-->表
- 属性-->字段
- 实例化对象-->一条记录

## 使用ORM把对象映射到数据库中

```
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData

# dialect+driver://username:password@host:port/database?charset=utf8
DB_URL = 'mysql+mysqlconnector://root:root@127.0.0.1:3306/demo0420'

# 初始化引擎
engine = create_engine(DB_URL,echo=True)

# Construct a base class for declarative class definitions
Base = declarative_base(engine)

# 定义类对象
class Student(Base):
    #定义表名，关键字__tablename__不能改
    __tablename__ = 'student'

    #设置字段
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(50))
    age = Column(String(20))
    gender = Column(Integer,nullable=False,comment='1为男，2为女')

# 将类映射到数据库中
Base.metadata.create_all()
```


# Flask的资源

 [Flask框架.pdf](Flask框架.pdf) 

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

#### for循环变量

```
loop.index		当前循环迭代的次数（从1）
loop.index0		当前循环迭代的次数（从0）
loop.revindex	当前循环的反向索引，如果序列长度为5，则第一次循环这个值为5，然后每次循环减一（5,4，3，2，1）
loop.revindex0	和上面一样，序列长度为5的话，则是第一次值为loop.length-1（4，3，2，1，0）
loop.first		如果是第一次迭代，则为True
loop.last		如果是最后一次迭代，则为True
loop.length		序列长度
loop.previtem	当前循环值的上一个值，如果当前循环是第一次，则上一个值为空
loop.nextitem	当前循环值的下一个值，如果当前循环是最后一次，则下一个值为空
loop.cycle		在一串序列期间取值的辅助函数/辅助循环
```

loop.cycle()的使用

```
<!-- 假设 value=[1,2,3,4,5,6,7] -->
{% for value in values %}
	<p class="{{ lopp.cycle('one','two') }}">{{ value }}</p>
{% endfor %}

<!-- 出来的效果为 -->
<p class="one">1</p>
<p class="two">2</p>
<p class="one">3</p>
<p class="two">4</p>
<p class="one">5</p>
<p class="two">6</p>
<p class="one">7</p>
```

九九乘法表(三种方法)

```
{% for row in range(1,10) %}
	{% for column in range(1,row+1) %}
		{{ row }} * {{ column }} == {{ row*column }}
	{% endfor %}
{% endfor %}


{% for row in range(1,10) %}
	{% for column in range(1,10) if column<=row %}
		{{ row }} * {{ column }} == {{ row*column }}
	{% endfor %}
{% endfor %}


{% for row in range(1,10) %}
	{% for column in range(1,10) %}
		{% if column<=row %}
			{{ row }} * {{ column }} == {{ row*column }}
		{% endif %}
	{% endfor %}
{% endfor %}
```

#### for循环的测试器

测试器主要是用来判断一个值是否满足某种类型

```
callable(object)		是否可调用
defined(object)			是否被定义
escaped(object)			是否应景被转义了
upper(object)			是否全部大写
lower(object)			是否全部小写
string(object)			是否是一个字符串
sequence(object)		是否是一个序列
number(object)			是否是一个数字
odd(object)				是否是奇数
even(object)			是否是偶数
divisibleby(value,num)	value是否能被num整除
sameas(value,other)		判断一个对象是否指向另一个对象相同的内存地址
```

测试器的使用

```
单个参数的测试器的使用：
{% if <variable> is defined %} # 判断变量<variable>是否被定义
	do something...
{% else %}
	do other something...
{% endif %}


两个参数的测试器的使用：
{% if 9 is divisibleby 3 %}
	9能被3整除
{% else %}
	9不能被3整除
{% endif %}
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

## ORM增删改查（CURD）

```
from sqlalchemy impor create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integet, String
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def add():
	user = User(xxxx)  #User是默认为定义过的数据库类
	session.add(user)
	session.add_all([user,user1,...])
	session.commit()
	
def search():
	user = session.query(User).all()
	all()/first()/get()/filter()/filter_by()

#更新
def update():
	#先查询后更新,最后session.commit()
	user = session.query(User).first()
	user.name = 'xxx'
	session.commit()
	#回滚
	session.rollback()  #撤销上一步orm操作(即user.name='xxx')

def delete():
	#查询然后删除
	user = session.query(User).first()
	session.delete(user)
	session.commit()
```

## sqlalchemy常用数据类型

- String
- Float
- Integer
- Boolean
- Date/Time/Datetime
- Enum
- LONGTEXT
- Text
- DECIMAL



## Column常用参数

- default
- name
- nullable
- autoincrement
- primary_key
- onupdate 更新的时候执⾏的函数。 
- unique



## 聚合函数

```
from sqlalchemy import func

max,min,sum,count,avg

session.query(func.聚合函数(模型.列名)).first()
```

## 过滤条件

- equals（==）

  - ```
    filter(模型.字段 == 'xxx').all()
    ```

- not equals（!=）

  - ```
    filter(模型.字段 != 'xxx').all()
    filter(~模型.字段 == 'xxx').all()
    ```

- and_

  - ```
    result = session.query(Article).filter(and_(Article.title == 'title0',Article.price==21)).all()
    ```

- or_：

  - ```
    result = session.query(Article).filter(or_(Article.title=='title0',Article.id.in_([1,2,3,4]))).all()
    ```

- like：('%xxx%') 或like('_xxx%')....

  - ```
    result = session.query(Article).filter(Article.title.like('title%')).all()
    ```

- in_

- notin_

  - ```
    result = session.query(Article).filter(~Article.id.notin_([i for i in range(0,6)]))
    ```

- is_

  - ```
    result = session.query(Article).filter(Article.id.is_(None)).all()
    ```

- isnot

  - ```
    result = session.query(Article).filter(Article.id.isnot(None)).all()
    ```

## 外键以及约束

主表是父表，从表是子表（携带外键的表），举例：用户（主表），银行账户（从表），从表依赖主表。https://zhidao.baidu.com/question/542403418.html

```
from sqlalchemy import ForeignKey

# 表名.字段
uid = Column(Integer,ForeignKey('表名.字段'),ondelete='xxx')
# ondelete常用类型：RESTRICT、NO ACTION、CASCADE、SET NULL

# 外键的查询
session.query(User).filter(User.id == Article.uid).first()
```

## 表关系

### 一对多

```
from sqlalchemy.orm import relationship
#一对多 表关系
class Article(Base):
    __tablename__ = 'article3'

    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50))
    content = Column(Text,nullable=False)
    uid = Column(Integer,ForeignKey('user3.id'))

    author = relationship('User')

#一个用户对应多篇文章
class User(Base):
    __tablename__ = 'user3'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False)

    #可以添加backref='author',这样的话 Article类中不需要添加author字段
    # articles = relationship('Article',backref='author')
    articles = relationship('Article')

```

### 一对一

```
https://blog.csdn.net/weixin_30670151/article/details/95969853

class User(Base):
    __tablename__ = 'user4'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))

    uid = Column(Integer,ForeignKey('user4.id'))

    user = relationship('User',backref=backref('extend',uselist=False))
	# 这里relationship中的backref中添加uselist

```



### 多对多

```
中间表
from sqlalchemy import Table

xxx = Table(
	'表名字',
	Base.metadata,
	Column(外键),
	Column(外键),
	)

classes = relationship('Class',backref='teachers',secondary=中间表名字)
#这里relationship中需要添加secondary


例子：
teachers_classes = Table(
    'teachers_classes',
    Base.metadata,  #如果用了flask_sqlalchemy，则这句话不用写
    Column('teachers',Integer,ForeignKey('teachers.id')),
    Column('classes',Integer,ForeignKey('classes.id')),
)

class Teacher(Base):
    __tablename__='teachers'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50))
    classes = relationship('Class',backref='teachers',secondary=teachers_classes)
    def __str__(self):
        return 'teachers(id:{},name:{},classes:{})'.format(self.id,self.name,self.classes)

class Class(Base):
    __tablename__='classes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    def __str__(self):
        return 'classes(id:{},name:{},teachers:{})'.format(self.id,self.name,self.teachers)

```

## 排序

- session.query(模型).order_by(字段).all()

  - 默认升序asc()，降序desc()
  - 降序也可以通过在字段前添加 '-'（负号）

- 在模型中定义

  - ```
    __mapper_args__ ={
    	'order_by':['-id','xxx']
    } 
    ```

## limit offset 切片

```
limit 	条数
offset 	偏移量
切片	   Python层面的切片操作

articles = session.query(Article).order_by(Article.id).limit(3).offset(2).all()[1:2]

```

## 分组和分组之后的筛选

```
group_by()

result = session.query(User.gender,func.count(User.id)).group_by(User.gender).all()  

having()

result = session.query(User.age, func.count(User.id)).group_by(User.age).having(User.age <= 18).all()

```

## Flask-SQLAlchemy

Flask-SQLAlchemy插件，是对SQLAlchemy进行了简单的封装，使用可以在flask中更加简单的使用sqlalchemy语法。引入了Flask-SQLAlchemy中的SQLAlchemy，则可以不需要from sqlalchemy impor create_engine和from sqlalchemy.ext.declarative import declarative_base，取而代之如下

```
安装
pip install flask-sqlalchemy

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(50))

class Article(db.Model):
	uid = db.Column(db.Integer, db.ForeignKey('user.id'))
	author = db.relationship('User', backref='articles')

db.drop_all()
db.create_all()

#查询
User.query.all()
db.session.query(User).all() # 和上面一句一样的效果
```

## Flask-Script与Flask-Migrate

Flask-Script作用：可以在命令行中使用命令去将models.py文件中定义好的模型类映射到数据库中

Flask-Migrate：配合Flask-Script使用

安装

```
pip install flask-script
pip install flask-Migrate
```

### 第一种写法：

flask-script：可以在命令行执行自己定义的函数

```
migrate.py文件下
from flask_script import Manager
from xxx(主程序文件) import app

manager = Manager(app)

@manager.command
def index():
	print('hello')
```

给命令传参数(可以在函数编写修改数据库代码，然后通过命令行去执行)

```
@manage.option('-u','--name',dest='name')
@manage.option('-e','--email',dest='email')
def add_user(name,email):
    user = AdminUser(name=name,email=email)
    db.session.add(user)
    db.session.commit()
if __name__ == '__main__':
    manage.run()
   
   
在虚拟环境命令行下：python migrate.py add_user -u xxx -e xxx
```

### 第二种写法：

migrate.py(manage.py)下

```
# 通过这个文件去映射数据库

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db  #这个exts是公共py文件，存放一些被公共调用的变量（防止两个文件双向调用）
from flask_app import app  # 从主程序文件flask_app中调用变量app


#映射哪个模型 就把哪个模型导入进来
from models import User
manage = Manager(app)

Migrate(app,db)

manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()

```



## 项目目录

- static文件夹
  - 静态资源文件
- templates文件夹
  - 模板文件
- blueprint文件夹
  - 蓝图
- models.py
  - 模型
- config.py
  - 配置文件
- forms.py
  - 表单验证
- manage.py(可以写成migrate.py，这是自定义的)（python manage.py xxx）
  - 数据库映射文件
- app.py
  - 项目入口文件

## 映射数据库命令

```
# 初始化一个迁移文件夹
python manage.py db init

# 把当前的模型添加到迁移文件中
python manage.py db migrate

# 把迁移文件中对应的数据库操作，真正的映射到数据库中
python manage.py db upgrade
```

## 表单验证

安装

```
pip install flask-wtf
```

注册表单验证

```
froms.py下

from wwtforms import Form,StringField,validators
from wtforms.validators import Length, Regexp, EqualTo

class RegisterForm(Form):
    username = StringField(validators=[Length(min=3,max=10,message='长度问题')])
    password = StringField(validators=[Length(min=3,max=10,message='长度问题')])
    password_repeat = StringField(validators=[Length(min=3, max=10,message='长度问题'),EqualTo('password',message='两次密码不一致')])
```

常用验证器

- EqualTo
- Email
- Regexp
- URL
- NumberRange
- 文件上传
  - FileRequired
  - FileAllowed
  - 前端中form标签中加入属性enctype
  - 视图中CombinedMultiDict，requestCombinedMultiDict([request.form,request.files])



# Cookies 和 Session

## cookie

Http是无状态的 cookie 用来记录用户信息，大小为4K，以文件的形式存储在浏览器中

```
from flask import Response

@app.route('xxx')
def xxxx():
	res = Response('xxx')
	res.set_cookie()
	return res
```

## session

flask的session模式：session信息保存在服务器中，session id保存在cookie中，cookie保存在浏览器

```
from flask import session

app = Flask(__name__)

# app.config['SECRET_KEY'] = '随机字符串'  #可以用os.urandom(20)函数
app.config['SECRET_KEY'] = os.urandom(24)

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2) # 设置过期时间

@app.route('/login/')
def login():
    session['username'] = 'hhh' # 设置session信息
    session['pass'] = '123'
    #持久化
    session.permanent = True
    return '登录页面'

@app.route('/')
def index():
    username = session.get('username') #用get()方法获取session值
    return '首页'
    
@app.route('/logout')
def logout():
    # session.pop('username')   #删除对应的session信息
    session.clear()				#删除所有session信息
    return '退出'
```

# Flask中上下文

- 请求上下文对象
  - request

  - session

- 应用上下文对象

  - current_app
  - g

# 钩子函数 hook

```python
@app.before_first_request		#第一次请求之前执行
@app.before_request				#每次请求之前
@app.after_request				#每次请求之后
@app.teardown_appcontext		#每次请求之后，不管有没有异常都会执行（debug需要为false）
@app.context_processor			#上下文处理器 返回数据到所有的模板中
@app.errorhadler(错误状态码)		 # debug需要关闭
```

示例：

```
from flask import Flask,render_template,abort

app = Flask(__name__)


@app.route('/')
def index():
    abort(404)  
    #abort函数 主动抛出异常，主动会跳转到404函数（@app.errorhandler(404)对应的函数）
    
    print('shouye')
    # return '首页'
    username = 'shouye'
    content = {
        'username':'qqq'
    }
    return render_template('index.html',**locals()) 
    #**locals()将所有变量传递到模板中

@app.route('/list/')
def list():
    return render_template('list.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404
    # return '页面不存在',404

@app.errorhandler(500)
def server_error(error):
    return '服务器内部错误'

@app.context_processor
def context_processor():
    return {'username':'ddd'}

@app.before_first_request
def handle_before_first_request():
    print('这是第一次请求之前执行的')


@app.before_request
def handle_before_quest():
    print('每次请求之前执行的')

@app.after_request
def handle_after_request(response):
    print('每次请求之后执行的')
    return response


@app.teardown_appcontext
def handle_teardown(response):
    print('teardown被执行')
    return response


if __name__ == '__main__':
    app.run(debug=True)
```

# Restful 

Restful：restful通俗来说是一种规范概念，用与在前端与后台进行通信的一套规范。

Flask-Restful：一个专门用来写restful api(大多数返回json数据，少数xml数据)的一个插件，

多用于app的后台和纯api的后台。对于普通的网页开发，几乎没什么作用，因为视图函数中的返回值都是render_to_templates，几乎不会有json数据返回

```
安装：
pip install flask-restful

定义Restful的视图：from flask_restful import Api,Resource

参数解析：Flask-Restful插件提供了类似WTForms的功能来验证用户提交上来的数据是否合法，reqparse包

输出字段：视图函数中，可以指定一些字段用于返回到前端
```

例子一：简述reqparse验证前端提交上来的数据的功能

```
from flask_restful import Resource,Api,reqparse,inputs,fields,marshal_with
from flask  import Flask

app = Flask(__name__)

api = Api(app)				# restfule的Api绑定app


class IndexView(Resource):	# 视图类必须继承Resource
    def get(self):
        return {'user':'name'}

    def post(self):
        parse = reqparse.RequestParser()	#reqparse用于验证用户数据
        parse.add_argument('username',type=str,help='用户名验证错误',required=True)		# 第一个参数(username)对应着html标签的name属性的值
        parse.add_argument('gender',type=str,help='性别错误',choices=['male','female','secret'],default='secret')
        parse.add_argument('url',type=inputs.url,help='url错误',required=True)		# inputs里面也有类型定义，例如这里的url
        parse.add_argument('phone',type=inputs.regex(r'^1[3456789]\d{9}$'),help='手机号码错误错误',required=True)
        args = parse.parse_args()
        print(args)
        return {'res':'发送成功'}


api.add_resource(IndexView,'/',endpoint='index')

if __name__ == '__main__':
    app.run(debug=True)

```

例子二：指定一些输出字段返回到前端中

```
主程序文件中：
from flask_restful import Resource,Api,fields,marshal_with
from flask  import Flask
import config  
from exts import db    			#exts.py中定义中间变量db = SQLAlchemy()
from models import Article

app = Flask(__name__)
app.config.from_object(config) #配置文件config有写数据库的配置
db.init_app(app)				#app变量应用在orm模型中

api = Api(app)					# restfule的Api绑定app

class ArticleView(Resource):	# 视图类必须继承Resource
    resource_fields = {			# 指定定义一些字段，用于下面return到前端页面
        # 'title':fields.String,
        'article_title':fields.String(attribute='title'), #前端显示article_title，但实际上数据库的字段是title，相当于更改了显示的名字
        'content':fields.String,
        # 'author':fields.String,
        'author':fields.Nested({	# fields.Nested()以字段形式展示
            'username':fields.String,
            'email':fields.String,
        }),
        # 'tags':fields.String,
        'tags':fields.List(fields.Nested({   #fields.List()代表字段中有列表
            'id':fields.String,
            'name':fields.String,
        })),
        'read_count':fields.Integer(default=0)  #此字段在数据库中并不存在，也可以返回到前端中
    }

    #添加了@marshal_with()装饰器，即使return只返回了title，也会将resource_fields中剩下的字段给自动返回到html中
    @marshal_with(resource_fields)
    def get(self,article_id):
        article = Article.query.get(article_id) #查询数据库
        return article

# 定义url，endpoint相当于name
api.add_resource(ArticleView,'/art/<int:article_id>',endpoint='art')

if __name__ == '__main__':
    app.run(debug=True)

```


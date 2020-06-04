

# Django框架 

 [Django.pdf](D:\Data\Desktop\Django.pdf) 

## 框架思想

- MVC思想

  - ```
    M：model 模型
    V：view 视图
    C：controller 控制器
    ```

  - ```
    流程：
    1、Browser请求Controller
    2、Controller接收到请求后的数据传给Model
    3、Model去访问数据库
    4、数据库返回信息给Model
    5、Model返回信息给Controller
    6、Controller把数据交给View处理
    7、View将处理好的信息返回给Controller
    8、Controller将信息返回给Browser
    ```

    ![image-20200420232853449](C:\Users\dujun\AppData\Roaming\Typora\typora-user-images\image-20200420232853449.png)

- MVT思想（Django使用的思想）

  - ```
    M：model 模型
    V：view 视图
    T：template 模板
    ```

    ![image-20200420232927738](C:\Users\dujun\AppData\Roaming\Typora\typora-user-images\image-20200420232927738.png)

    

## 虚拟环境

1、virtualenv

2、virtualenvwrapper

3、pipenv

### 环境

```
开发环境：程序员写代码的地方
生成环境：项目上线的环境
```

## 项目介绍

### 创建项目和app

```
django-admin startproject '项目名字' #创建项目
python manage.py runserver # 运行项目
python manage.py startapp 'app名字' #创建app
python manage.py help # 查看全部命令
```

### 项目结构介绍

- 项目目录中的文件

  - ```
    manage.py：以后和项目交互基本上都是基于这个文件。一般都是在终端输入python manage.py [子命令]。可 以输入python manage.py help看下能做什么事情。除非你知道你自己在做什么，一般情况下不应该编辑这个文件。
    
    settings.py：本项目的设置项，以后所有和项目相关的配置都是放在这个里面。
    
    urls.py：这个文件是用来配置URL路由的。比如访问http://127.0.0.1/news/是访问新闻列表页，这些东西就需 要在这个文件中完成。
    
    wsgi.py：项目与WSGI协议兼容的web服务器入口，部署的时候需要用到的，一般情况下也是不需要修改的。
    
    ```

- app中的文件

  - ```
    __init__.py 说明目录是一个Pyyhon模块
    
    model.py 写和数据库相关的内容
    
    views.py 接受请求，处理数据，与Model和Template交互
    
    test.py	 写测试代码的文件
    
    admin.py 网站后台管理相关的文件
    ```

### url映射

```
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from news.views import news  #导入news  app中的视图函数

def index(request):
    return HttpResponse('<h1>首页</h1>')

def books(request):
    return HttpResponse('books')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),			#映射路由
    path('news/',news),
    path('books/',books)
]
```

### DEBUG模式

```
在settings.py中设置
1、开启了debug模式，那么修改代码后按ctrl+s保存后，Django会自动重启项目
2、Django项目中代码出现了问题，会在浏览器页面和控制台中打印出错误信息
3、如果项目上线了，需要关闭debug模式，不然错误信息会暴露在浏览器页面中
4、关闭了debug模式后需要指定allowed_host，日志文件
```



## 视图与URL映射

### 指定url传递的参数的类型

两种参数：
1、在/后面传递的参数

```
path('<int:bid>',views.books)
这个参数可以规定类型，上面规定int
查看方式：from django.urls import converters
```

2、在?后面传递的参数

```
这种参数是直接在视图函数中通过request方法获取
xxx/?name=ddd
name = request.GET.get('name')   #name为ddd
```

### URL模块化

include函数，将url路由模块化，分别在每个app下urls.py文件中映射好对应函数，然后集中在项目的urls.py中映射

作用：

```
分工合作，防止导入代码冲突
```

```
from django.urls import include

在项目下的urls.py文件下：
path('books/',include('books.urls')),

在books（app）下的urls.py文件下：
from django.urls import path
from . import views

urlpatterns = [
    path('',views.books),
]
```

### 重定向、反转、url命名、应用命名空间、实例命名空间

redirect、reverse、url命名、应用命名空间四个一般同时使用，实例命名空间一般少用

#### redirect、reverse、url命名、应用命名空间

front(app)下的views.py

```
from django.shortcuts import redirect,reverse  #导入对应的重定向和反转函数
from django.http import HttpResponse

def front(request):
    name = request.GET.get('name')  #判断前台界面是否有传参数name
    if name:
        return HttpResponse('front页面')  #有传就返回到front页面
    else:
		return redirect(reverse('front:login'))  #否则重定向到对应的app名为front下的url名为login的url路由中
```

front(app)下的urls.py

```
from django.urls import path
from . import views

app_name = 'front'  #应用命名空间

urlpatterns = [
    path('',views.front),
    path('signin/',views.login,name='login') #name为url命名
]
```

#### 实例命名空间

是指在项目下的urls.py文件下的path函数中，如果一个app映射了对应的路由，就相当于创建了一个实例，下面是创建了两个实例，分别对应的路由是 cms1/ 和 cms2/

项目的urls.py下：

```
 path('cms1/',include('cms.urls', namespace='cms1')),  #namespace为实例命名空间关键字，相当于实例名字
 path('cms2/',include('cms.urls',namespace='cms2')),
```

cms（app）下的views.py：

```
def cms(request):
    name = request.GET.get('name')
    if name:
        return HttpResponse('cms页面')
    else:
        # return redirect('signin/')
        current_namespace = request.resolver_match.namespace #相对应这边需要接收对应的实例名字
        print(current_namespace)
        return redirect(reverse('{}:login'.format(current_namespace))) #反转到对应的实例下的url名为login下的url路由中
```

cms（app）下的urls.py：

```
from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('',views.cms),
    path('signin/',views.login,name='login'),
]
```

#### reverse反转中传递参数

##### 传递/形式的参数

views.py下：

```
return redirect(reverse('front:login',kwargs={'fid':1})) # 传递的参数为fid，由于这是/形式的参数，对应的函数中也需要接收，还有对应url路由映射中也需要传递
def login(request,fid): #这里需要写参数fid
	return HttpResponse('front:login,接收到的参数：{}'.format(fid))
```

urls.py下：

```
path('signin/<fid>',views.login,name='login') #这里需要<fid>
```

##### 传递?形式的参数

views.py下：

```
param = reverse('front:login') + '?name=ddd'  #这里是跳转到url名为login对应的url路由下
return redirect(param)

def login(request):
    param  = request.GET.get('name')
    return HttpResponse('front:login,接收到的参数：{}'.format(param))
```

### 指定默认参数

是指函数中给定的参数给它个默认值

例如：

```
def index(request,bid=1):  #这里的参数bid默认为1
	return HttpResponse('xxx')
```

### re_path函数

```
urlpatterns = [ 
    re_path(r"^$",views.article), 
    re_path(r"^article_list/(?P<year>\d{4})/",views.article_list), 
    re_path(r"^article_list/(?P<mouth>\d{2})/",views.article_mouth) 
]
https://blog.csdn.net/dxcve/article/details/82108479
```

## Template

Django模板引擎：DTL（django template language）

### 引用模板

```
1、在视图函数中使用render函数
2、创建对应的templates文件夹存放模板文件
3、在settings.py文件中设置模板的路径
```

### 模板变量

```
在视图函数中可以传递变量到模板中：render函数
模板中使用变量：{{}}方式
模板内置的变量：forloop.counter/forloop.first/forloop.last......
```

### 模板标签

```
通过{% %}方式使用标签
类型：if、for、url
```

### 模板过滤器

内置的过滤器：https://blog.csdn.net/a599174211/article/details/82751693

自定义过滤器：https://docs.djangoproject.com/zh-hans/2.2/howto/custom-template-tags/

```
{{需要过滤的值|过滤器函数:过滤器参数}}
```

### 模板结构优化

#### include和extends

为了不重复写代码

```
include标签引入模板
extends标签继承模板，模板中可以重写父模板中的block标签
```

### 加载静态资源文件

静态资源：CSS、JavaScript文件以及常用图片（不经常变动的资源）

- 首先看settings.py中

  - ```
    INSTALLED_APP下是否有'django.contrib.staticfiles'
    
    如果有：
        STATIC_URL = '/static/'  # 设置App的静态资源文件夹static
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR,'staitc') #设置根目录的静态资源文件夹static
        ]			
    
    如果没有：
    	可以在项目目录下的urls.py中添加：
    	from django.conf.urls.static import static
    	from django.conf import settings
    	urlpatterns = [
        path('admin/', admin.site.urls),
    ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    #在这里加了static后，可以在url中访问地到静态资源文件
    ```

- 模板中引用

  - ```
    {% load static%}
    <link rel="stylesheet" href="{% static 'color.css' %}">
    <img src="{% static 'zuanshi.png'%}" alt="">
    ```

  - 如果想省略{% load static %}语句

    - ```
      在settings.py下的TEMPLATES中添加
      'builtins':['django.templatetags.static']
      ```

### 加载媒体资源

媒体资源：经常变动的资源（用户头像、歌曲文件等）

- MEDIA_URL

  - 用于设置媒体资源的路由地址

- MEDIA_ROOT

  - 用于获取media文件夹在计算机系统的完整路径信息

- settings.py中

  - ```
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR,'media')
    ```

- 配置属性设置后，还需将media文件夹注册到Django里，让Django知道如何找到媒体文件，否则无法在浏览器上访问到该文件夹的文件信息

  - 根目录下的urls.py

    - ```
      from django.urls import re_path
      from django.views.static import serve
      from django.conf import settings
      ```

    - ```
      urlpatterns = [
      	re_path('media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT},name='media')
      ]
      ```

    - 

## Django<-->数据库

### 原生SQL和ORM模型方式

- 通过写原生SQL语句
- ORM模型：
  - object relational mapping 对象关系映射，通过把Python写好的类对象映射成数据库的表，来达到更好的操作数据库的效果，会把对应的python对象中操作转换为SQL原生语句，从而去查询或者修改数据库

### 前提

```
Django去操作数据库，实际上还是通过Python代码。因此想要使用Django去操作MySQL的话，需要安装驱动程序去创建Django与数据库之前的连接接口。
驱动程序：pymysql、mysqlclient等
Django也有封装好的接口对象：connection  
```

### 连接操作数据库

```
使用封装好的connection对象：
	需要在settings.py中写好对应的数据库信息，connection对象会自动去读取
	连接并操作：
		from django.db import connection
		cursor = connection.cursor() #创建游标
        cursor.execute('select * from books') #通过原生SQL语句去操作数据库
    	cursor.fetchall()
 
 使用驱动程序pymysql：
 	不需要在settings.py中配置数据库信息
 	from pymysql import *
 	connection = connect(host='127.0.0.1', port=3306, database='django0423', user='root', passwd='root')   #这里需要填写对应的数据库信息
 	cursor = connection.cursor()
        cursor.execute('select * from books')
    	cursor.fetchall()
```

### 小任务：图书管理系统

```
实现展示数据库中图书的信息，添加和删除功能
```

### ORM模型应用

#### 创建ORM模型

```
在models.py下创建
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,null=False, default='')
    author = models.CharField(max_length=20, null=False, default='')
    price = models.FloatField(default=0)
```

#### 将创建好的对象映射到数据库中

```
1、settings.py下配置好数据库信息，INSTALLED_APPS中添加app名字
2、在命令行终端项目路径下输入：python manage.py makemigrations 生成迁移脚本文件
3、python manage.py migrate 将迁移脚本文件映射到数据库中
```

#### ORM增删改查

```
from django.shortcuts import render
from .models import Book


def index(request):
    # book = Book(name='python',author='guishu',price=99) #实例化对象
    # book.save()	#保存到数据库中
    # print(book)

    # 查询数据
    # book = Book.objects.get(pk=1)
    # print(book)
    # book = Book.objects.filter(name='python')
    # print(book)
    # book = Book.objects.all()
    # print(book)

    # 删除数据
    # book = Book.objects.filter(pk=1)
    # book.delete()

    #修改数据
    # book = Book.objects.get(pk=2)
    # book.name = 'go'
    # book.save()
    # book = Book.objects.filter(pk=3)
    # for b in book:
    #     b.name = 'go'
    #     b.save()
    return render(request,'index.html')
```

#### 模型常用字段

https://www.cnblogs.com/ivqi/p/10074877.html

````
AutoField
BigAutoField
BooleanField 	#可以用作伪删除is_delete
CharField		#相当于varchar
DateTimeField	
EmailField
ImageField
FloatField
IntegerField
BigIntegerField
PositiveIntegerField
SmallIntegerField
PositiveSmallIntegerField
TextField
UUIDField
URLField
````

#### Field的常用参数

```
null
db_column # 修改字段名字不常用
default
primary_key
unique
max_length
```

#### 模型中Meta配置

```
对于一些模型级别的配置。我们可以在模型中定义一个类，就做Meta。然后再这个类中添加一些类属性来达到控制模型的作用。
例如：修改表名关键字: db_table 
	 排序关键字: ordering

例子：
class Book(models.Model):
    id = models.AutoField(primary_key=True) #定义字段
    price = models.FloatField(default=0)
    
    class Meta:
        db_table = 'book_model'  #修改表名
        ordering = ['-id','price']  #views中查询的顺序是按id倒序和price正序

```

#### 外键和表

```
外键引用的表是在同一个app中：
models.ForeignKey('对应模型中的类名',on_delete=models.CASCADE) #级联删除

外键引用的表为自身：
class Comment(models.Model):
    content = models.TextField()
    user_comment = models.ForeignKey('self',on_delete=models.CASCADE) # self可以替换成自己的类名（Comment）

外键引用的表是不在同一个app中：
models.ForeignKey('appname:对应模型中的类名',on_delete=models.CASCADE) #级联删除
```

在视图中绑定外键

```
def article(request):
    # category = Category(name='LOL') 	# 外键表
    # category.save() 					# 若没有记录则先生成记录
    
    category = Category.objects.get(pk=2) # 主键为2的记录
    
    article = Article(name='zuoyi',author='zuoyi')
    article.category=category 			# 外键绑定对应的Category表中的主键为2的记录
    article.save()						# 保存

    article = Article.objects.first()
    print(article.category.name) 		# 直接获取外键表中的数据

    return HttpResponse('success')
```

外键和表的关系：

```
on_delete=models.CASCADE
on_delete=models.PROTECT
on_delete=models.SET_NULL
on_delete=models.SET_DEFAULT
on_delete=models.SET()
on_delete=models.DO_NOTHING
```

#### 查询操作

```
get()：只能返回一条数据，Books.objects.get(pk=1)
all():返回QuerySet查询集
filter()：条件查询，返回QuerySet查询集，可以通过逗号连接多个条件，Books.objects.filter(pk=x,name=xxx)
exclude():filter函数取反,Books.objects.exclude(pk=3) 查询主键不为3的记录
```

```
__exact:精确查询相当于=号，区分大小写。iexact不区分
__contains:like查询(BINARY LIKE ‘%xxx%’),区分大小写。icontains不区分大小写
__startswith:like查询(BINARY LIKE 'x%')
__gt:大于。gte大于等于
__lt:小于。lte小于等于
__in:判断数据是否在给定的值里(__in=[1,3])
__range：判断数据是否在给定的范围里（__range=(x,x)）,常用来判断日期
__date：针对date或datetime类型的字段（__date=datetime(year=xx,month=xx,day=xx)）
__year:__year=2019
__time:__time=(hour=10,minute=20,second=30)
```

```
聚合函数
aggregate：返回聚合函数后的字段和值，返回的对象是一个字典
annotate：在查询结果集上添加一个字段，该字段是使用了聚合函数的字段，会对当前模型的主键进行分组，返回一个QuerySet查询结果对象集（可遍历）
from django.db.models import Avg,Sum,Count,Min,Max
Avg：Book.objects.aggregate(my_avg=Avg('price')) # my_avg是名字
Count('xxx')
Sum：book = Book.objects.aggregate(Sum('bookorder__price')) #bookorder是另一个模型的类名（这里bookorder模型与Book模型是有外键的关系，所以才可以跨表查询）
Mix('xxx')
Max('xxx')
```

```
F表达式和Q表达式
from django.db.models import F,Q
F表达式：适用于更新数据
	例子：
	#把三国演义书的价格提高10元
    book = Book.objects.filter(name='三国演义').update(price=F('price')+10)
    不使用F表达式：
    book = Book.objects.filter(name='三国演义')
    for b in book:
       b.price += 10
       b.save()
Q表达式：适用于多个查询条件
	例子：
	# 查询书的价格大于等于98 或 评分大于4.5的书籍
    book = Book.objects.filter(Q(price__gte=98)|Q(rating__gt=4.5))
    # 这里的|也可以换成&，取反Q表达式~Q
```

#### QuerySet

查看SQL语句

```
from django.db import connection
print(connection.queries)  #查看SQL语句

针对QuerySet对象：
例如：book=Book.objects.filter('xxx')
	 print(book.query) #查看SQL语句
```

QuerySet方法

```
filter
exclude
annotate
order_by
values
values_list
select_related # 一对一
prefetch_related #多对一、多对多
create
get_or_create
exists
update
切片操作：[1:3]
```

QuerySet对象在何时会被转换为SQL语句去执行？

```
1、迭代：QuerySet对象被迭代的时候
2、使用切片操作
3、调用len函数
4、调用list函数
5、判断：对某个QuerySet进行判断，也会被转换成SQL语句去执行
```

#### 迁移脚本文件过程命令

- 迁移过程

  - ```
    1、使用makegrations生成迁移脚本文件 #文件存放在app文件下的migrations目录下
    2、migrate将迁移脚本文件迁移到数据库中：
    	2-1：将迁移脚本中的命令转换成对应的SQL语句并在数据库中执行
    	2-2：执行成功后，在数据库下的migrations表中记录此次迁移过程 	# 下面内容有引用此2-2阶段
    ```

- makemigrations：生成迁移脚本文件

  - ```
    python manege.py makemigrations app_label  # 指定生成app的迁移文件，不指定则生成所有app和系统的迁移脚本文件
    ```

  - ```
    python manage.py makemigrations --name '迁移脚本文件名字'
    ```

  - ```
    python manage.py makemigrations --empty  # 生成一个空的迁移脚本
    ```

- migrate：将生成好的迁移脚本映射到数据库中

  - ```
    python manege.py migrate app_label
    ```

  - ```
    python manege.py migrate app_label migrationname #将app下的指定号的迁移脚本文件映射到数据库中
    ```

  - ```
    python manege.py migrate --fake #只执行上述迁移过程的2-2阶段，并不会将迁移脚本文件转换成SQL语句去修改数据库。--fake适用于迁移脚本文件没有缺少，但是数据库下的迁移记录缺少的情况
    ```

  - ```
    python manege.py migrate --fake-initial # 和fake类似，也不会真正的执行迁移脚本文件，只是添加了迁移记录。适用于迁移脚本文件有缺少，且数据库下的迁移记录也缺少的情况。
    
    实现过程：
    		1、app模型字段和数据库保持一致
    		2、将app下的migrations目录下的迁移脚本文件都删除掉
    		3、删除数据库migrations表下对应app的记录
    		4、python manege.py makemigrations app_label
    		5、python manege.py migrate app_label --fake-initial
    ```

- showmigrations：查看某个app下的迁移文件。如果后面没有app，那么将查看INSTALLED_APPS中所有的迁 

  移文件

  - ```
    python manage.py showmigrations [app名字]
    ```

- sqlmigrate：查看某个迁移文件在映射到数据库中的时候，转换的SQL语句 

  - ```
    python manage.py sqlmigrate book [0001_initial]
    ```

#### 根据已有的表自动生成模型

1、在settings.py中指定想要生成模型的数据库

2、python manage.py inspectdb > models.py  #将数据库中的表转换为ORM模型的类对象语句并保存在models.py文件中

3、得到对应的模型后，需要去修正模型（因为会将一整个数据库的表转换后的模型语句都放在一起，我们要将他们手动分配到对应的app下）

- ```
  模型名、模型所属app、模型外键引用、删除Meta类下的managed=False语句、有多对多的模型时，将中间表注释掉，添加ManyToManyField字段
  ```

- 修改完后，执行python manage.py makemigrations和python manage.py migrate --fake-initial

## 视图高级

### Django限制请求method、页面重定向301和302

限制请求装饰器：

```
from django.views.decorators.http import require_http_methods,require_GET,require_POST,require_safe


# 视图高级部分
def index(request):
    return render(request,'index.html')

@require_http_methods(['GET','POST'])
def view_methods(request):
    # data = request.POST['pass']         #获取不到则会将错误信息暴露在页面上
    data = request.POST.get('passw')     #获取不到不会将错误信息展现在页面上
    if data == '123':
        print(data)
    return HttpResponse('view_methods')

# @require_GET
# @require_POST
@require_safe  #这个相当于GET和HEAD请求  因为都不会对数据库有修改，所以称作是safe
def view2(request):
    return HttpResponse('views')

def view_redirect(request):
    # return redirect(reverse('index'),permanent=False) #暂时重定向301
    return redirect(reverse('index'),permanent=True) #永久重定向302
```

### HttpRequest对象

```
WSGI：Python社区创建了Web服务器网关接口（WebServerGatewayInterface，WSGI），这是创建跨服务器和框架工作的PythonWeb组件的标准。
```

```
Django在接收到http请求之后，会根据http请求携带的参数以及报文信息创建一个WSGIRequest对象，并且作 为视图函数第一个参数传给视图函数。也就是我们经常看到的request参数。在这个对象上我们可以找到客户端 上传上来的所有信息。这个对象的完整路径是django.core.handlers.wsgi.WSGIRequest。
```

- WSGIRequest对象常用属性

  - ```
    WSGIRequest对象上大部分的属性都是只读的。因为这些属性是从客户端上传上来的，没必要做任何的修改。
    ```

  - ```
    def view_adv(request):
        # print(request)
        # print(request.path)
        # print(request.path_info)
        # print(request.method)
        # print(request.GET)
        # print(request.POST)
        # print(request.COOKIES)
        # print(request.session)
        # print(request.META)
        # print(request.content_type)
    ```

- WSGIRequest对象常用方法 

  - ```
        # print(request.get_full_path())
        # print(request.is_secure())
        # print(request.is_ajax())
        # print(request.get_host())
        # print(request.get_raw_uri())
    ```

### HttpResponse对象

```
Django服务器接收到客户端发送过来的请求后，会将提交上来的这些数据封装成一个HttpRequest对象传给视图 函数。那么视图函数在处理完相关的逻辑后，也需要返回一个响应给浏览器。而这个响应，我们必须返回 HttpResponseBase或者他的子类的对象。而HttpResponse则是HttpResponseBase用得最多的子类
```

- 常用属性 

  - ```
        # response = HttpResponse(content_type='text/plain;charset=utf-8')
        # response.content = 'response:view_adv'
    
        # response.status_code = 404
        # response['X-Access-Token'] = 'xxxx'。
        # return response
    ```

- 常用方法

  - ```
    1.set_cookie：用来设置cookie信息。 
    2.delete_cookie：用来删除cookie信息。 
    3.write：HttpResponse是一个类似于文件的对象，可以用来写入数据到数据体（content）中。
        # response.write('sdsdsd')
    ```

### JsonResponse

```
用来对象dump成json字符串，然后返回将json字符串封装成Response对象返回给浏览器。并且他的Content- Type是application/json。
```

```
from django.http import JsonResponse

def index(request):
    data = {
            'username':'ddd',
            'pass':'asdasd'
        }
    data2 = ['哈哈','dasdasd']  #要传递非字典，需要去设置safe参数为False
    # return  JsonResponse(data=data) #传递字典
    return  JsonResponse(data=data2,safe=False,json_dumps_params={'ensure_ascii':False}) #要传递非字典，需要去设置safe参数为False,传递中文需要设置json_dumps_params参数
```

### 类视图

#### View

- ```
  django.views.generic.base.View是主要的类视图，所有的类视图都是继承自他。如果我们写自己的类视图，也 可以继承自他。然后再根据当前请求的method，来实现不同的方法。比如这个视图只能使用get的方式来请求， 那么就可以在这个类中定义get(self,request,*args,**kwargs)方法。以此类推，如果只需要实现post方法，那么 就只需要在类中实现post(self,request,*args,**kwargs)。
  ```

- views.py

  - ```
    from django.views import View
    class ArticleIndexView(View):
        def get(self,request,aid):
            params = request.GET.get('name')
            return HttpResponse('这是get方法-斜杠参数：{}，问号参数：{}'.format(aid,params))
    
        def post(self,request):
            name = request.POST.get('name')
            return HttpResponse('这是post方法-{}'.format(name))
    
        def http_method_not_allowed(self, request, *args, **kwargs):
            return HttpResponse('您的请求方式为{}，只允许为get和post'.format(request.method))
    ```

- urls.py

  - ```
    urlpatterns = [
        path('', views.ArticleIndexView.as_view(), name='index'),  #这里是post请求
        path('<int:aid>',views.ArticleIndexView.as_view(),name='index'), #这里是get请求
        ]
    ```

#### TemplateView 

- ```
  django.views.generic.base.TemplateView，这个类视图是专门用来返回模版的。在这个类中，有两个属性是经常需要用到的，一个是template_name，这个属性是用来存储模版的路径，TemplateView会自动的渲染这个变量指向的模版。另外一个是get_context_data，这个方法是用来返回上下文数据的，也就是在给模版传的参数的
  ```

- 有两种方式来应用模板类

  - 第一种：直接指定路由‘xxx/’去对应模板about.html（不需要写模板视图类）

    - ```
      urlpatterns = [	path('about/',TemplateView.as_view(template_name='about.html')),  #直接指定路由about/对应模板about.html（不需要写模板视图类）
      ]
      ```

  - 第二种：写模板视图类

    - views.py

      - ```
        from django.views.generic import TemplateView
        class Template_view(TemplateView):
            template_name = 'about2.html' #指定模板文件
        
            def get_context_data(self, **kwargs):   #这个方法作用是可以将变量传递到模板中
                context = super().get_context_data(**kwargs)
                # print(context)
                # context['username']='ddd'
                # context['pass']='ddd'
                context = {
                    'age':18,
                    'gender':'man'
                }       #这里写了字典，则上面的username和pass在模板中调用不了
                return context
        ```

    - urls.py

      - ```
        urlpatterns = [
        path('about2/',views.Template_view.as_view(template_name='about2.html'))
        ]
        ```

#### ListView

```
在网站开发中，经常会出现需要列出某个表中的一些数据作为列表展示出来。比如文章列表，图书列表等等。在 Django中可以使用ListView来帮我们快速实现这种需求。
```

- views.py

  - ```
    from django.views.generic import ListView
    class List_view(ListView):
        model = Article                     # 指定模型（所以要去创建模型）
        template_name = 'list_view.html'    # 指定模板文件
        paginate_by = 3                     # 页面中每一页显示的数据的数量（3个数据分一页）
        context_object_name = 'articles'    # 指定模型数据在模板中的参数名称（模型的数据赋给变量名为articles，然后传递到模板中去使用）
        ordering = 'create_time'            # 指定模型数据的排序方式
        page_kwarg = 'page'                 # 在页面中获取第几页的数据的参数名称，默认是page(?page=2,获取第二页)
    
        def get_context_data(self, **kwargs):  #获取上下文的数据。这个方法作用是可以将变量传递到模板中
            context = super().get_context_data(**kwargs)
            print(context)                     #这个context是字典，其中有键paginator和page_obj，分别对应着Paginator和Page类对象
            paginator = context['paginator']
            page_obj = context['page_obj']
            return context
    
        def get_queryset(self):  #提取数据库的数据
            return Article.objects.all() #提取所有数据（可以做过滤）
    
    ```

- urls.py

  - ```
    urlpatterns = [
    path('listview/',views.List_view.as_view(),name='listview')
    ]
    ```

- templates目录下list_view.html

  - ```
    <ul>
        {% for article in articles %} 这里的articles是传递过来的，数据库中的数据
        <li>{{ article }}</li>
        {% endfor %}
        <li>{{ paginator.count }}</li>
        <li>{{ paginator.num_pages }}</li>
        <li>{{ paginator.page_range }}</li>
        <br>
        <li>{{ page_obj.has_next }}</li>
        <li>{{ page_obj.has_previous }}</li>
        <li>{{ page_obj.has_other_pages }}</li>
        <li>{{ page_obj.next_page_number }}</li>
        {# <li>{{ page_obj.previous_page_number }}</li> #}
        <li>{{ page_obj.number }}</li>
        <li>{{ page_obj.start_index }}</li>
        <li>{{ page_obj.end_index }}</li>
    </ul>
    ```

##### Paginator和Page类 

https://www.cnblogs.com/donghaiming/p/11007505.html

- Paginator和Page类都是用来做分页的。他们在Django中的路径为django.core.paginator.Paginator和 

  django.core.paginator.Page。以下对这两个类的常用属性和方法做解释： 

- Paginator常用属性和方法 :

  - ```
    方法：
    	page(number)：根据参数number返回一个Page对象。（number为1的倍数）
    属性：
        count：总共有多少条数据
        num_pages：总共有多少页
        page_range：页面的区间。比如有三页，那么就range(1,4)
    ```

- Page常用属性和方法：

  - ```
    方法：
        has_next：是否还有下一页 
        has_previous：是否还有上一页
        next_page_number：下一页的页码
        previous_page_number：上一页的页码
    属性：
        number：当前页
        start_index：当前这一页的第一条数据的索引值 
        end_index：当前这一页的最后一条数据的索引值
    ```

### 通用分页小练习

- 效果图：

![image-20200429145438615](C:\Users\dujun\AppData\Roaming\Typora\typora-user-images\image-20200429145438615.png)

- 思路：

  - ```
    1、利用ListView类和Bootstrap网站来实现
    2、首先下面的分页组件去bootstrap查找并添加到模板中：https://v3.bootcss.com/components/#pagination-default
    3、页面中的数据是从数据库中提取过来的
    4、在视图和模板中完成逻辑代码
    ```

- 实现过程：

  - views.py

    - ```
      from django.views.generic import ListView
      class List_view(ListView):
          model = Article                     # 指定模型（所以要去创建模型）
          # template_name = 'list_view.html'    # 指定模板文件
          template_name = 'list_view_opt.html'    # 指定模板文件
          # paginate_by = 3                     # 页面中每一页显示的数据的数量（3个数据分一页）
          paginate_by = 1
          context_object_name = 'articles'    # 指定模型数据在模板中的参数名称（模型的数据赋给变量名为articles，然后传递到模板中去使用）
          ordering = 'create_time'            # 指定模型数据的排序方式
          page_kwarg = 'page'                 # 在页面中获取第几页的数据的参数名称，默认是page(?page=2,获取第二页)
      
          def get_context_data(self, **kwargs):  #获取上下文的数据。这个方法作用是可以将变量传递到模板中
              context = super().get_context_data(**kwargs)
              # print(context)                     #这个context是字典，其中有键paginator和page_obj，分别对应着两个对象，对象中有需要的方法
              paginator = context['paginator']
              page_obj = context['page_obj']
              page_range_data = self.get_page_range(paginator,page_obj) #向方法中传递参数并接收返回值
              context.update(page_range_data)
              return context
      
          def get_queryset(self):  #提取数据库的数据
              return Article.objects.all() #提取所有数据（可以做过滤）
      
          def get_page_range(self,paginator,page_obj,page_offset=2):   #创建一个方法来写逻辑代码（如果当前页码是5，则显示3 4 5 6 7这5个分页）
              current_page = page_obj.number        #当前页码
      
              has_left_more = False   # 一个标志位（判断什么时候在模板中加入...符号和第一个分页）
              has_right_more = False # 同上
      
              if current_page <= page_offset+1: #当前页码是否小于3
                  left_range = range(1, page_obj.number) #页码小于3则左边范围从1开始
              else:
                  has_left_more = True #标志位
                  if current_page==4: #如果当前页面为4，则标志位为False。即在模板中不添加...符号
                      has_left_more = False
                  # 3 4 5
                  left_range = range(current_page-page_offset ,page_obj.number) #左边页码范围为2，如果当前页码是5则左边为3和4
      
              if current_page >= paginator.num_pages-page_offset: #当前页码是否大于 最大页码数-2
                  right_range = range(current_page + 1, paginator.num_pages+1) #右边分页
              else: #否则 下面在模板的右边分页中添加...和最后一个分页
                  has_right_more = True #标志位
                  if current_page== paginator.num_pages-page_offset-1:
                      has_right_more = False
                  # 5 6 7
                  right_range = range(current_page+1 ,page_obj.number+page_offset+1) #右边分页范围
      
              page_range = {
                  'left_range':left_range,
                  'right_range':right_range,
                  'has_left_more':has_left_more,
                  'has_right_more':has_right_more,
              }
              return page_range #将变量传入字典中放回到context中，然后可以在模板中引用
      
      ```

  - list_view_opt.html

    - ```
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>Title</title>
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
      </head>
      <body>
          <h1>listview</h1>
      
          <ul>
              {% for article in articles %}   # 显示数据库中的数据
                  <li>{{ article.id}}-{{article.title}}</li>
              {% endfor %}
      
          </ul>
      
          <nav aria-label="Page navigation">
              <ul class="pagination">
      
              <!--  最前面的<< -->
                  {% if page_obj.has_previous %}
                      <li>
                          <a href="{% url 'listview' %}?page={{ page_obj.previous_page_number }}" aria-label="Previous">
                              <span aria-hidden="true">&laquo;</span>
                          </a>
                      </li>
                  {% else %}
                      <li class="disabled">
                          <a href="#" aria-label="Previous">
                              <span aria-hidden="true">&laquo;</span>
                          </a>
                      </li>
                  {% endif %}
      
              <!-- 中间的跳转标-->
                  {% if has_left_more %}
                      <li><a href="{%url 'listview' %}?page=1">1</a></li>
                      <li><a href="#">...</a></li>
                  {% endif %}
                  {% for left in left_range %}
                      <li><a href="{%url 'listview' %}?page={{ left }}">{{ left }}</a></li>
                  {% endfor %}
      
                  <li class="active"><a href="{%url 'listview' %}?page={{ page_obj.number }}">{{ page_obj.number }}</a></li>
      
                  {% for right in right_range %}
                      <li><a href="{%url 'listview' %}?page={{ right }}">{{ right }}</a></li>
                  {% endfor %}
      
                  {% if has_right_more %}
                      <li><a href="#">...</a></li>
                      <li><a href="{%url 'listview' %}?page={{ paginator.num_pages }}">{{ paginator.num_pages }}</a></li>
                  {% endif %}
              <!--  最后面的>>-->
                  {% if page_obj.has_next %}
                      <li >
                          <a href="{% url 'listview' %}?page={{ page_obj.next_page_number }}" aria-label="Next">
                              <span aria-hidden="true">&raquo;</span>
                          </a>
                      </li>
                  {% else %}
                      <li class="disabled">
                          <a href="#" aria-label="Next">
                              <span aria-hidden="true">&raquo;</span>
                          </a>
                      </li>
                  {% endif %}
      
              </ul>
          </nav>
      
      </body>
      </html>
      ```

### 错误处理

常用的错误码

```
404：服务器没有指定过的url
403：没有权限访问相关的数据
405：请求的method错误
400：bad request，请求的参数错误
500：服务器内部错误，一般时代码出bug
502：一般部署的时候见的比较多，一般时nginx启动了，然后uwsgi有问题
```

错误处理方式：

- 直接指定错误状态码模板文件

  - ```
    1、项目的templates文件下直接创建404.html、500.html...
    2、在settings.py中修改
    	DEBUG = False
    	ALLOWED_HOSTS = ['127.0.0.1']
    
    在访问网页时如果访问到了没有指定好的url，django中页面会自动跳转到404页面
    ```

- 专门定义一个app来处理

  - ```
    在视图中做判断从而redirect到对应的错误处理(404\500)路由下
    ```



## 表单

### 用表单验证数据

```
前端提交上来的表单数据需要做验证，表单数据验证逻辑在forms.py文件中写（解耦思想，不然都在视图函数里面写）。
Django的表单文件（forms.py）有两个作用：
1、渲染表单模板，即在表单中定义的字段在模板中渲染
2、表单文件中做数据验证（对提交上来的表单数据，在html中form标签中的数据）
```

#### 表单整体使用流程：

- 在forms.py中定义一个表单类（继承自django.forms.Form）
- 在视图中，根据GET或POST请求来做相应的操作
  - GET请求可以将表单渲染到模板中（一般不会使用的操作）
  - POST请求中去获取前端传来的form数据，传递到表单类中去做验证
- 在froms.py下的表单类中写验证逻辑代码（会牵扯到数据库信息）

#### 表单验证代码

-  views.py文件:

  - ```
    from django.shortcuts import render
    from django.http import HttpResponse
    from .froms import ArticleForm
    from django.views import View
    # django.forms.utils.ErrorDict
    from django.forms.utils import ErrorDict
    
    def index(request):
        return HttpResponse('首页')
        
    class ArticleView(View):
        def get(self,request):
            form = ArticleForm()  # 这里给表单类一个空的表单，因为这是get请求，前台不会有表单传输过来
            return render(request,'index.html',{'form':form}) #将form对象传入index.html模板中
    
        def post(self,request):
            form = ArticleForm(request.POST) # 给表单类传递一个前台提交上来的表单数据
            # print(form)           #form是网页的源代码
            if form.is_valid():     # is_valid()其实是表单数据在表单类中进行验证，全部验证通过才返回True
                telephone = form.cleaned_data.get('telephone')  #通过cleaned_data去获取验证后的telephone表单字段对应的数据
                # print(telephone)
                return HttpResponse('验证成功')
            else:
                # print(form.errors)   # 错误信息是带有标签的html代码
                # print(type(form.errors))
                print(form.errors.get_json_data())  # 以字典的形式打印错误信息
    
                return HttpResponse('验证失败')
    ```

- 模板文件index.html

  - ```
    <form action="" method="">
        <table>
            {{ form.as_table }} 			#表单渲染模板，这是在table标签中
        </table>
        <input type="submit" value="提交">
    </form>
    <!--{{ form.as_p }}-->  #可以在p标签中进行渲染
    <!--{{ form.as_ul }}--> #ul无序标签中
    ```

- forms.py

  - ```
    from django import forms
    from django.core import validators
    from .models import User
    
    
    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=10,min_length=2,error_messages={'min_length':'输入的值的最小长度为2'},label='标题')
        content = forms.CharField(widget=forms.Textarea,label='内容')
    
        email = forms.EmailField(required=False)  # EmailField已经是验证了
        # email = forms.CharField(validators=[validators.EmailValidator(message='请输入正确的邮箱')]) #和上面达到类似的效果（使用表单验证器）
    
        reply = forms.BooleanField(required=False) #required 表示这个reply字段在网页中是否一定要输入值，false为不需要输入值
        website = forms.URLField(required=False)
        # 这里只能验证手机号是否输入正确
        telephone = forms.CharField(validators=[validators.RegexValidator(r'1[3456789]\d{9}',message='请输入正确的手机号')])
        # print(telephone)
        pwd1 = forms.CharField(max_length=12)
        pwd2 = forms.CharField(max_length=12)
    
        #验证电话号码 是否 在数据库中已存在，验证一个表单字段
        def clean_telephone(self):
            telephone = self.cleaned_data.get('telephone')
            # print(telephone)
            exists = User.objects.filter(tele=telephone).exists()  #判断手机号在数据库中是否存在
            if exists:
                raise forms.ValidationError('手机号码已存在')
    
            return telephone
    
        # clean函数可以验证多个表单字段
        def clean(self):
            cleaned_data =super().clean()
    
            pwd1 = cleaned_data.get('pwd1')
            pwd2 = cleaned_data.get('pwd2')
    
            if pwd1 != pwd2:
                raise forms.ValidationError('两次密码输入不一致')
            return cleaned_data
    ```

- models.py

  - ```
    from django.db import models
    
    # Create your models here.
    
    class User(models.Model):
        username = models.CharField(max_length=10)
        password = models.CharField(max_length=10)
        tele = models.CharField(max_length=11)
    ```

- urls.py

  - ```
    from . import views
    from django.urls import path
    
    
    urlpatterns = [
        path('',views.index),
        path('article/',views.ArticleView.as_view())
    
    ]
    ```

#### ModelForm

model+form：模型表单

写表单验证时，表单类中的字段几乎都是对应着模型中的字段，当做大项目时，几百个字段时，重复在表单类下写字段就显得比较冗余。

所以有ModelForm类，直接引用model中的字段即可。表单中的其他操作（渲染模板和验证表单数据）不受影响。只是不用写那么多代码

- models.py

  - ```
    from django.db import models
    
    class Front(models.Model):
        title = models.CharField(max_length=5)
        content = models.TextField()
        author = models.CharField(max_length=5)
        create_time = models.DateTimeField(auto_now_add=True)
    ```

- forms.py

  - ```
    from django.forms import Form,ModelForm
    from django import forms
    from .models import Front
    
    class FrontForm(ModelForm): # 注意：这里是ModelForm
        author = forms.IntegerField()  #这里还是可以自己定义表单字段
        class Meta:
            model = Front
            fields = '__all__'  #引用model中的所有字段
            # fields = ['title']  # 只引用title字段
            # exclude = ['title'] # 引用除了title字段以外的其他字段
    
            error_messages = {    # 由于引用了model字段，不能在字段里面写错误信息，故通过这个方式
                'title':{     #指定title字段
                    'max_length':'最大长度为5个字符' #错误信息
                }
            }
    ```

### 文件图片上传

- 思路

  - ```
    1、在模板template中定义好上传的接口(form标签，form标签需要指定属性enctype，input类型是file)
    2、在模型model中写好对应的字段，字段类型也是对应的FileField和ImageField
    3、表单form中使用ModelForm
    4、在视图view中将前端上传上来的文件或图片对象传入表单类中，做表单验证
    5、验证成功后考虑将文件/图片保存在哪个目录下（可以在settings.py指定目录，也可以使用模型的字段中up_load='xxx'参数来指定存放目录）
    ```

- ![image-20200430155847721](C:\Users\dujun\AppData\Roaming\Typora\typora-user-images\image-20200430155847721.png)

- 代码如下：

  - 在模板template中定义好接口

    - ```
      <form action="" method="post" enctype="multipart/form-data">
          文件上传：<input type="file" value="文件" name="file"><br>
          图片上传：<input type="file" value="图片" name="image"><br>
          <input type="submit" value="上传">
      </form>
      ```

  - 在模型中定义对应的类

    - ```
      class FileModel(models.Model):
          # upload_to 指定上传上来的文件的目录
          # file = models.FileField(upload_to='files')  #这里指定的路径是目录，如果settings.py中已经配置了MEDIA_ROOT，那么上传上来的文件将会保存在MEDIA_ROOT指定的目录下的files目录下
          file = models.FileField(upload_to='%Y/%m/%d',validators=[validators.FileExtensionValidator(['txt','pdf'])])
      
          image = models.ImageField(upload_to='%Y/%m/%d',null=True)
      ```

  - 模型中可以指定文件保存的目录，也可以保存在settings.py配置好的目录下（常用）

    - ```
      MEDIA_ROOT = os.path.join(BASE_DIR,'media')
      MEDIA_URL = '/media/'
      ```

  - 表单验证

    - ```
      class FileForm(ModelForm):
          class Meta:
              model = FileModel
              fields = '__all__'
      
              error_messages = {
                  'file':{'invalid_extension':'只允许传入txt和pdf格式的文件'}
              }
      ```

  - 视图任务：接收前端文件/图片数据，然后把文件/图片保存到目录中，添加到数据库记录中

    - ```
      from django.shortcuts import render
      from django.http import HttpResponse
      from django.views import View
      from .models import FileModel
      from .forms import FileForm
      
      
      def index(request):
          return HttpResponse('首页')
      
      
      class File_upload(View):
          def get(self,request):
              return render(request,'file_upload.html') #模板文件
      
          def post(self,request):
              file_form = FileForm(request.POST,request.FILES) #给表单类传递数据
      
              # with open('django.jpg','wb') as f: #将上传上来的文件直接保存在当前目录下
              #     f.write(file.read())
      
              # 上传成功之后需要将上传上来的文件保存下载，并在数据库中做记录
              if file_form.is_valid():  #做表单验证
                  file = request.FILES.get('file')  #获取上传上来的文件
                  image = request.FILES.get('image') #获取上传上来的图片
                  FileModel.objects.create(file=file,image=image) # 上传上来的文件保存到数据库指定的目录
                  return HttpResponse('上传成功')
              else:
                  print(file_form.errors.get_json_data()) #打印错误信息
                  return HttpResponse('fail')
      ```


## session和cookie

Django上操作

```
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware,now


def cs(request):
    response = HttpResponse('cookies—session')
    # response.delete_cookie('username')
    # response.set_cookie(key='username',value='ddd',max_age=60,expires=make_aware(datetime(year=2020,month=5,day=3,hour=14)))
    # response.set_cookie(key='username',value='ddd',max_age=60,expires=now())

    # request.session['pass'] = '123'
    # request.session['word'] = 'hhh'
    # p = request.session.get('word')
    # p = request.session['pass']
    # p = request.session.pop('pass')
    # p = request.session.keys()
    # p = request.session.items()
    # request.session.clear()
    # request.session.flush()
    # p = request.session.get('word')
    # request.session.set_expiry(-1)
    # request.session.clear_expired()
    # print(p)
    return response


def get_cs(request):
    cookie = request.COOKIES
    print(cookie)
    cookie_dict = {key:value for key,value in cookie.items()}
    print(cookie_dict)
    print(cookie.get('username'))
    username = cookie.get('username')
    return HttpResponse(username)

```

## memcached

Memcached是一个高性能的分布式的内存对象缓存系统

https://www.cnblogs.com/wayne173/p/5652034.html 

特性：

```
1.保存内存中 
2.重启服务，数据会丢失 
3.LRU算法，根据最近使用的变量，将长时间没有使用的变量删除 
4.memcache服务端是不安全的， 
5.不适合单机使用，对内存的消耗比较大 
6.格式简单，不支持list数据格式
```

操作和redis差不多

缺点：

```
安全性的问题，memcached的操作不需要任何用户名和密码，只需要知道memcached服务器的ip地址和端口号即可。因此 memcached使用的时候尤其要注意他的安全性
```

在Django中使用memcached

settings.py

```
CACHES = { 'default': { 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache', 'LOCATION': '127.0.0.1:11211',}}
```

views.py

```
from django.core.cache import cache 
def index(request): 
	cache.set('abc','juran',60) 
	print(cache.get('abc')) 
	response = HttpResponse('index') 
	return response
```


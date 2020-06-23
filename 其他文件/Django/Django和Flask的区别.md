# Django和Flask的区别

django中的app相当于flask中的蓝图

django中有专门的urls.py文件来进行路由的映射

flask则是在蓝图中定义好路由后，在项目入口py文件中进行注册

## 模板引擎:

```
django使用DTL模板引擎
falsk使用jinja2模板引擎
不过用法差不多，应该就语法上有些不一样
```



渲染模板上的区别：

```
django：render(request,'xxx.html',context = context)
flask:render_template('xxx.html',**context)
在模板中可以用{{}}和.方式引用
```


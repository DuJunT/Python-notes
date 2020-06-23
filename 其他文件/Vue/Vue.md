## Vue模板语法

### 视图更新注意事项

1、直接修改数组中的值 不会触发视图更新

```
this.books[0] ='xxx' #这种不行
```

2、动态添加对象属性

```
this.books.title='xxx' #这种不行
```

通过Vue.set

```
Vue.set(this.books,0,xxx)
Vue.set(this.books,'title','xxx')
```

## 事件的绑定

通过v-on

$event 参数 获取原生的DOM事件



###  双向绑定v-model



### 计算属性

```
v-model:value='xxx'
computed:{
	xxx:function(){
		自己的业务逻辑
	}
}
```

### set

计算属性默认只有get，如果有set方法那必须有get

```
v-model:value='xxx'

computed:{
	set:function(){},
	get:function(){}
}
```

#### 监听属性

```
v-model:value='xxx'
watch:{
	xxx:function(新值,旧值){}
}
```



### 表单input输入绑定

1、text 文本

2、textarea 文本域

3、checkbox 复选框

4、radio 单选框

5、select 下拉框

### 修饰符

```
.lazy	延迟同步
.trim	去收尾空格
.number 自动将用户输入类型变成数值类型
```



## 自定义组件

### 自定义组件定义

```
<组件的名字></组件的名字>
Vue.component('组件的名字',{
	template:'组件的模板',
	data:function(){
		return {
			xxx
		}
	}
})
```

### 给组件添加属性

```
<组件的名字></组件的名字>
Vue.component('组件的名字',{
	props:['属性的名字'],
	template:'组件的模板',
	data:function(){
		return {
			xxx
		}
	}
})
```

### 单一根元素

组件中的模板，只能在一个标签中

### 事件的传递

```
this.$emit('方法的名字','参数')
```

### 自定义组件v-model

````
model:{
	prop:xxx,
	event:xxx
}
````

### 插槽

```
<slot></slot>
```

### 插槽的命名

```
<slot name='xxx' v-bind:navs='navs'></slot>

<template v-slot:xxx='xxxx'>
{{xxxx.navs}}
```



### 生命周期函数

- 创建期间
- 运行期间
- 销毁期间



## 过滤器

```
Vue.filter('过滤器名字',function(value){})

{{username|过滤器的名字}}
{{username|过滤器1|过滤器2}}
```

## 图书管理系统的案例

```
JSON.stringify  转成字符串
JSON.parse 转成JS认识的代码
JSON.parse(JSON.stringify(xxxx))
bootstrap  前端样式组件

filter	数组中的过滤
filter(function(item){
	return true/false
})
```

## Vue-Router路由

路由的基本使用

```
<router-link to='/'>首页<router-link>

<router-view><router-view>

var 模板名字 = Vue.extend(template:'xxx')
var router = new VueRouter({
	routes:[
		#path 路径
		{path:'路径',component:'模板名字'}
	]
})

new Vue({
	router:router   //第一个router是关键字，第二个router是上面代码的router
})
```

### 动态路由

```#
<router-link to='路径/参数'><router-link>
<router-view><router-view>

var 模板名字 = Vue.extend(template:'xxx {{route.paras.参数}}')

var router = new VueRouter({
	routes:[
		{path:路径/:参数,component:'模板名字'}
	]
})

new Vue({
	el:'',
	router:router
})
```

### 错误页面

```
var notfound = Vue.extend({template:<p>not found</p>})
var profile = Vue.extend({
		template:<p>个人中心{{$route.params.userid}}</p>,
        mounted(){       
        	if(this.$route.params.userid!=123){  #这里是错误判断
        	this.router.replace('/404')			#这里是错误跳转，跳转到404页面
        	}
        }
		})
var router = new VueRouter({
	routes:[
		{path:'/404',component:notfound},		# 404页面
		{path:'profile/:userid',component:profile}
	]
})
```

### 嵌套路由

```
var setting = Vue.extend({template:'<p>setting</p>'})
var message = Vue.extend({template:'<p>message</p>'})
var user = Vue.extend(
        {
            template:`
            <div>
                <h1>个人中心</h1>
                <ul class="nav nav-tabs">
                    <li role="presentation" class="active">
                        <router-link to='/user/123/setting'>设置</router-link> #嵌套路由
                    </li>
                    <li role="presentation">
                        <router-link to='/user/123/message'>消息</router-link>
                    </li>
                </ul>
                <div class='container'>
                    <router-view></router-view>   #在定义好的路由中如果嵌套路由，需要给定一个出口
                </div>
            </div> 
            `
        })
        
var router = new VueRouter({
        routes:[
            {path:'/',component:index},
            {
                path:'/user/:userid',
                component:user,
                children:[         #直接在路由的定义下添加children属性
                    {path:'setting',component:setting},
                    {path:'message',component:message},
                ]            
            },
        ]
    })
```

### 编程式导航

使用<router-link>可以在用户点击的情况下跳转链接，还有一种方式是使用js代码修改页面的跳转方式，这时候就要使用到编程式导航

```
在html中指定跳转按钮
然后在Vue对象中定义对应的methods方法
在对应的methods方法中使用对应的跳转方式
var router= new VueRouter({
        routes:[
            {path:'/',component:index},
            {path:'/profile/:userid',component:profile,name:'myprofile'},
            {path:'/login',component:login},
        ]
    })
    
new Vue({
        el:"#app",
        methods:{
            index:function(){
                this.$router.push('/')    // 跳转到对应的 / 的路径
            },
            profile:function(){
                // this.$router.push('/profile/123')
                this.$router.push({name:'myprofile',params:{userid:"djt"}})  //这个name需要对应VueRouter其中的一个path
            },
            login(){
                this.$router.push({path:'login',query:{wd:'python'}})    //在url以添加?wd=python的形式
            },
            prev(){
                this.$router.go(-1)    //网页浏览记录会记录在history栈中，-1代表步数，向后退一步
            },
            next(){
                this.$router.go(1)
            }
        },
        router:router
    })
```

### 命名路由

```
可以对路由进行命名
{path: "/user/:userid", component: user,name:'User'}
在<router-link>中调用
<router-link v-bind:to="{name:'User',params:{userid:123}}">中心{{$route.params.userid}}</router-link>
```

### 命名视图

```
对于<router-view>来说：
可以在一个html->body标签中添加多个<router-view>标签而且还可以命名，来提供视图
<div id="app">
        <div class='header'>
            <router-view name='header'></router-view>
        </div>
        <div class='body'>
            <router-view name='left'></router-view>
            <router-view name='right'></router-view>
        </div>
        <div class='footer'>
            <router-view name='footer'></router-view>
        </div>
        
</div>
var headerc = Vue.extend({template:'<h1>header_view内容</h1>'})
    var leftc = Vue.extend({template:'<h1>left_view内容</h1>'})
    var rightc = Vue.extend({template:'<h1>right_view内容</h1>'})
    var footerc = Vue.extend({template:'<h1>footer_view内容</h1>'})
var router = new VueRouter({
        routes:[
            {
                path:'/',
                components:{     //这里是有s的  components
                    header:headerc,    //header为<router-view>中的name，headerc为对应的模板
                    left:leftc,		
                    right:rightc,
                    footer:footerc,
                }
            }
        ]
    })

```




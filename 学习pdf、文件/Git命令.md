## 初始化

```
git init
```

## 指定管理文件

```
git add xxx.xxx
```

## 生成版本

```
git commit -m '描述信息'
```

## 查看信息

- 查看管理目录下的文件状态

  ```
  git status
  ```

- 查看版本信息

  ```
  git log
  ```


 ## 回滚

```
git reset --hard 版本号
git reflog
```

## 分支

查看分支情况

```
git branch
```

创建分支

```
git branch xxx
```

切换分支

```
git checkout xxx
```

分支合并

```
git merge xxx(要合并的分支名字)
```

删除分支

```
git branch -d xxx
```

## 使用Git Hub托管代码

### 家—Git Hub—公司

Git Hub：创建仓库

公司：git上给仓库起别名

```
git remote add origin(别名) 远程仓库地址
```

公司：向远程仓库推代码

```
git push -u origin(别名) master(分支名)
```

家：克隆远程仓库代码

```
git clone 远程仓库地址
```

```
克隆解释：https://www.cnblogs.com/bluestorm/p/7380141.html
```

家：拉代码

```
git pull origin（别名） dev(分支名)
```



## 多人协同开发

Git Hub创建组织（multiworker）

创建仓库(test1)

创建本地目录和项目并推送上仓库

```
mkdir 项目目录
git init
touch xxx
git add .
git commit -m 'xxx'  # xxx为注释如：'第一次提交'
git remote origin 仓库地址
git push origin master
```

给版本打标签

```
git rag -a v1 -m 'xxx'
git push origin --tag
```



### 邀请成员

创建dev分支并推送到Github

```
git branch dev
git checkout -b dev
git push origin dev
```

到项目中邀请成员并给权限

成员A 在自己本地开发

```
mkdir xxx
git clone xxxxx
giat checkout -b ddz(假设这里开发斗地主功能)
touch ddz.py
git add .
git push origin ddz
```

对应仓库的管理员去Git Hub建立Branch规则

成员A开发完成之后可以进入到Git Hub中去合并ddz到dev中（也可以使用git合并），这样在Git Hub中，组织中的管理员就可以在Git Hub中去进行code review。

项目中还需要测试分支去测试dev功能，测试完成后才把dev合并到master中



### 代码review

- team leader在Git Hub上创建规则
- 成员 pull request
- team leader 去检查代码并用Git Hub 进行合并
- 拉去dev分支下面的最新代码



### 多人协同开发之测试上线

```
git checkout -b release		#创建release分支
```

也可以测试人员拉取代码到本地测试



## Git补充

配置文件

- 项目配置文件（只对当前项目）
  - .git/config
- 全局配置文件（对所有项目）
  - ~/.gitconfig

- 系统配置文件（对电脑上所有用户）
  - /etc/gitconfig



### 免密登录

- URL

  ```
  https://用户名:密码@github.com/xxx/xxx.git
  ```

- SSH

### Git忽略文件

创建.gitignore文件

在里面填写对应要忽略的文件类型

```
*.h		#点.h解为的文件都不管理
!a.h 	#除了a.h类型以外的文件
dir/	#忽略dir目录
```



### 项目的文件

issue ：文档以及任务管理

wiki：项目的介绍文件
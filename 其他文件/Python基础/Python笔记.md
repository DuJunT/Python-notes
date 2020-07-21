# Python笔记

## 教程：https://www.liaoxuefeng.com/wiki/1016959663602400

## 内置函数：https://docs.python.org/3/library/functions.html

## 官方库：https://pypi.org/

## Python基础

### 数据类型和变量

#### 整数

#### 浮点数

- 即小数，之所以叫浮点数是因为按照科学计数法表示时，一个浮点数的小数点位置是可变的
- 1.23e10与12.3e9一样结果

#### 字符串

#### 布尔值

#### 空值

#### 变量

- 除法 
  - /：取全部
  - //：取整数部分
  - %：取余数

### 字符串和编码

- 编码：数字/字符编程字节的过程
- 解码：字节变成数字/字符的过程

编码方式历史进程：

- 一开始是ASCII，由美国发明
- 接下来到各国的编码方式：中国GB2312、日本Shift_JIS、韩国Euc-kr
- 为了统一各个国家的编码方式，Unicode编码方式诞生
- 为了解决Unicode占用存储空间太大和传输不方便的问题
- UTF-8诞生
- ......

编码方式解释：https://www.zhihu.com/question/52346583/answer/977492415

![image-20200717184859482](C:\Users\dujun\AppData\Roaming\Typora\typora-user-images\image-20200717184859482.png)

![image-20200717184910019](C:\Users\dujun\AppData\Roaming\Typora\typora-user-images\image-20200717184910019.png)

- ord()函数
  - 获取字符的整数表示
  - 获取字符对应的编码的编码号
  - ord('A')   ----65
- chr()
  - 把编码数字转换成对应的字符形式
  - chr(65)-----A

### list和tuple

#### list

- 有序的集合，可以随时添加和删除其中的元素
- 可变的有序表
- append(obj)：添加元素
- extend(obj)：添加元素，会将obj遍历一次才添加到列表中
- insert(index,obj)
- pop(index)

#### tuple

- 有序列表，元组

- 不可变有序列表

- 因为是不可变，所以代码更安全，如果可能，就尽量用tuple代替list

- 注意点：t = (1)这个输出是为1，为不是(1)

  - 因为这里会有歧义，会认为()是括号来的而不是代表元组，所以需要加逗号
  - t = (1,)


### 条件判断

- if...elif...else
- round(x [, n])
  - **round()** 方法返回浮点数x的四舍五入值
  - n为保留小数个数

### 循环

- for...in循环

- while循环

- break语句，直接退出循环

  - ```	
    n = 1
    while n <= 100:
        if n > 10: # 当n = 11时，条件满足，执行break语句
            break # break语句会结束当前循环
        print(n)
        n = n + 1
    print('END')
    ```

- continue语句可以提前结束本轮循环

  - ```
    n = 0
    while n < 10:
        n = n + 1
        if n % 2 == 0: # 如果n是偶数，执行continue语句
            continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
        print(n)
    ```

### dict和set

#### dict

- key-value形式存储，key为不可变对象
- in方法判断对象是否存在key中
  - d = {'tom':18,'cat':11}
  - 'tom' in d
- get(key)方法获取指定的value，返回值为value，没有对应的key则返回None
- pop(key)删除指定的key和value，返回值为value，没有对应的key则报错
- keys()
- values()
- items()

#### set

- set和dict类似，也是一组key的集合，但不存储value，key也不能重复，也为不可变对象

- 要创建一个set，需要提供一个list作为输入集合：

  - ```
    s = set([5,2,3])
    ```

- set中的元素不重复，重复元素会自动过滤

  - ```
    s = set([1,1,2,3,3,4])
    print(s)
    {1,2,3,4}
    ```

- add(key)添加元素

- remove(key)删除元素

- set可以看成数学意义上的无序和无重复的集合，所以两个set可以做数学意义上的交集、并集

  - ```
    s1 = set([1, 2, 3])
    s2 = set([2, 3, 4])
    print(s1 & s2)   # {2，3}
    print(s1 | s2)	#{1，2，3，4}
    ```

## 函数

函数就是最基本的一种代码抽象的方式

### 内置函数

- https://docs.python.org/3/library/functions.html

### 调用函数

- int()

- float()

- str()

- bool()

- ......

- 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个"别名"

  - ```
    a = abs	#变量a指向abs函数
    print(a(-1)) # 1,所以也可以通过a调用abs函数
    ```

### 定义函数

- 函数名+参数+返回值
- 空函数：pass
- 如果有必要，可以先对参数的数据类型做检查
- 函数体内部可以用return随时返回函数的结果，没有return语句时，会自动return None
- 函数可以同时返回多个值，但其实就是一个tuple

### 函数的参数

- 必须参数（位置参数）、默认参数、可变参数（*args）、关键字参数（**kw）、命名关键字参数
- 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

- Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数
- 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误
- 要注意定义可变参数和关键字参数的语法
  - *args是可变参数，args接收的是一个tuple
  - **kw是关键字参数，kw接收的是一个dict
- 以及调用函数时如何传入可变参数和关键字参数的语法
  - 可变参数既可以直接传入：func(1,2,3)，又可以先组装list或tuple，再通过*args方式传入：
    - tuple = (1,2,3)
    - func(\*tuple)
  - 关键字参数既可以：func(a=1,b=2)，也可以先组装dict，再通过**kw方式传入：
    - dict = {'a':1,'b':2}    
    - func(\*\*dict)
- 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法
- 命名的关键字参数是为了限制调用者传入的参数名，同时可以提供默认值
- 定义命名的关键字参数再没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数

### 递归函数

- 使用递归函数的有点是逻辑简单清晰，缺点是过深的调用是导致栈溢出

- 针对尾递归优化的语言可以通过尾递归防止栈溢出。

- 尾递归事实上适合循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

- Python 标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

- 练习：汉诺塔的移动

  - 请编写`move(n, a, b, c)`函数，它接收参数`n`，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法

  - ```
    def move(n, a, b, c):
        if n == 1:
            print(a, '-->', c)
        else:
            move(n-1, a, c, b)	#把前n-1块从柱子A移至柱子B
            print(a, '-->', c)	#把最大块从柱子A移至柱子C
            move(n-1, b, a, c)	#把前n-1块从柱子B移至柱子C
          
    move(3, 'A', 'B', 'C')
    #输入：
    A --> C
    A --> B
    C --> B
    A --> C
    B --> A
    B --> C
    A --> C
    ```

## 高级特性

一行代码能解决的事情，绝不写5行代码，代码越少，开发效率越高

### 切片

- slice切片操作

- 去空格函数

  - strip([char])：收尾去除char，不填则去除空格

    - ```
      str = '000123456000'
      str.strip('0') #收尾去除0
      # '123456'
      ```

    - ```
      str = "123abcrunoob321"
      print (str.strip( '12' ))  # 字符序列为 12
      # 3abcrunoob3,从结果来看 去除的12字符不分顺序
      ```

  - ltrip()

  - rtrip()

- 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的`strip()`方法：

  - ```
    def trim(s):
        while(s[:1] == ' '):
                s = s[1:]
        while(s[-1:] == ' '):
                s = s[:-1]
        return s
    s = '  hello'
    print(s[:1])
    # 测试:
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')
    ```

### 迭代

- 使用for循环去遍历可迭代对象

- 判断对象是否是可迭代对象

  - ```
    from collections.abs import Iterable
    print(isinstance('abc',Iterable))  # True
    print(isinstance(123,Iterable))		# False
    print(isinstance([1,2,3],Iterable)) # True
    ```

- 想通过for循环获取list的下标，使用内置函数enumerate

  - ```
    for index,value in enumerate(['a','b','c'])
    	print(index,value)
    # 0 a
    # 1 b
    # 2 c
    ```

- for循环同时引用两个变量

  - ```
    dict = {'a':1, 'b':2, 'c':3}
    for x,y in dict.items():
    	print(x,y)
    # a 1
    # b 2 
    # c 3
    ```

- 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

  - 解题思路：

    - 一开始我没有去认真看题目的需求和认真分析
    - 其实就按结果导向思路来解题最好
    - 题目说只要最大值和最小值，就不要去搞什么排序操作（下面第一种方法就排了序），其实就定义两个变量去接收就好了
    - 做题目之前应该先列出所有参数的可能性，然后围绕这些列出的需要传入的参数去解题
      - 例如：这里是传递L，即可迭代对象，就以list为例，列出空列表，列表中只有一个元素，列表中只有两个元素甚至是多个元素的可能性，然后围绕这些可能性去写答案（即下面代码中先写出测试的内容，然后围绕测试的内容去写答案）

  - ```
    # 第一种：未使用for循环，使用while
    # def findMinAndMax(L):
    #     if L == []:
    #         return (None, None)
    #     if len(L) == 1:
    #         return (L[0],L[0])
    #     n = 0
    #     m = 0
    #     while m < len(L)-1:
    #         if L[n] > L[n+1]:
    #             L[n],L[n+1] = L[n+1],L[n]
    #         n += 1 
    #         m += 1 
    #     return (L[0], L[-1])
    
    #第二种：只使用for循环就可以解决
    def findMinAndMax(L):
        if len(L) == 0:
            return (None, None)
        min = L[0]
        max = L[0]
    
        for i in L:
            if i > max:
                max = i
            if i < min:
                min = i
    
        return (min, max)
    
    # 测试
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')
    ```

### 列表生成式

- 单层循环

  - ```
    [x * x for x in range(1, 11)]
    ```

- 两层循环

  - ```
    [m + n for m in 'ABC' for n in 'XYZ']
    ```

- if...else

  - ```
    [x for x in range(1, 11) if x % 2 == 0]
    ```

  - 错误写法：

    - ```
      [x if x % 2 == 0 for x in range(1, 11)]
      ```

- for循环前面是一个表达式，而后面是一个筛选条件

  - 所以在列表生成式for循环前面使用if语句的话要加上else
  - for循环后面则为筛选条件，使用if不能加上else

- 练习：

  - 请修改列表生成式，通过添加`if`语句保证列表生成式能正确地执行：

  - ```
    L1 = ['Hello', 'World', 18, 'Apple', None]
    
    # 答案----------------------------
    L2 = [i.lower() for i in L1 if isinstance(i,str)]
    # --------------------------------
    
    # 测试:
    print(L2)
    if L2 == ['hello', 'world', 'apple']:
        print('测试通过!')
    else:
        print('测试失败!')
    ```

### 生成器

- 生成器是一种快速完成迭代器功能的工具
- 生成器是根据某种算法边循环边计算的一种机制

- generator其中两种创建方式

  - 把一个列表生成式[]改为()，就创建了一个generator

    - ```
      L = [x * x for x in range(10)]	# L为list
      g = (x * x for x in range(10))  # g为generator
      ```

  - 在函数的定义中包含yield关键字即可，普通函数就变为generator

    - ```
      def fib(max):  # 斐波那契数列
          n, a, b = 0, 0, 1
          while n < max:
              yield b
              a, b = b, a + b
              n = n + 1
          return 'done'
      ```

- 获取generator中的值

  - next(generator对象)
  - for循环遍历generator对象

- 获取generator中的返回值

  - 通过捕获StopIteration错误，返回值包含在StopIteration中的value里

    ```
    f = fib(6)   # 斐波那契数列对象
    while True:
        try:
            x = next(f)
            print(x)
        except StopIteration as e:
            print(e.value)
            break
    ```

- 练习：杨辉三角

  - ![image-20200719175610008](C:\Users\dujun\AppData\Roaming\Typora\typora-user-images\image-20200719175610008.png)

  - 把每一行看做一个list，试写一个generator，不断输出下一行的list：

  - ```
    # 答案-----------------------------
    def triangles():
    	s = [1]
        while True:
            yield s
            l = []
            sum = 0
            for i in s:
                l.append(sum+i)
                sum = i
            l.append(s[len(s)-1])
            s = l
    # ---------------------------------
    
    
    # 期待输出:
    # [1]
    # [1, 1]
    # [1, 2, 1]
    # [1, 3, 3, 1]
    # [1, 4, 6, 4, 1]
    # [1, 5, 10, 10, 5, 1]
    # [1, 6, 15, 20, 15, 6, 1]
    # [1, 7, 21, 35, 35, 21, 7, 1]
    # [1, 8, 28, 56, 70, 56, 28, 8, 1]
    # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    n = 0
    results = []
    for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break
    
    for t in results:
        print(t)
    
    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!')
    ```

### 迭代器

- 凡是可作用于for循环的对象都是Iterable类型

- 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列

- 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数把Iterable对象变成Iterator对象

- Python的for循环本质上就是通过不断调用next()函数实现的

  - ```
    for x in [1,2,3,4]
    	pass
    ```

  - 上面等价于下面

  - ```
    # 首先获得Iterator对象
    it = iter([1,2,3,4])
    # 循环
    while True:
    	try:
    		# 获得下一个值
    		x = next(it)
    	except StopIteration:
    		# 遇到StopIteration就退出循环
    		break
    ```

## 函数式编程

https://www.liaoxuefeng.com/wiki/1016959663602400/1017328525009056

### 高阶函数

- 变量可以指向函数

  - 以abs()函数为例

  - ```
    f = abs
    f(-10)
    # 10
    ```

- 函数名也是变量

  - 函数名是什么？函数名其实就是指向函数的变量

  - 以abs()为例，完全可以把函数名abs堪称变量，它指向一个可以计算绝对值的函数

  - 如果把abs指向其他对象

    - ```
      abs = 10
      abs(-10)
      # 会报错，因为abs变量指向了整数10，此时abs不是指向计算绝对值的函数
      # 要恢复abs函数，需要重启Python交互环境
      ```

    - 由于`abs`函数实际上是定义在`import builtins`模块中的，所以要让修改`abs`变量的指向在其它模块也生效，要用`import builtins; builtins.abs = 10`。

- 传入函数

  - 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

  - 简单的高阶函数

    - ```
      def add(a,b,f)
      	return f(a) + f(b)
      
      a = -5
      b = 6
      f = abs
      result = add(a,b,f)
      print(result)
      # 11
      ```


### map/reduce

- map()参数：

  - 第一个是函数
  - 第二个是Iterable对象
  - map是内置函数，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

- reduce()参数：

  - 第一个：函数
  - 第二个：Iterable对象
  - reduce需要导入，reduce把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，把累积后的结果作为返回值

- 练习：

  - 利用map和reduce编写一个str2float函数，把字符串‘123.456’转换成浮点数123.456

  - 最快的方法是用float()函数把字符串转为浮点数，但要探究，就不能用这个方法

  - ```
    from functools import reduce
    DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
    # 字符转化为数字
    def char2num(s):
    	retrn DIGITS[s]
    	
    # 字符串转化为整数
    def str2int(s):
    	return reduce(lambda x,y:x*10+y,map(char2num,s))
    
    # 字符串转化为浮点数
    def str2float(s):
        L = s.split('.')
        return reduce(lambda x,y:x*10+y,map(char2num,L[0])) + reduce(lambda x,y:x*10+y,map(char2num,L[1]))/(10**len(L[1]))
    ```

### fliter

- 内置函数

- filter()接受一个函数和一个序列，返回值是一个Iterator，也就是一个惰性序列

- 和map()不同点在于，filter()虽然也是把传入的函数依次作用在每个元素，但是根据函数的返回值是否是True还是False来决定保留还是丢弃该元素（即filter()会自动对参数一函数的返回值进行bool判断，是True则留下，False丢弃）

- 例子：

  - 判断列表的元素是否是基数，基数则留下，偶数则删除

  - ```
    def is_odd(n):
    	return n%2 == 1
    list(filter(is_odd,[1,2,3,4,5,6,7]))
    # [1,3,5,7]
    ```

  - 把一个序列中的空字符串删掉

  - ```
    def not_empty(s):
    	return s and s.strip()
    
    list(filter(not_empty,['AB',' ',None,'C']))
    # ['AB','C']
    ```

- 练习：用filter求素数（埃式筛法）

  - ```
    # 构造一个从3开始的奇数序列
    def _odd_iter():
    	n = 1
    	while True:
    		n += 2
    		yield n
    
    # 筛选函数
    def _not_divisible(n):
    	return lambda x: x % n > 0
    
    # 定义一个生成器，不断返回下一个素数
    def primes():
    	yield 2
    	it = _odd_oter()  #初始序列
    	while True:
    		n = next(it)
    		yield n 
    		it = filter(_not_divisible(n),it)
    ```

- 练习：用filter筛选出回数

  - 算法一：

    - ```
      def is_palindrome(n):
          s = str(n)
          if len(s) == 1:
              return 1
          if len(s)%2 == 0:
             return s[:len(s)//2] == s[len(s)//2:]
          return s[:len(s)//2] == s[(len(s)//2)+1:]
          
      # 测试:
      output = filter(is_palindrome, range(1, 1000))
      print('1~1000:', list(output))
      if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
          print('测试成功!')
      else:
          print('测试失败!')
      ```

  - 算法二：

    - ```
      def is_palindrome(n):
      	s = str(n)
      	l = len(s)+1
      	for i in range(l//2):
      		if s[i] != s[-i-1]
      			return False
      	return True
      	
      # 测试:
      output = filter(is_palindrome, range(1, 1000))
      print('1~1000:', list(output))
      if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
          print('测试成功!')
      else:
          print('测试失败!')
      ```

### sorted

- sorted(iterable, key=None, reverse=False)参数：

  - 第一个参数为可迭代对象
  - 第二个参数key可以接收一个函数，然后作用在第一个参数的每个元素上，再进行大小比较（整数就比较数字大小，字符串则比较Ascii的大小）
  - reverse默认从小到大排序，True则为从大到小

- 练习

  - 假设我们用一组tuple表示学生名字和成绩：使用sorted()对列表分别按名字和姓名排序

  - ```
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    
    # 对名字进行排序，名字是字符串即通过Ascii的大小比较
    def by_name(t):
        return t[0]
    L2 = sorted(L, key=by_name)
    print(L2)
    
    # 对成绩以倒序方式排序
    def by_score(t):
        return -t[1]	# 这里添加"-"号的效果和在sorted函数中添加reverse=True效果一样
    L3 = sorted(L, key=by_score)
    print(L3)
    ```

### 返回函数（闭包讲解）

https://www.liaoxuefeng.com/wiki/1016959663602400/1017434209254976

- 1、高阶函数除了可以接收函数作为参数外，还可以把函数作为结果值返回

- 2、在一个函数(外部函数)中又定义了一个函数（内部函数），内部函数可以引用外部函数的参数和局部变量，当外部函数返回内部函数时，相关参数和变量都保存在返回的内部函数中，这种程序结构称为”闭包“

- 3、注意：返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量（可以使用可变类型的数据例如list）

- 4、如果一定要引用循环遍历，方法就是在创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何修改，已绑定到函数参数的值不变

- 练习：利用闭包返回一个计数器函数，每次调用它返回递增整数

  - 下面代码闭包的返回值不能使用整数类型，因为整数是不可变数据类型(修改值的话，内存地址也会发生改变)（笔记第3点），而是使用list（可变），这样修改list中的value，对应的id也不会发生改变

  - ```
    def createCounter():
        n = [0]
        def counter():
            n[0] = n[0]+1
            return n[0]
        return counter
    
    # 测试:
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
    ```

### 匿名函数

- 匿名函数：没有函数名，只是一个函数对象

- 由于匿名函数是只是一个函数对象，没有函数名，所以不用担心函数名冲突问题，此外还可以将匿名函数赋值给一个变量，再利用变量来调用函数

- 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果

  ```
  lambda x:  x*x   # 参数可以有多个
  相当于
  def f(x):
      return x * x
  ```

### 装饰器

- 在代码运行期间动态增加功能的方式，称之为装饰器

- 本质上，decorator就是一个返回函数的高阶函数

- 通过functools.wrap()把原始函数的\__name__等属性复制到wrapper()函数中，否则有些依赖函数签名的代码执行就会报错

- 不带参数的decorator

  - ```
    import functools
    
    def log(func):
        @functools.wraps(func)  # 把原始函数的__name__等属性复制到wrapper()函数中，否则有些依赖函数签名的代码执行就会报错
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
    ```

- 带参数的decorator

  - ```
    import functools
    
    def log(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    ```

- 练习1：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

  - ```
    import time, functools
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            start_time = time.time()
            tmp = fn(*args, **kw)
            end_time = time.time()
            print('%s executed in %s ms' % (fn.__name__, end_time - start_time))
            return tmp
        return wrapper
    
    # 测试
    @metric
    def fast(x, y):
        time.sleep(0.0012)
        return x + y;
    
    @metric
    def slow(x, y, z):
        time.sleep(0.1234)
        return x * y * z;
    
    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')
    ```

- 练习2：请编写一个decorator，能在函数调用的前后打印出`'begin call'`和`'end call'`的日志，写出一个@log的decorator，使它即支持

  - ```
    @log
    def f():
        pass
    ```

  - 又支持

  - ```
    @log('execute')
    def f():
        pass
    ```

  - ```
    import functools,time
    def log(text):   # 注意这里的text，当不传入参数时，text相当于传入的函数名
        if isinstance(text,str):
            def decorator(fn):
                @functools.wraps(fn)
                def wrapper(*args, **kw):
                    print('begin call %s' % fn.__name__)
                    tmp = fn(*args, **kw)
                    print('end call %s' % fn.__name__)
                    return tmp
                return wrapper
            return decorator
    
        @functools.wraps(text)  #注意这里的text，当不传入参数时，text相当于传入的函数名
        def wrapper(*args, **kw):
            print('begin call %s' % text.__name__)
            tmp = text(*args, **kw)
            print('end call %s' % text.__name__)
            return tmp
        return wrapper
        
    
    # 测试
    @log
    def f():
        print('f')
    f()
    
    print('------------------------')
    
    @log('im')
    def f1():
        print('f1')
    f1()
    ```


### 偏函数

- 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单

  - ```
    def int2(x ,base=2):
        return int(x, base)
    print(int2('1000000'))
    ```

  - ```
    import functools
    int2 = functools.partial(int,base=2) # partial()函数固定base参数
    print(int2('10000000'))
    ```

## 模块

- 模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用
- 创建自己的模块时，要注意：
  - 模块名要遵循Python变量命名规范，不要使用中文、特殊符号
  - 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，内置模块：https://docs.python.org/3/library/functions.html
- 包：为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包
  - ![image-20200721151416816](C:\Users\dujun\AppData\Roaming\Typora\typora-user-images\image-20200721151416816.png)
  - 文件www.py的模块名是mycompany.web.www，web下的\_\_init\_\_.py必须要创建（包的结构），可以不写内容，\_\_init\_\_.py本身也是一个模块，它的模块名是mycompany.web（即web的模块名为\_\_init.py\_\_的模块名）

### 使用模块

- import xxx

- from xxx import xxx

- 类似\_xxx和\_\_xxx这样的函数或变量就是非公开的(private)，不应该被直接引用（不应该不是不能）

- private函数或变量的作用

  - ```
    def _private_1(name):
        return 'Hello, %s' % name
    
    def _private_2(name):
        return 'Hi, %s' % name
    
    def greeting(name):
        if len(name) > 3:
            return _private_1(name)
        else:
            return _private_2(name)
    ```

  - 在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数就不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public

### 安装第三方模块

- https://www.liaoxuefeng.com/wiki/1016959663602400/1017493741106496

- 推荐使用Anaconda，一个基于Python的数据处理和科学计算平台，其已经内置了许多非常有用的第三方库

## 面向对象编程

- 面向对象编程-object Oriented Programming，简称OOP，是一种程序设计思想
- OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数
- 面向过程于面向对象的程序设计：
  - 面向过程的程序设计是把计算机程序视为一系列命令的集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度
  - 面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递
- 在Python中所有数据类型都可以视为对象，也可以自定义对象。自定义的对象数据类型就是面向对象中的类(Class)的概念
- 采用面向对象的程序设计思想，首先思考的不是程序的执行流程，而是将待处理的数据视为一个对象，去思考对象中有哪些属性，可以有哪个方法
- 面向对象的设计思考是抽象出Class，根据Class创建instance
- 一个Class既包含数据，又包含操作数据的方法
- 面向对象的三大特点：封装、继承、多态

### 类和实例

- 面向对象最重要的概念是类和实例，类是抽象的模板，而实例是根据类创建出来的一个个具体的"对象"，各个实例拥有的数据都相互独立，互不影响；

- 方法就是于实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据

- 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节

- 数据封装：

  - ```
    class Student(object):
    
        def __init__(self, name, score):
            self.name = name
            self.score = score
    
        def print_score(self):  # 类的方法，将数据封装起来
            print('%s: %s' % (self.name, self.score))
    ```

  - 通过类的方法将数据封装起来，外部调用Student对象的实例的print_score方法很容易，但是不知道该方法内部的逻辑和数据。起到一个封装作用。

### 访问限制

- 关于下划线：https://zhuanlan.zhihu.com/p/105783765?utm_source=com.miui.notes

- 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的如咋逻辑

- 为了不让内部属性被外部访问，可以在属性的名称前添加\_\_两条下划线，实例的变量如果以\_\_开头，就变成了一个私有属性，只有内部可以访问，而外部不可以访问（实际上还是可以访问的，下面会说）

  - ```
    class Student(object):
    
        def __init__(self, name, score):
            self.__name = name
            self.__score = score
    
        def print_score(self):
            print('%s: %s' % (self.__name, self.__score))
    ```

  - ```
    s = Student('tom',80)
    print(s.__name)  # 会报错
    print(s._Student__name)  #这种方法可以访问到私有属性
    ```

- Python中，有些变量名是\_\_xxx\_\_的，这种是特殊变量，不是private，外部是可以直接访问的

- 有些是\_xxx这种一个下划线的变量，外部是可以直接访问的，但是，按照约定俗成的规定，当看到这种变量时，意思是："虽然我可以被访问，但是，请把我视为私有变量，不要随意访问我"

- 私有属性“\_\_name”在类中定义的时候，Python解释器会对外把\_\_name变量改成_Classname__name，所以外部还是可以通过“ 实例名.\_Classname\_\_name”的方式去访问私有属性

- 如果外部代码要获取私有属性的值和修改私有属性的值的话，我们可以在类中增加get方法和set方法（也可以用装饰器@property把方法变成属性用于调用），外部可以通过函数去调用或修改属性

  - ```
    class Student(object):
        def __init__(self, name, gender):
            self.name = name
            self.__gender = gender
    
        def get_gender(self):
            return self.__gender
        
        def set_gender(self, gender):
            if not isinstance(gender,str):
                raise 'TypeError'
            self.__gender = gender
    
    # 测试:
    bart = Student('Bart', 'male')
    if bart.get_gender() != 'male':
        print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            print('测试成功!')
    ```

### 继承和多态

- 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
- 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的
- https://www.liaoxuefeng.com/wiki/1016959663602400/1017497232674368

### 获取对象信息

- type()
  - 使用type()判断对象类型，基本类型都可以用type()判断

  - 判断函数使用types()，这个函数不是builtin的，需要import types

  - ```
    >>> import types
    >>> def fn():
    ...     pass
    ...
    >>> type(fn)==types.FunctionType
    True
    >>> type(abs)==types.BuiltinFunctionType
    True
    >>> type(lambda x: x)==types.LambdaType
    True
    >>> type((x for x in range(10)))==types.GeneratorType
    True
    ```

- isinstance()

  - 对于class的继承关系来说，使用type()就很不方便。要判断class的类型，可以使用isinstance()函数

  - ```
    class Animal(object):
    	def run(self):
    		print('Animal is runing...')
    
    class Dog(Animal):
    	def run(self):
    		print('little dog is running...')
    a = Animal()
    d = Dog()
    print(isinstance(a,Animal))  # True
    print(isinstance(d,Animal))  # True
    ```

  - instance()还可以判断一个变量是否是某些类型中的一种

  - ```
    isinstance([1, 2, 3], (list, tuple))
    ```

- dir()

  - 要获取一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list

    - ```
      dir('ABC')  #获取str对象的所有属性和方法
      # ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
      ```

  - 当使用len()函数去获取对象的长度时，其实内部是调用了\_\_len\_\_()这个特殊方法，所以我们也可以自己在class中重写这个方法（类似的其他内置函数道理也一样）

  - 获取class内的数据，还有getattr()、setattr()、hasattr()函数

    - ```
      class MyObject(object):
      	def __init__(self):
      		self.x = 9
      	def power(self):
      		return self.x * self.x
      obj = MyObject()
      
      print(hasattr(obj,'x'))  # True
      print(hasattr(obj,'y'))	 # False
      setattr(obj,'y',19)
      print(hasattr(obj, 'y')) # True
      print(getattr(obj, 'y')) # 19
      ```

    - getattr()试图获取不存在的属性时会报错，可以指定默认的返回值

      - ```
        getattr(obj,'z',404)  #若obj对象中没有z属性，则返回404
        ```

### 类属性和实例属性

- 类属性可以通过“类名.属性名”方式或“实例对象.属性名”调用
- 不要对实例属性和类属性使用相同的名字，实例属性优先级比类属性高，所以当类属性名和实例属性名相同时，外部调用时会调用实例属性
- 实例属性属于各个实例所有，互不干扰
- 类属性属于类所有，所有实例共享一个属性

## 面向对象高级编程

- 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。
- 我们会讨论多重继承、定制类、元类等概念。

### 使用\_\_slots\_\_

- 正常情况下，我们可以给创建的class绑定属性或方法

  - 绑定属性有两种，第一种是创建实例化对象后绑定，另一种是直接类名.属性名绑定类属性

  - 绑定方法同样有两种情况

    - 1、实例化对象后，给对象绑定方法，不过只有此实例化对象可以使用该方法，另一个实例却不可以用

      - ```
        >>>	class Student(object):
        ... 	pass
        >>> def set_age(self, age): # 定义一个函数作为实例方法
        ...     self.age = age
        ...
        >>> from types import MethodType
        >>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
        >>> s.set_age(25) # 调用实例方法
        >>> s.age # 测试结果
        25
        
        >>> s2 = Student() # 创建新的实例
        >>> s2.set_age(25) # 尝试调用方法
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        AttributeError: 'Student' object has no attribute 'set_age'
        ```

    - 2、为了给所有实例都绑定方法，可以给class绑定方法：

      - ```
        >>> def set_score(self, score):
        ...     self.score = score
        ...
        >>> Student.set_score = set_score
        ```

- 使用\_\_slots\_\_限定实例的属性（类属性不限制），规定实例只可以绑定哪些属性

  - ```
    class Student(object):
        __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
    ```

  - 使用`__slots__`要注意，`__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的，不过子类中也可以定义\_\_slots\_\_，这样的话子类实例允许定义的属性就是自身的\_\_slots\_\_加上父类的\_\_slots\_\_

### 使用@property

- 为了让外部使用类中的属性而不将真实属性名暴露出去，可以使用get()方法和set()或者使用@property装饰器

- ```
  class Student(object):
  
      def get_score(self):
           return self._score
  
      def set_score(self, value):
          if not isinstance(value, int):
              raise ValueError('score must be an integer!')
          if value < 0 or value > 100:
              raise ValueError('score must between 0 ~ 100!')
          self._score = value
  ```

- ```
  class Student(object):
  
      @property
      def score(self):
          return self._score
  
      @score.setter
      def score(self, value):
          if not isinstance(value, int):
              raise ValueError('score must be an integer!')
          if value < 0 or value > 100:
              raise ValueError('score must between 0 ~ 100!')
          self._score = value
  ```

- ```
  >>> s = Student()
  >>> s.score = 60 # OK，实际转化为s.set_score(60)
  >>> s.score # OK，实际转化为s.get_score()
  60
  >>> s.score = 9999
  Traceback (most recent call last):
    ...
  ValueError: score must between 0 ~ 100!
  ```
# BOSS面试题目

## 1、你好.笔试试题“

- 小明有一些气球想挂在墙上装饰，他希望相同颜色的气球不要挂在一起，写一个算法帮他得出一种可行的挂气球方式，自行定义函数，输入和返回，如果无法做到相同颜色的气球不挂在一起，请定义合适的异常方式返回”

- 你这边给我邮箱发简历及试题答案做好之后回传给我.我的邮箱是huangxiaofang@guanmai.cn 谢谢

- ```
  def balloon_arrange(data):
      # 获取气球总数
      total = 0
      for i in data.values():
          total = total + i
      # 气球颜色最多的数量
      sort_balloon = sorted(data.items(), key=lambda x:x[1], reverse=True)
      max_count = sort_balloon[0][1]
      if max_count > (total + 1) // 2:
          return "无法做到相同颜色的气球不挂在一起"
  
      res = []
      list = [None] * total
      for k, count in sort_balloon:
          res.extend(k * count)
      if max_count == (total + 1) // 2:
          list[::2], list[1::2] = res[:(total + 1) // 2], res[(total + 1) // 2:]
      else:
          list[::2], list[1::2] = res[total // 2:], res[:total // 2]
          return "-".join(list)
  
  data = {'r': 2, 'b': 4, 'w': 1, }
  print(balloon_arrange(data))
  
  ```

- ```x
  cmp() 函数
  cmp(x,y)函数用于比较2个对象，如果x<y返回-1，x==y返回0，x>y返回1
  ```

- ```
  extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
  ```

- ```
  sorted()函数对所有可迭代的对象进行排序操作，返回值是一个新的list，不在原来的对象上进行操作
  sort()函数是应用在list上的方法，对已存在的列表进行操作，无返回值
  
  sorted(iterable, cmp=None, key=None, reverse=False)
  
  iterable--可迭代对象
  cmp--比较的函数
  	>>> L=[('b',2),('a',1),('c',3),('d',4)]
  	>>> sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))
  key--主要是用来进行比较的元素
  	>>> L=[('b',2),('a',1),('c',3),('d',4)]
  	>>> sorted(L, key=lambda x:x[1])
  	
  >>> students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
  >>> sorted(students, key=lambda s: s[2],reverse=False)            # 按年龄升序排序
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
  ```


## 2、Python开发工程师063002

你的简历已经通过了我们的初筛，这个岗位是需要现场做一套笔试题哒，笔试范围如下：
考试范围：Python基本功和基本原理，重点考察运算符、装饰器、垃圾回收机制、代码规范、各种数据类型、生成器的原理和实现，以及线程、进程、协程等的概念和应用；计算机基础，重点考察数据结构和算法分析，数据结构中可能会在链表、哈希表、堆栈、二叉树中选择一种。算法分析则会先描述一段算法，再要求进行时间复杂度分析。
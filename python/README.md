# 学习笔记

## 数据类型
int
float
bool(True/False)
string
None

int和float没有上限的限制
(超过上限会表示为inf(无限大))

## 字符串
"abc"
'abc'
r'abc"""bbb\n\taaa'
'''abc,
def
ghi'''


## 运算
除法
10/3=3.3333...
触法 整除(地板除)
10//3=3

余数
10%3=1

## 逻辑运算
and/or/not

## 字符与对应的数字编码之间的转换
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'

## 编码与转换
print("abc".encode('ascii'))
print("中文".encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

## 内容长度
print(len("abc"))	#3
print(len("中文"))	#2
print(len("中文".encode('utf-8')))	#6

## 文本输出
print("abc%sdef%daaa" % ("中文", 999))	#格式化

print("rate:%.1f%%" % ((85-72)/100))	#格式化
所有的类型都可以通过`%s`来输出，会被自动转化为字符串

## list
```python
l = ["a", "b", "c"]
print(l,len(l),l[1],l[-1])
l.append("d")
print(l)
l.insert(1,"ab")
print(l)
print(l.pop())
print(l)
print(l.pop(1))
print(l)
l[1]="abc"
print(l)
l.insert(-1, [1, 2, 3])
print(l, l[-2][1])

l = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(l[0][0],l[1][1],l[2][2])

```

## tuple

就是const的list，一旦初始化好就不能改变了。

```python
l = (1, 2, 3)
//l[1] = 4 // 报错
l = (1, 2, [3, 4])
l[2][0] = 5 // 没有问题，因为修改的是列表的内容，tuple内的内容的地址指针没有变化
l[2][1] = 6
```

## if/elif/else

```python
a = input("input age:")
a = int(a)
if a > 50:
    print(">50")
elif a > 25:
    print(">25")
else:
    print("<=25")
```

## for循环

```python
print(range(5))
for i in list(range(5)):
    print(i)
for a,b in [(1, 'A'), (2, 'B'), (3, 'C')]:
    print(a, b)
for k, v in enumerate(['A', 'B', 'C']): # 特殊遍历
    print("%s=>%s" % (k, v))
```

## while循环

```python
n = 100
while n > 0:
    print(n)
    n -= 10
```

## dict

dict的key是不可变的
```python
d={"a":"aaa","b":"bbb","c":"ccc"}
d["d"] = "ddd"
print(d["a"])
# print(d["e"])
print("d" in d, "e" in d)
d["d"] = 998
print(d.get("d"), d.get("e"))
print(d.pop("d"))
print(d)
```

### tuple和list做key(set同dict)
```python
a={"a":(1,2), (1,2):"bbb"}
print(a)
# b=[3,4] # 报错:unhashable type: 'list'
# a[b] = "bbb"
# print(a)
c=(1,2)
a[c]="ccc"
print(a)
d=(2,3)
a[d]="ddd"
print(a)
# e=(3,4,[5,6]) # 报错:unhashable type: 'list'
# a[e]="eee"
# print(a)
for k, v in enumerate(['A', 'B', 'C']): # 特殊遍历
    print("%s=>%s" % (k, v))
```

## set

```python
s = set([1, 2, 2, 3, 3])
print(s)
s.add(4)
s.add(4)
print(s)
print(s.pop())
print(s.pop())
print(s)
print(s.remove(3))
print(s)
# s.remove(2) # 没有这个值的话就会报错
print(s)
s1 = set((2,3,4))
print(s1)
s2 = s1 & s
print(s2)
print(s1 | s)
print(3 in s1)
print(1 in s1)
```

## 不可变对象

对象的方法不会改变对象本身，而会创建新的对象返回，这样的对象就是不可变对象

```python
a="abc"
print(a)
b=a.replace("b","d")
print(a,b)
```

## 函数

### 基本使用方法

```python
print(abs(-1))
# print(abs("a")) # TypeError: bad operand type for abs(): 'str'
# print(abs(2, 3)) # TypeError: abs() takes exactly one argument (2 given)
a = abs
print(a(-999))
```

### 函数定义与使用
```python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-100))
print(my_abs(100))

def tmp():  # 空函数
    pass    # 在没有想清楚怎么写的使用用，占位，保证程序可以正常运行
tmp()

if age >= 18:
    pass    # 这样写也不会出错

def my_abs(x):
    if not isinstance(x, (int, float)): # 限制传入的参数的类型
        raise TypeError('bat operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs("abc"))
```

```python
import math

def test(a, b, c):
    return (-b+math.sqrt(math.pow(b, 2) - 4*a * c))/ (2*a), (-b-math.sqrt(math.pow(b, 2) - 4*a * c)) / (2*a)

print(test(2,3,1))
print(test(1,3,-4))
```

### 多返回

多返回的本质是返回一个tuple(省略括号)
接收多返回的结果的参数要么是一个(tuple),
要么是和返回值个数相等的参数,
如果不足则会报错,超出也会报错
```python
def test():
    return 1, 2, 3
print(test())
x = test()
# a, b = test() # ValueError: too many values to unpack (expected 2)
c, d, e = test()
print(x, c, d, e)
```

### 默认参数

1. 默认参数必须在必选参数前
2. 变化大的参数在前,变化小的参数在后
3. 默认参数必须指向不变对象

#### 基本用法
```python
def my_pow(x, n = 2):
    r = 1
    while (n > 0):
        r *= x
        n -= 1
    return r

print(my_pow(3))
print(my_pow(3,3))
```

#### 指定默认参数用法
```python
def def_args(a, b = 1, c = 2):
    print("a=%d, b=%d, c=%d" % (a, b, c))

def_args(1)
def_args(1,2)
def_args(1, 2, 3)
def_args(1, c=3)
def_args(1, c=3, b=2)
```

#### 默认参数本身必须不可变

- 会出问题的地方
```python
def def_args_attention(l=[]):
    l.append("END")
    return l

print(def_args_attention([1, 2, 3]))    # [1, 2, 3, 'END']
print(def_args_attention([]))   # ['END']
print(def_args_attention([]))   # ['END']
print(def_args_attention())   # ['END']
print(def_args_attention()) # ['END', 'END']
```
函数内改变默认参数的值会导致默认参数在下次调用也会变化

- 修改方法
```python
def def_args_attention(l=None):
    if not l:
        l = []
    l.append("END")
    return l
```
这样就不会出现上面的问题了。

==我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象(多线程不需要枷锁，安全，使用不容易出现BUG)==

### 可变参数(参数的个数可变不定)

值在参数前增加`*`即可,
python会将对应的参数转化为tuple

```python
# 传统写法
def sum1(numbers):
    s = 0
    for i in numbers:
        s += i
    return s
print(sum1([1,2,3]))

# 可变参数写法
def sum2(*numbers):
    s = 0
    for i in numbers:
        s += i
    return s
print(sum2(1,2,3))
print(sum2(*[1,2,3]))
print(sum2(*(1,2,3)))
```

### 关键字参数(将多个没有声明的参数统一成一个字典传到函数中)

这里的传值是复制传值，改变参数不会影响到原始的数据

```python
def test_key_word_argument(a, b, **kw):
    print("a=%s,b=%s,kw=%s" % (a, b, kw))
test_key_word_argument(1, 2)
test_key_word_argument(1, 2, c="ccc", d="ddd")
test_key_word_argument(1, 2, **{"c": "ccc", "d":"ddd"})
```

### 命名关键字参数

参数名固定，不准许像关键字参数一样自定义参数名

```python
def test_assignment_key_word_argument(a, b, *, c="ccc", d):
    print(a,b,c,d)

test_assignment_key_word_argument(1, 2, d="ddd")
test_assignment_key_word_argument(1, 2, d="ddd", c="999")
```

### 参数组合

必选参数、默认参数、可变参数、关键字参数、命名关键字参数
除了可变参数无法和命名关键字参数组合外，其他都可以混合

#### 参数定义顺序
只能是:
必选参数,默认参数,可变参数/命名关键字参数,关键字参数

实例:
```python
def f1(a, b, c=0, *args, **kw):
    print("a=%s,b=%s,c=%s,args=%s,kw=%s" % (a, b, c, args, kw))

def f2(a, b, c=0, *, d, **kw):
    print("a=%s,b=%s,c=%s,d=%s,kw=%s" % (a, b, c, d, kw))

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f1(*(1,2,3,4), **{'d':99,'x':'#'})

f2(1,2,d=99,ext=None)
f2(*(1,2,3),**{'d':88,'x':'#'})
```

### 递归

```python
fact_num = 15

# 普通递归
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(fact(fact_num))

# 尾调用递归(python没有做尾调用优化，所以无效)
def fact_ex(n, res = 1):
    if n <= 1:
        return res
    return fact_ex(n-1, n*res)

print(fact_ex(fact_num))
```

尾调用:在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现溢出的情况

## 切片

### 使用范围
- 数组
- tuple
- 字符串

### 切片参数:
- 首个索引
- 结尾索引(不包含这个元素)
- step(默认是1)

### 注意
`l1=l[:]`可以直接复制一个数组，修改一个不会导致另一个发生变化
`l1=l`实际是引用，修改一个会导致另一个数组发生变化

### 例子
```python
l = list(range(5))
print(l)
print(l[2:3])
print(l[:3])
print(l[2:])
print(l[2:-1])
l1 = l[2:3]
l1[0] = 999
print(l1)
print(l)
print(l[::2])
l1 = l
l1[0] = 999
print(l)
print(l1)
l1 = l[:]
l1[0]=1
print(l)
print(l1)
```

### 迭代

```python
l = list(range(5))
for i in l:
    print(i)

m = {"a":"aaa", "b":"bbb", "c":"ccc"}
for k in m:
    print(k)
for v in m.values():
    print(v)
for k, v in m.items():
    print(k,v)
    
for ch in "abcd":
    print(ch)
```

判断是否是某个类型的实例
```python
from collections import Iterable

print(isinstance(["A", "B", "C"], Iterable))
```

==任何可迭代对象都可以作用于for循环，包括我们的自定义数据类型==

## 列表生成式

最终要生成的元素表达式写在最前面，后面跟上for循环表示范围

```python
import os

print([x * x for x in range(1, 11)])    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x * x for x in range(1, 11) if x % 2 == 0])  # [4, 16, 36, 64, 100]
print([m + n for m in 'ABC' for n in 'XYZ'])    # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print([d for d in os.listdir(".")]) # ['.vscode', 'test.py', 'test.pyproj', '__pycache__']
print([k+"="+v for k, v in {"a":"aaa", "b":"bbb", "c":"ccc"}.items()])  # ['a=aaa', 'b=bbb', 'c=ccc']
print([s.lower() for s in ["Hello", "WORLD"]])  # ['hello', 'world']
print([s.lower() for s in ["Hello", "WORLD", 123] if isinstance(s, str)])   # ['hello', 'world']
```

## 生成器

知道元素的算法，但因为不确定具体需要多少个元素，同时还可以节省内存

- 写法1
```python
g = (x * x for x in range(1, 11))
print("=>", g)
print("==>", next(g))
for i in g:
    print("===>", i)
```

- 写法2(通用)
```python
def fib(max):
    a, b = 0, 1
    while max:
        yield b
        a, b = b, a + b
        max -= 1
    # print('done')

f = fib(6)
print(f)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
for i in f:
    print(1, i)

for i in f: # 没有输出，上面结束了实际上这个对象就结束了，没有找到重置的方法
    print(2, i)
```

- 获取generator的返回值
需要通过捕获异常的方式获取,没有主动返回的话返回值为None
```python
def fib(max):
    a, b = 0, 1
    while max:
        yield b
        a, b = b, a + b
        max -= 1
    print('done')
    return "done1"

f = fib(6)
while True:
    try:
        print(next(f))
    except StopIteration as e:
        print("Generator return value:", e.value)
        break

def tringle(dep):
    l1 = [1]
    l2 = [1]
    yield l2
    dep -= 1
    while dep:
        l1Len = len(l1)
        for i in range(l1Len):
            if i > 0:
                l2[i] = l1[i-1] + l1[i]
            else:
                l2[i] = 1
        l2.append(1)
        yield l2
        l1 = l2[:]
        dep -= 1

t = tringle(10)
for l in t:
    print(l)
```

## 迭代

- `iterable`
    可以被for循环调用的
- `iterator`
    可以被next调用的(惰性序列)

列表生成式实际是生成一个list,所有内容都已经在内存当中了
生成器是一个算法,不知道最终结尾是什么,只能通过next来触发计算下一个树枝,所以不存在内存占用问题

```python
from collections import Iterable
from collections import Iterator

print(isinstance((x for x in range(10)), Iterable))
print(isinstance([x for x in range(10)], Iterable))
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance("ABC", Iterable))
print(isinstance(100, Iterable))

print("==========")

print(isinstance((x for x in range(10)), Iterator))
print(isinstance([x for x in range(10)], Iterator))
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance("ABC", Iterator))
print(isinstance(100, Iterator))

print("==========")

print(isinstance((x for x in range(10)), Iterator))
print(isinstance(iter([x for x in range(10)]), Iterator))
print(isinstance(iter([]), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter("ABC"), Iterator))
# print(isinstance(iter(100), Iterator))
```

## 高阶函数

高阶函数:接收另一个函数作为参数的函数

```python
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 10, abs))
```

## map

将iterable的对象的所有元素都进行操作，返回一个惰性序列

```python
def f(x):
    return x*x
a = map(f, list(range(5)))
print(a, list(a))
print(list(map(str, list(range(5)))))
```

## reduce

- 参数:
    1. 一个接收两个参数的函数,返回一个值
    2. iterator序列

- 功能:
    将列表
    `reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`

```python
from functools import reduce
def sum(x, y):
    return x + y
print(reduce(sum, list(range(5))))
def base10(x, y):
    return x * 10 + y
print(reduce(base10, list(range(5))))
```

```python
from functools import reduce
def convertCh(ch):
    return {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        }[ch]

def base10(x, y):
    return 10 * x + y

def convertStr(str):
    return reduce(base10, map(convertCh, str))

def convertStrl(str):
    return reduce(lambda x, y : 10 * x + y, map(convertCh, str))

print(convertStr("986123")+1)
print(convertStrl("986123")+1)
```

### 测试

#### 字符串格式整理
```python
l = ['adam', 'LISA', 'barT']

def fmt(str):
    return str[0].upper() + str[1:].lower()
    
print(list(map(fmt, l)))
```

### 列表求积
```python
from functools import reduce
l = [9, 8, 7]
print(reduce(lambda x, y : x * y, l))
```

### 字符串转浮点数
```python
from functools import reduce
from math import pow

def ch2int(c):
    return {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '.':'.',
        }[c]

dot = -1
def conv(x, y):
    if y == '.':
        global dot
        dot += 1
        return x
    elif dot >= 0:
        dot += 1
    return 10 * x + y
        
def str2float(s):
    return reduce(conv, map(ch2int, s)) / pow(10, dot)

print(str2float("123.345") + 1)
```

## filter

过滤掉所有返回false的元素，将剩余的重组为数组

```python
print(list(filter(lambda x : x % 2, list(range(10)))))
```

### 求素数
好神奇，可以不断的过滤
```python
def odd():
    n = 3
    yield n
    while True:
        n += 2
        yield n

def filter_divisible(n):
    return lambda x : x % n > 0

def prime():
    yield 2
    it = odd()
    while True:
        n = next(it)
        yield n
        it = filter(filter_divisible(n), it)

for i in prime():
    print(i)
    if (i > 1000):
        break
```

### 求回数
```python
def condition(x):
	s = str(x)
	for i in range(int(len(s)/2)):
		if s[i] != s[-i-1]:
			return False
	return True

o = filter(condition, range(1, 1000))
print(list(o))
```

## sorted

排序,指定排序规则(都是`<`排序),可以反转

```python
print(sorted([36,5,-12,9,-21]))
print(sorted([36,5,-12,9,-21], key=abs))
print(sorted([36,5,-12,9,-21], reverse=True))
```

## 闭包

就是返回函数的函数,同时这个函数有自己的局部变量来给返回的函数使用

闭包中的代码是在最终调用(或返回)时执行的,而不是在运行过程中

### 注意

下面的函数输出不是期望的1,4,9而是9,9,9
因为闭包只在返回的时候进行计算操作

==闭包中,返回函数不要引用循环变量或者后续可能发生变化的变量==

```python
def count():
    l = []
    for i in range(1,4):
        def f():
            return i * i
        l.append(f)
    return l
f1, f2, f3 = count()
print(f1()) // 9
print(f2()) // 9
print(f3()) // 9
```

当非要使用循环变量的时候可以像下面这样写

```python
def count():
    l = []
    for i in range(1,4):
        def f(j):
            def g():
                return j * j
            return g
        l.append(f(i))
    return l
f1, f2, f3 = count()
print(f1()) // 1
print(f2()) // 4
print(f3()) // 9
```

## 匿名函数

python的匿名函数就是一个lambda表达式
有参数和返回值,
只能是一行

```python
print(list(map(lambda x : x*x, list(range(1,10)))))
f = lambda x : x*x
print(f)
print(f(5))
def build(x, y):
    return lambda : x * x + y * y
f1 = build(10, 20)
f2 = build(10, 20)
print(f1, f2, f1 == f2)
print(f1(), f2())
```

## 装饰器

### 没有参数的装饰器

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def la():
    print("lalala")
la()
```

相当于:
`la = log(la)`

==`@functools.wraps(func)`相当于手动的`wrapper.__name__=func.__name__`==
修改`__name__`来保证函数的签名保持不变

### 有参数的装饰器

就是在没有参数的装饰器外面再包装一层

```python
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('[%s]call %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log("!!!!")
def la():
    print("lalala")
la()
```

相当于:
`la = log("!!!!")(la)`

### 练习

1. 函数调用前/后都会输出日志功能
```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("begin call:%s" % func.__name__)
        ret = func(*args, **kw)
        print("end call")
        return ret
    return wrapper

@log
def la(t):
    print("lalala:%s" % t)
    return t

a = la("aab")
print(a, la.__name__)
```

2. 同时支持有参数和没有参数

```python
import types
import functools

def log(p):
    if isinstance(p, types.FunctionType):
        @functools.wraps(p)
        def wrapper(*args, **kw):
            print("in")
            r = p(*args, **kw)
            print("out")
            return r
        return wrapper
    else:
        def decoder(f):
            @functools.wraps(f)
            def wrapper(*args, **kw):
                print("in:%s" % p)
                r = f(*args, **kw)
                print("out")
                return r
            return wrapper
        return decoder
            

@log
def la(t):
    print("lalala:%s" % t)
    return t

@log("aaa")
def la1(t):
    print("1lalala:%s" % t)
    return t

a = la(111)
print(a)
b = la1(222)
print(b)
```

## 偏函数

是用于简化函数调用的一种方式
当函数的参数太多,有很多参数不需要每次都改变时,可以使用偏函数

```python
import functools

print(int("123"))
print(int("123", base=8))
print(int("101", base=2))

int2 = functools.partial(int, base=2)
print(int2)
print(int2("101"))
print(int2("101", base=10))

max2 = functools.partial(max, 10)
print(max2(1, 5, 9))
```

## 模块

模块也叫`module`
`xxx.py`的`xxx`就是模块名
解决命名冲突用

文件夹也叫包`package`
文件夹名就是包名
文件夹内必须要有一个对应的模块文件,
统一叫:`__init__.py`(这个文件的模块名就是包名)
这个文件可以有内容,也可以是空文件

### 使用模块

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'pan'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello, world!")
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print("Too many arguments!")

if __name__ == '__main__':
    test()

```

规范说明
1. 第一行:表示运行环境
2. 第二行:编码格式
3. 第四行:是一个字符串,表示模块的文档注释,任何模块代码的第一个字符串都被视为模块的文档注释
4. 第六行:`__author__`变量表示文件的作者是xxx

## 私有`private`

没有严格的私有
已`_`开头的命名作为私有变量|函数
私有内容不应该被外部调用

## 安装第三方库

使用`pip`命令来进行安装

安装库
`pip install Pillow`

第三方库一般都会在Python官方的pypi.python.org上注册,
可以直接在上i安找到需要的库名,然后运行上面的命令安装即可

### 模块搜索路径

```python
import sys

print(sys.path)
```

输出
```
['d:\\pan\\test_python\\test\\test\\test', 'C:\\Users\\panj\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\panj\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\panj\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\panj\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\panj\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages']
```

python按照顺序搜索当前目录、内置模块、第三方模块

要添加自定义路径有两种方法

1. 直接在`sys.path`后添加(运行后失效)
    `sys.path.append('/newpath')`
2. 修改系统环境变量(持续生效,不会覆盖默认的搜索顺序)
    变量名:`PYTHONPATH`

## 面向对象

类基本测试代码
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'pan'

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def show(self):
        print("%s:%s" % (self.name, self.score))

if __name__ == '__main__':
    bart = Student("Bart Simpson", 59)
    lisa = Student("Lisa Simpson", 87)
    bart.show()
    lisa.show()
```

## 类的私有属性

`__`属性前加两个下划线表示私有变量,无法通过实例.属性名获取
**已双下划线开头和结尾的变量为系统特殊变量，可以直接访问，不是私有变量**

```python
a = Student("aa", 10)
print(a.__name)
print(a._Student__name) // 直接访问私有变量的方法,应该不会使用
```

```t
Traceback (most recent call last):
  File "d:\pan\test_python\test\test\test\test.py", line 21, in <module>
    print(a.__name)
AttributeError: 'Student' object has no attribute '__name'
```

## 继承&多态

类名后面的`()`内的内容为继承的基类,类本身为子类
`type`的返回值为类型
多态就是对象的函数调用的是对象自身的函数,如果没有实现,则调用的是基类的方法

```python
import types

class Animal(object):
    def run(self):
        print("animal run")

class Cat(Animal):
    def run(self):
        print("cat run")

class Dog(Animal):
    def run(self):
        print("dog run")

def run_twice(a):
    a.run()
    a.run()

c = Cat()
d = Dog()
c.run()
d.run()
run_twice(c)
run_twice(d)
print(type(c), isinstance(c, Animal), Animal, type(c) == Animal, type(c) == Cat)
print(type(run_twice), type(run_twice) == types.FunctionType)
```

```t
cat run
dog run
cat run
cat run
dog run
dog run
<class '__main__.Cat'> True <class '__main__.Animal'> False True
True
```

## 属性的继承

类型定义时即可设置初始值
子类会继承父类的属性值
修改类的属性值会影响所有使用这个类的初始值的对象,
但是不会影响已经手动设置过值的对象

```python
class A(object):
	a = 10

class B(A):
	pass

a = A()
b = A()
c = A()
d = B()
a.a = 20
print(a.a) # 20
print(b.a) # 10
print(c.a) # 10
print(d.a) # 10
a.a = A.a # 即使把这个值还原会初始值,他的数值也不会随类初值变化而变化
A.a = 30
print(a.a) # 20
print(b.a) # 30
print(c.a) # 30
print(d.a) # 30
```

## 类型判断`isinstance`

判断基类子类的类型，常用的数据类型的类型可以用`isinstance`这个函数
同时,这个函数还支持类型或

```python
print(isinstance((1,2,3), (list, tuple)))
print(isinstance([1,2,3], (list, tuple)))
```

```t
True
True
```

## dir函数

显示对象的所有成员(属性/方法)

```python
print(dir('ABC'))
print('ABC'.__len__(), len('ABC'))
```

```t
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
3 3
```

## 属性的存在/获取/设置函数

==用这些方法可以对任意一个python对象进行剖析,但是要注意,只有在不知道对象信息的时候,我们才会去获取对象信息==

如果可以写`sum = obj.x + obj.y`就不要写`sum = getattr(obj, 'x') + getattr(obj, 'y')`
正确的用法:

```python
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
```

- `hasattr`
    判断属性/方法是否存在
- `setattr`
    设置添加属性/方法
- `getattr`
    获取属性/方法
    当获取不存在的属性/方法时,会报错`AttributeError: 'TestObj' object has no attribute 'z'`
    可以使用默认值的方式来获取`print(getattr(t, 'z', 10))`

```python
class TestObj(object):
	def __init__(self, x):
		self.x = x
	def power(self):
		return self.x * self.x

t = TestObj(3)
print(t.power())
print(hasattr(t, 'x'))
print(getattr(t, 'x'))
print(hasattr(t, 'y'))
print(setattr(t, 'y', 10))
print(hasattr(t, 'y'))
print(getattr(t, 'y'))
print(hasattr(t, 'power'))
print(getattr(t, 'power'))
print(getattr(t, 'power')())
```

```t
9
True
3
False
None
True
10
True
<bound method TestObj.power of <__main__.TestObj object at 0x02CF5790>>
9
```

## 实例的属性和类属性

- 类的属性
    实例可以直接使用类的属性，当实例的属性被赋值后，会优先使用实例的属性，而类本身的属性并不会改变，实际使用要注意，否则会出现问题。

==推荐不要使用同名的类属性和实例属性(?我还不是很懂python的面向对象编程)==

```python
class TestObj(object):
	name = "aaa"
	def __init__(self, x):
		self.x = x
	def power(self):
		return self.x * self.x

t = TestObj(3)
print(t.name)
print(TestObj.name)
t.name="bbb"
print(t.name)
print(TestObj.name)
del t.name
print(t.name)
print(TestObj.name)
```

## 面向对象高级编程

### 使用`__slots__`

#### 函数绑定

1. 实例绑定方法

```python
from types import MethodType

class TestObj(object):
	pass

def test(self):
	print("test")

a = TestObj()
a.test = MethodType(test, a)
a.test()
```

2. 类型绑定方法

```python
from types import MethodType

class TestObj(object):
	pass

def test(self):
	print("test")

TestObj.test = MethodType(test, TestObj)
a = TestObj()
a.test()
```

#### 限定类型的属性

```python
class TestObj(object):
	__slots__ = ('name', 'age')

class TestObj2(TestObj):
	__slots__ = ('score')

a = TestObj2()
a.name = 'aaa'
a.age = 10
a.score = 99
a.rank = 999 # 报错
print(a.name, a.age, a.score)
```

#### getter/setter方法(@property)

==python中可以直接用属性名的方式调用get/set方法==

```python
class TestObj(object):
	def get_score(self):
		return self.__score
	def set_score(self, score):
		self.__score = score
	@property
	def age(self):
		print(2)
		return self.__age
	@age.setter
	def age(self, age):
		print(1)
		self.__age = age
	@property
	def name(self):
		return 10
	

a = TestObj()
a.set_score(10)
print(a.get_score())
a.age=25
print(a.age)
print(a.name) # 只读属性
```

- 例子

模拟分辨率

```python
class Screen(object):
	@property
	def width(self):
		return self.__width
	@width.setter
	def width(self, width):
		self.__width = width
	@property
	def height(self):
		return self.__height
	@height.setter
	def height(self, height):
		self.__height = height
	@property
	def resolution(self):
		return self.width * self.height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
```

### 多继承

python支持多继承,无需冗长的多重继承即可实现复杂的功能
可以理解为单一继承和多个接口的形式.
主线一般是单一继承下来的,当需要混入额外功能时,添加MixIn就可以了.
多继承的'接口'在python中叫做`MixIn`,一般在类名中有相应的表现

```python
class Test(object):
	def ta(self):
		print('ta')

class TestMixIn(object):
	def tm(self):
		print('tm')

class TestChild(Test, TestMixIn):
	pass

a = TestChild()
a.ta()
a.tm()
```

## 定制类

`__xxx__`这类命名的变量或者函数在python中是有特殊用途的
`__slots__`限制成员变量
`__len__()`是class可以作用于`len()`函数

- `__str__`提供输出的方法

```python
class Test(object):
	def __str__(self):
		return "123"

a = Test()
print(a)
```

- `__repr__`提供调试输出的方法(基本同str)

```python
class Test(object):
	def __str__(self):
		return "123"
    __repr__ = __str__
```

- `__iter__`想要被用于`for...in`循环,必须实现这个方法,返回一个迭代对象.
    python的for循环会不断调用这个迭代对象的`__next__()`方法来获取下一个值,直到
    遇到`StopIteration`错误时退出循环

```python
class Fib(object):
	def __init__(self):
		self.__a, self.__b = 0, 1 # 初始化
	def __iter__(self):
		return self
	def __next__(self):
		self.__a, self.__b = self.__b, self.__a + self.__b
		if self.__a > 1000:	# 退出循环
			raise StopIteration()
		return self.__a

for i in Fib():
	print(i)
```

- `__getitem__`像list一样获取某个对象

    - 基本获取功能
```python
class Fib(object):
	def __init__(self):
		self.__a, self.__b = 0, 1 # 初始化
	def __iter__(self):
		return self
	def __next__(self):
		self.__a, self.__b = self.__b, self.__a + self.__b
		if self.__a > 1000:	# 退出循环
			raise StopIteration()
		return self.__a
	def __getitem__(self, n):
		a, b = 1, 1
		for i in range(n):
			a, b = b, a+b
		return a

f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[10])
```

    - 支持切片的接口

```python
class Fib(object):
	def __init__(self):
		self.__a, self.__b = 0, 1 # 初始化
	def __iter__(self):
		return self
	def __next__(self):
		self.__a, self.__b = self.__b, self.__a + self.__b
		if self.__a > 1000:	# 退出循环
			raise StopIteration()
		return self.__a
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for i in range(n):
				a, b = b, a+b
			return a
		elif isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			r = []
			a, b = 1, 1
			for i in range(stop):
				if i >= start:
					r.append(i)
				a, b = b, a+b
			return r

f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[10])
print(f[:5])
print(f[3:5])
```

*还没有做切片的step处理,没有负数的处理等*
如果想像操作dict一样操作,也可以做key处理
同理还有
`__setitem__()`,`__delitem__()`

- `__getattr__()`动态的返回一个属性

只有在没有找到属性的情况下,才会调用`__getattr__`方法

```python
class Test(object):
	def __init__(self):
		self.name = 'a'
	def __getattr__(self, attr):
		if attr == 'age':
			return 99
		raise AttributeError("obj has no attribute '%s'" % attr)    # 改成这样没有找到的话就会返回一个错误

t = Test()
print(t.name)   # a
print(t.age)    # 99
print(t.score)  # None
```

==一个神奇的写法==

```python
class Chain(object):
	def __init__(self, path=""):
		self.__path = path

	def __getattr__(self, path):
		return Chain("%s/%s" % (self.__path, path))

	def __str__(self):
		return self.__path

	__repr__ = __str__

c = Chain().a.b.c.d
print(c)    # /a/b/c/d
```

- `__call__()`使实例本身可以作为方法调用

*通过函数`callable`可以判断参数对象是否可以被作为函数调用*

```python
class Test(object):
	def __init__(self, name="test"):
		self.__name = name
	def __call__(self):
		print("Test's name is '%s'" % self.__name)

t = Test("haha")
t() # Test's name is 'haha'
print(callable(t))  # True
print(callable(Test))   # True
```

## 枚举

就是正常的枚举,但是默认是从1开始
Enum可以把一组相关常量定义在一个class中,且class不可变,而且成员可以直接比较

```python
from enum import Enum

Sex = Enum("Sex", ("Male", "Female"))

print(Sex.Female, Sex.Female.value)
print(Sex.Male)
```

枚举的定制
通过继承可以使枚举从0开始
`@unique`使枚举的值不能重复

```python
from enum import Enum,unique

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

print(Weekday.Tue, Weekday.Tue.value, Weekday["Tue"])   # Weekday.Tue 2 Weekday.Tue
print(Weekday(1))   # Weekday.Mon
print(Weekday(1) == Weekday.Mon)    #True
for name, member in Weekday.__members__.items():
	print(name, "=>", member, "=", member.value)
# Sun => Weekday.Sun = 0
# Mon => Weekday.Mon = 1
# Tue => Weekday.Tue = 2
# Wed => Weekday.Wed = 3
# Thu => Weekday.Thu = 4
# Fri => Weekday.Fri = 5
# Sat => Weekday.Sat = 6
```

## 使用元类

`type()`

```python
class Hello(object):
	def hello():
		print("Hello world.")

print(type(Hello))  # <class 'type'>
print(type(Hello()))    # <class '__main__.Hello'>
print(type(Hello()) == Hello)   # True
print(isinstance(Hello(), Hello))   # True
```

类`Hello`实际是通过type函数来动态创建的

类的创建过程:
元类(metaclass)->类(class)->实例(instance)

类可以看成是元类的实例

`metaclass`

可以构建/扩展类

    - `__new__`的参数:
        1. 当前准备创建的类的对象
        2. 类的名字
        3. 类继承的父类集合
        4. 类的方法集合

```python
class HelloMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs["add"] = lambda self, value: print("add", value)
		return type.__new__(cls, name, bases, attrs)

class Hello(object, metaclass=HelloMetaclass):
	def hello(self):
		print("Hello world.")

h = Hello()
h.hello() # Hello world.
h.add("aaa") # add aaa
```

使用metaclass可以使类似`ORM`(数据库与数据结构关联,自动拼sql)一类的功能写起来更简单

## 错误/调试/测试

**函数可能抛出的异常应该在文档中说明清楚,让调用方可以清晰的处理**

### 注意点

    - `except`是从上到下依次执行的,如果异常的基类在上,子类在下,则子类永远接收不到异常
    - `try...except...else...finally`处理异常
    - `try`监听可能出现异常的代码段
    - `except`处理可能发生的异常(从上到下依次执行,并且只会执行一次)
    - `else`当`try`中没有异常时调用,在`finally`之前
    - `finally`不论是否有异常都会调用
    - `BaseException`是所有异常的基类

==异常是可以跨函数的,按照堆栈自下向上查找,指导有`try...except`为止==

### 示例代码

```python
def test():
	try:
		print("try")
		r = 1/2
		# r = 1/0 # ZeroDivisionError
		# r = 1/int("a") # ValueError
		print("try end")
	except ZeroDivisionError as e: # 出错调用
		print("except 1:", e)
	except ValueError as e: # 出错调用
		print("except 2:", e)
	else: # 没有异常调用
		print("else")
	finally: # 无论是否有异常都调用
		print("finally")
	print("END")

test()
```

### 记录错误/日志模块

logging可以配置,是否记录在文件中还是打印出来.

使用logging模块来记录错误,并继续运行程序

```python
import logging

def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar("0")
	except Exception as e:
		logging.exception(e)

main()
print("END")
```

### 自定义异常

在可以使用常规异常时,不要使用自定义异常.

```python
class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError("invalid value: %s" % s)
	return 10/n

foo("0")
```

### 连续抛出异常

有时候,当捕捉异常的函数无法处理异常时,可以继续向上级抛出异常
`raise`在没有参数时,会把当前错误原样抛出

```python
def foo(s):
	n = int(s)
	if n == 0:
		raise ValueError("invalid value: %s" % s)
	return 10/n

def bar():
	try:
		foo("0")
	except ValueError as e:
		print("ValueError")
		raise

bar()
```

在处理异常时,`except`的内容不光可以直接抛出,
只要逻辑合理,也可以将他转换成别的类型抛出

```python
try:
    10/0
except ZeroDivisionError:
    raise ValueError("Input Error!")
```

## 调试

### 日志

就是`print`出来
或者使用`logging`

设置logging的显示等级
`logging.basicConfig(level=logging.INFO)`

### 断言

如果断言条件为假,则抛出异常
`assert`可以使用`-0`关闭,如:
`python3 -0 err.py`
`assert`关闭后,可以看成是`pass`

```python
def foo(s):
	n = int(s)
	assert n != 0, "n is zero"
	return 10/n

foo("0")
```

### pdb

`pdb`就是`python`的调试器
命令行启动方法:
`python3 -m pdb err.py`

要使用高级功能的话,还是使用有调试功能的IDE吧.

#### 技能操作方法

    - `l` list,显示附近代码
    - `n` next,下一行
    - `p` print,显示某个变量
    - `q` quit,退出
    - 设置断点
        需要在代码里面设置
        `pdb.set_trace()`,运行到这里就会自动暂停
        ```python
        import pdb

        print(1)
        print(2)
        pdb.set_trace()
        print(3)
        print(4)
        ```

## 单元测试

### 测试原因

- 保证功能的可靠/完整性
- 后期重构代码时,可以根据测试结果来判断代码的完善程度

### 初始化/结束函数

- `setUp`在所有测试开始前调用,用于初始化一些测试统一需要用的东西
- `tearDown`在所有测试结束后调用,用于析构一些测试统一需要用的东西

### 测试实例

`mydict.py`

```python
# -*- coding: utf-8 -*-
class Dict(dict):
	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value
```

`mydict_test.py`

```python
# -*- coding: utf-8 -*-
import unittest

from mydict import Dict

if __name__ == "__main__":
	unittest.main()
# python -m unittest mydict_test

class TestDict(unittest.TestCase):
	def setUp(self):
		print("setUp...")

	def tearDown(self):
		print("tearDown...")

	def test_init(self):
		d = Dict(a=1, b="test")
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, "test")
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d["key"] = "value"
		self.assertEqual(d.key, "value")

	def test_attr(self):
		d = Dict()
		d.key = "value"
		self.assertTrue("key" in d)
		self.assertEqual(d["key"], "value")

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d["empty"]

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
```

控制台输出

```shell
panj@UPC2195 MINGW64 /d/pan/test_python/test/test/test
$ python -m unittest mydict_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

vscode输出

```shell
test_attr (mydict_test.TestDict) ... ok
test_attrerror (mydict_test.TestDict) ... ok
test_init (mydict_test.TestDict) ... ok
test_key (mydict_test.TestDict) ... ok
test_keyerror (mydict_test.TestDict) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```

添加setUp/tearDown后的输出

```shell
$ python -m unittest mydict_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
setUp...
tearDown...
setUp...
tearDown...
setUp...
tearDown...
setUp...
tearDown...
setUp...
tearDown...
```

## 文档测试(Doctest)

### 功能

用于生成文档,实例代码,同时也可以用于测试代码是否正确

### 示例代码

```python
# -*- coding: utf-8 -*-

import doctest

def abc(n):
	'''
	Function to get absolute value of number

	Example:
	>>> abs(1)
	1
	>>> abs(-1)
	11
	>>> abs(0)
	0
	'''
	return n if n > 0 else (-n)

doctest.testmod()
```

输出

```shell
**********************************************************************
File "d:\pan\test_python\test\test\test\test.py", line 12, in __main__.abc
Failed example:
    abs(-1)
Expected:
    11
Got:
    1
**********************************************************************
1 items had failures:
```

正常情况下输出为空,什么都没有

## IO编程

### 读文件

- 方法1

```python
try:
	f = open("a.txt", "r")
	print(f.read())
finally:
	if (f):
		f.close()
```

- 方法2

```python
with open("a.txt", "r") as f:
	print(f.read())
```

其中方法2更简洁

==`with`可以保证在最终的时候`close`掉函数,所以方法1和方法2的实际作用是完全一直的==

### file-like Object

有`read()`方法的对象就是file-like Object,像字节流等

### 二进制文件

图片,视频,二进制文件读取方法

`f = open("filePath", "rb")`

### 字符编码

默认都是用`utf-8`编码
如果需要指定编码,可以用:
`f = open("filePath", "r", encoding="gbk")`

遇到不规范编码时忽略错误:
`f = open("filePath", "r", encoding="gbk", errors="ignore")`

### 写文件

- 覆盖(创建)

```python
with open("b.txt", "w") as f:
	f.write("aabbcc")
```

- 追加

```python
with open("b.txt", "a") as f:
	f.write("aabbcc")
```

## StringIO

像操作文件一样操作string的接口

```python
from io import StringIO

f = StringIO()
f.writelines("a")
f.writelines("bb")
f.writelines("ccc")
print(f.getvalue())

f = StringIO("Hello!\nHi!\nGoodbye!")
for l in f.readlines():
	print(l.strip())
```

## BytesIO

像操作文件一样操作bytes的接口

```python
from io import BytesIO

f = BytesIO()
f.write("中文".encode("utf-8"))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
```

## 操作文件和目录

### 基本操作

```python
import os
import shutil

# print(os.name) # 系统版本
# print("env:", os.environ) # 所有环境变量
# print("path", os.environ.get("PATH")) # 获取PATH变量
# print(os.path.abspath(".")) # 当前目录绝对路径
# ndir = os.path.join("d:/pan/test_python/test/test/test", "a") # 拼接目录
# print(ndir)
# os.mkdir(ndir) # 创建目录
# ndir = os.path.join("d:/pan/test_python/test/test/test", "b", "c") # 拼接目录
# os.makedirs(ndir) # 创建路径下的所有目录
# os.rmdir(os.path.join("d:/pan/test_python/test/test/test", "a")) # 删除目录
# path1 = "/path/to/file.txt"
# path2 = "/path/to"
# print(os.path.split(path1)) # 拆分目录('/path/to', 'file.txt')
# print(os.path.split(path2)) # 拆分目录('/path', 'to')
# os.rename("a.txt", "c.txt") # 重命名
# os.remove("b.txt") # 删除文件
# shutil.copyfile("c.txt", "b.txt") # 复制文件(不在os中,不是系统函数,本质是通过读取和写文件完成的)
print([x for x in os.listdir(".") if os.path.isdir(x)]) # 输出当前目录的所有目录
print([x for x in os.listdir(".") if os.path.isfile(x)]) # 输出当前目录的所有文件
```

## 序列化

### 基本序列化功能

#### 示例

```python
import io
import pickle

d = dict(a="aaa",b="bbb")
print(d) # {'a': 'aaa', 'b': 'bbb'}

with open("a.txt", "wb") as f:
	pickle.dump(d, f)

d = None
print(d) # None

with open("a.txt", "rb") as f:
	d = pickle.load(f)
print(d) # {'a': 'aaa', 'b': 'bbb'}
```

#### 问题

只能用于python中,不通用.
不同版本的python的结果可能都不同.

### JSON序列化

#### 示例

```python
import json

d = dict(a="aaa",b="bbb",c="ccc")
j = json.dumps(d)
print(j)
t = json.loads(j)
print(t)
```

#### 通用说明

dump(s)/load(s)方法中最后的`s`是字符串的意思,
有`s`是操作字符串
没有`s`是操作有`read()`接口的文件流

#### JSON序列化/反序列化对象

```python
import json

class Person(object):
	def __init__(self):
		self.name = ""
		self.age = 0

def PersonSerialization(person):
	return {
		"name" : person.name,
		"age" : person.age,
	}

def PersonUnserialization(d):
	person = Person()
	person.name = d["name"]
	person.age = d["age"]
	return person

p = Person()
p.name = "a"
p.age = 10
s = json.dumps(p, default=PersonSerialization)
print(s)
s = json.dumps(p, default=lambda obj: obj.__dict__) # 对象一般都默认有一个dict来管理内部的数据
print(s)
n = json.loads(s, object_hook=PersonUnserialization)
print(n.name, n.age)
```

## 进程和线程

- 多进程
- 多线程
- 多进程+多线程

单进程至少包含一个线程

### 多进程

#### 普通创建进程

以下代码可以运行在bash/cmd下,不能直接在VSCode中运行

```python
from multiprocessing import Process
import os

def run_proc(name):
	print("[%s]process %s running" % (os.getpid(), name))

if __name__ == "__main__":
	p = Process(target=run_proc, args=("test",))
	print("[%s]child process will start." % os.getpid())
	p.start()
	p.join()
	print("child process end. %s" % p)
```

#### 进程池

大批量创建管理进程的方法
`join`方法会等待所有子进程执行完毕
`close`方法调用后就不能添加新的进程了
`close`方法必须在`join`方法前调用

下面代码只会同时创建4个进程,第五个进程将在先创建好的4个进程中
任意一个结束后创建.

```python
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print("Run task %s (%s)..." % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print("Task %s runs %.2f seconds." % (name, (end - start)))

if __name__ == "__main__":
	print("Parent process %s." % os.getpid())
	p = Pool(4) # 同时可以运行4个进程
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print("Waiting for all subprocesses done...")
	p.close()
	p.join()
	print("All subprocesses done.")
```

输出结果:

```t
C:\Users\panj>python d:/pan/test_python/test/test/test/test.py
Parent process 8500.
Waiting for all subprocesses done...
Run task 0 (4012)...
Run task 1 (9164)...
Run task 2 (8308)...
Run task 3 (4664)...
Task 1 runs 0.13 seconds.
Run task 4 (9164)...
Task 2 runs 1.78 seconds.
Task 4 runs 1.72 seconds.
Task 0 runs 2.44 seconds.
Task 3 runs 2.76 seconds.
All subprocesses done.
```

### 子进程

调用控制台shell命令

```python
import subprocess

print("$ nslookup www.python.org")
r = subprocess.call(["nslookup", "www.python.org"])
print("Exit code:", r)
```

### 进程间通信

以下通过`Queue`来实现进程间的通信
另外:进程间通信也可以使用`Pipes`等其他手段

```python
from multiprocessing import Process, Queue
import os, time, random

def write(q):
	print("Process to write: %s" % os.getpid())
	for v in ["A", "B", "C", "End"]:
		print("Put %s to queue..." % v)
		q.put(v)
		time.sleep(random.random())

def read(q):
	print("Process to read: %s" % os.getpid())
	v = q.get(True)
	while v != "End":
		print("Get %s from queue." % v)
		v = q.get(True)

if __name__ == "__main__":
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pr.start()
	pw.join()
	# pr.terminate()
	pr.join()
```

## 多线程

### 基本用法

`Thread()`创建
`start()`启动
`join()`等待结束

测试代码:

```python
import time, threading

def loop():
	threadName = threading.current_thread().name
	print("thread %s is running..." % threadName)
	n = 0
	while n < 5:
		n += 1
		print("thread %s >>> %s" % (threadName, n))
		time.sleep(1)
	print("thread %s ended." % threadName)

threadName = threading.current_thread().name
print("thread %s is runing" % threadName)
t = threading.Thread(target=loop, name="LoopThread")
t.start()
t.join()
print("thread %s ended." % threadName)
```

输出:

```console
C:\Users\panj>python d:/pan/test_python/test/test/test/test.py
thread MainThread is runing
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
thread MainThread ended.
```

### 多线程不加锁处理数据可能出现的问题

```python
import threading

num = 0

def change(n):
	global num
	num += n
	num -= n

def changeLoop(n):
	for i in range(100000):
		change(n)

t1 = threading.Thread(target=changeLoop, args=(5,))
t2 = threading.Thread(target=changeLoop, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(num)
```

### 加锁

加锁可以保证线程的安全,数据正确.
会影响执行效率(相当于单线程),
错误的加锁会导致卡死,进程无法结束.

```python
import threading

num = 0
lock = threading.Lock()

def change(n):
	global num
	num += n
	num -= n

def changeLoop(n):
	for i in range(100000):
		lock.acquire()
		try:
			change(n)
		finally:
			lock.release()

t1 = threading.Thread(target=changeLoop, args=(5,))
t2 = threading.Thread(target=changeLoop, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(num)
```

### 多核CPU

python中虽然是posix的线程
但是python本身有一个GIL锁,
所有的python程序都是通过获取这个锁来执行的.
所以python不论开多少线程,都是只在一个CPU核心上运行.
python的多进程中,每个进程都有一个GIL锁,所以多进程是可以利用多核心的.

所以python中的多线程并不能充分利用多核来达到高效处理的需求.

### ThreadLocal

`ThreadLocal`:就是线程自己的全局变量
解决了参数在线程中各个函数互相传递的问题

具体功能:

1. 只能访问自己线程的`ThreadLocal`变量
2. 可以像全局变量一样使用
3. 访问无需加锁

```python
import threading

threadLocal = threading.local()

def processStudent():
	d = threadLocal.student
	print("Hello, %s (in %s)" % (d, threading.current_thread().name))

def processThread(name):
	threadLocal.student = name
	processStudent()

t1 = threading.Thread(target=processThread, args=("aaa",))
t2 = threading.Thread(target=processThread, args=("bbb",))
t1.start()
t2.start()
t1.join()
t2.join()
```

## 进程vs线程

原始版本:
`Apache` 多进程(开销大)
`IIS` 多线程(不稳定)

后续版本:多进程+多线程

### 计算密集型 vs IO密集型

#### 计算密集型

适合`C`等执行高效的语言,
因为脚本运行效率底下.

#### IO密集型

适合`python`等易编码的语言,
因为性能实际是卡在IO上,而不是运算上.

### 异步IO

在python中就是协程,事件驱动

## 分布式进程

### 实例代码

注:`task_manager.py`代码无法运行,存在问题,待后续跟进

`task_manager.py`

```python
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

taskQueue = queue.Queue
resultQueue = queue.Queue

class QueueManager(BaseManager):
	pass

def GetTaskQueue():
	return taskQueue
def GetResultQueue():
	return resultQueue

if __name__ == "__main__":
	QueueManager.register("getTaskQueue", callable=GetTaskQueue)
	QueueManager.register("getResultQueue", callable=GetResultQueue)
	manager = QueueManager(address=("", 50001), authkey=b"abc")
	manager.start()

	task = manager.getTaskQueue()
	request = manager.getResultQueue()

	for i in range(10):
		n = random.randint(0, 10000)
		print("Put task %d..." % n)
		task.put(n)

	print("Try get results...")
	for i in range(10):
		r = result.get(timeout=10)
		print("Result:%s" % r)

	manager.shutdown()
	print("master exit")
```

`task_worker.py`

```python
# -*- coding: utf-8 -*-

import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass

QueueManager.register("getTaskQueue")
QueueManager.register("getRequestQueue")

serverAddr = "127.0.0.1"
print("Connect to server %s..." % serverAddr)
manager = QueueManager(address=(serverAddr, 50001), authkey=b"abc")
manager.connect()

task = manager.getTaskQueue()
request = manager.getRequestQueue()

for i in range(10):
	try:
		n = task.get(timeout=1)
		print("run task %d * %d..." % (n, n))
		r = "%d * %d = %d" % (n, n, n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print("task queue is empty")

print("worker exit.")
```

## 正则表达式

`\d`数字
`\w`字母
`\s`空白符
`.`任意字符
`+`至少一个字符
`*`没有或多个字符
`?`一个字符(或者是非贪婪匹配)
{3}三个字符
{3,5}3-5个字符
[abc]a或b或c
`|`或匹配
`^`匹配开头
`$`匹配结尾

### re模块

字符串`r"\d"`中的`r`表示这个字符串是按照正则形式写出来的,否则要达到同样效果可能需要写`"\\d"`

```python
import re

print(re.match(r"^\d{3}\-\d{3,8}$", "010-12345")) # 成功返回<_sre.SRE_Match object; span=(0, 9), match='010-12345'>,失败返回None

if re.match(r"^\d{3}\-\d{3,8}$", "010-12345"):
	print("OK")
else:
	print("FAILED)

print("a b  c".split(" ")) # ['a', 'b', '', 'c']
print(re.split(r"\s+", "a b  c")) # ['a', 'b', 'c']
print(re.split(r"[\s\,\;]+", "a,b;; c  d")) # ['a', 'b', 'c', 'd']
```

- 分组(Group)

```python
m = re.match(r"^(\d{3})\-(\d{3,8})$", "010-12345")
print(m.group(0), m.group(1), m.group(2)) # 010-12345 010 12345
```

- 贪婪匹配

默认匹配模式就是贪婪匹配
就是尽可能匹配多的字符

```python
print(re.match(r"^(\d+)(0*)$", "102300").groups()) # ('102300', '') 贪婪
print(re.match(r"^(\d+?)(0*)$", "102300").groups()) # ('1023', '00') 非贪婪
```

- 编译

如果一个正则表达式需要使用很多次,则出于效率考虑,可以对这个正则表达式进行编译.
否则每次使用都需要重新编译.

```python
reTmp = re.compile(r"^(\d{3})\-(\d{3,8})$")
print(reTmp.match("010-12345").groups()) # ('010', '12345')
print(reTmp.match("010-8086").groups()) # ('010', '8086')
```

## 常用内建模块

### datetime

处理日期和时间的标准库

datetime默认就是本地时间,设置时区后可以视为特定地区的时间
存储时间最好还是用timestamp值,因为这个值和时区无关,是一个绝对数字

常用操作

```python
from datetime import datetime

now = datetime.now() # 当前时间
print(now, type(now))
dt = datetime(2017, 10, 18, 16, 10, 31) # 创建指定时间对象
print(dt, dt.timestamp()) # 输出时间戳(UNIX秒)
t = 1508314231.0
print(datetime.fromtimestamp(t), datetime.utcfromtimestamp(t)) # 时间戳转换为时间对象
cday = datetime.strptime("2017-10-18 16:10:31", "%Y-%m-%d %H:%M:%S") # 将字符串格式化为时间对象
print(cday, cday.timestamp())
print(now.strftime("%Y,%m,%d-%H_%M_%S")) # 将时间对象转化为指定格式的字符串
```

- 时间运算

```python
from datetime import datetime, timedelta

now = datetime.now()
n = now + timedelta(hours=10)
print(n)
n = now - timedelta(days=1)
print(n)
```

#### 时区

UTC时间就是UTC+0的时间,北京时间是UTC+8时间

时区转换

```python
from datetime import datetime, timedelta, timezone

utcnow = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utcnow) # 2017-10-18 08:40:04.615409+00:00
bj_dt = utcnow.astimezone(timezone(timedelta(hours=8)))
print(bj_dt) # 2017-10-18 16:40:04.615409+08:00
tk_dt = utcnow.astimezone(timezone(timedelta(hours=9)))
print(tk_dt) # 2017-10-18 17:40:04.615409+09:00
```

### collections

内建集合模块,包含很多常用的数据结构

#### namedtuple

为了明确类型信息,但是又不需要复杂的代码定义(定义class)

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(1,2)
print(p, p.x, p.y)
print(isinstance(p, Point)) # True
print(isinstance(p, tuple)) # True
```

#### deque

在python中`list`按索引读取快,但是插入和删除慢(就是c++的vector)
deque是双向链表,链表就是访问慢,插入删除快.

```python
from collections import deque

q = deque(["a", "b", "c"])
q.append("d")
q.appendleft("e")
print(q) # deque(['e', 'a', 'b', 'c', 'd'])
print(q.pop(), q) # d deque(['e', 'a', 'b', 'c'])
print(q.popleft(), q) # e deque(['a', 'b', 'c'])
```

#### defaultdict

普通的`dict`如果`key`不存在,则抛出`KeyError`,
如果希望`key`不存在时返回一个默认值,就可以用`defaultdict`

除了`key`不存在时返回默认值外,其他功能和普通的`dict`完全一样.

```python
from collections import defaultdict

dd = defaultdict(lambda:"N/A")
dd["a"] = "aaa"
print(dd["a"]) # aaa
print(dd["b"]) # N/A
```

#### OrderedDict

使用`dict`时,`key`是无序的,我们无法确定迭代的顺序
`OrderedDict`可以使`key`迭代有序.

不是我们想象的自动按照key值排序,
而是记住了数据的插入顺序.

```python
from collections import OrderedDict

d1 = dict([("a","aaa"), ("b","bbb"), ("c","ccc")])
d2 = OrderedDict([("a","aaa"), ("b","bbb") ,("c","ccc")])
print(d1, d2)
```

#### Counter

简单的计数器
和自己简单使用的dict方法没有区别

```python
from collections import Counter

c = Counter()
for ch in "programming":
	c[ch] = c[ch] +1

print(c)
```

## Base64

`Base64`使用64个字符来表示任意二进制数据的方法,
是最常见的二进制编码方法

编码:
[a-zA-Z0-9+/]
因为标准编码可能有`+`,`/`不能出现在url中,所以可能有"url save"的`base64`编码

常用语URL,Cookie,和网页中传输少量二进制数据.

### 转换原理

将3个字节的二进制数据(3*8=24)转化成
4个字节的Base64数据(4*6=24)
6bit的数据范围是(0-63)64个字符

多余的数据用\x00在末尾补足,表示为一个或者两个`=`

### 实例代码

```python
import base64

s = base64.b64encode(b"binary\x00string")
print(s)
print(base64.b64decode(s))
```

### Struct

处理字节的数据类型
字节转换

```python
print(struct.pack(">I", 10240099)) # b'\x00\x9c@c' # `>`大端 `I`4字节无符号整形
print(struct.unpack(">IH", b"\xf0\xf0\xf0\xf0\x80\x80")) # (4042322160, 32896) # `H`2字节无符号整数
```

### hashlib

摘要算法

hashlib提供了常见的摘要算法:`MD5`,`SHA1`等

- 摘要算法大致流程:
	结果=算法函数(原始数据)

- 不同的数据有可能出现摘要结果完全一致的情况(就是碰撞)

```python
import hashlib

# MD5正常用法
md5 = hashlib.md5()
md5.update("abcdefg".encode("utf-8"))
print(md5.hexdigest()) # 7ac66c0f148de9519b8bd264312c4d64

# MD5按顺序拼接大数据的用法(和正常用法的结果是一样的)
md5 = hashlib.md5()
md5.update("abcde".encode("utf-8"))
md5.update("fg".encode("utf-8"))
print(md5.hexdigest()) # 7ac66c0f148de9519b8bd264312c4d64

# SHA1算法
sha1 = hashlib.sha1()
sha1.update("abcdefg".encode("utf-8"))
print(sha1.hexdigest()) # 2fb5e13419fc89246865e7a324f476ec624e8740
```

### itertools

提供了常见的迭代操作
它的接口的返回值一般都是Iterator,只有在循环中才会真正的计算

```python
import itertools

natuals = itertools.count() # 无限生成数字

for n in natuals:
	print(n)
	if n > 1000:
		break

cs = itertools.cycle("ABC") # 循环指定数组内容
cnt = 0
for c in cs:
	print(c)
	cnt += 1
	if cnt > 10:
		break

rp = itertools.repeat("A", 3) # 循环3次
for r in rp:
	print(r)

natuals = itertools.count()
ns = itertools.takewhile(lambda x:x <= 10, natuals) # 截取迭代器的指定范围内的数据
print(list(ns))
```

#### chain()

可以把一组迭代器串联起来,形成一个更大的迭代器

```python
for c in itertools.chain("abc", "xyz"):
	print(c)
```

```output
a
b
c
x
y
z
```

#### groupby

把迭代器中相邻的重复元素挑出来放在一起

```python
for key, group in itertools.groupby("aaabbbccaaaa"):
	print(key, list(group))
```

```output
a ['a', 'a', 'a']
b ['b', 'b', 'b']
c ['c', 'c']
a ['a', 'a', 'a', 'a']
```

## XML

1. DOM
	整体读取文件后进行解析的操作,内存大,速度慢,但是可以用树的方式任意读取
2. SAX
	边读取边解析,内存小,速度快,但是需要自己处理事件

使用SAX解析xml的示例代码:

```python
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	def start_element(self, name, attrs):
		print("sax:start_element:%s, attrs:%s" % (name, str(attrs)))

	def end_element(self, name):
		print("sax:end_element: %s" % name)

	def char_data(self, text):
		print("sax:char_data:%s" % text)

xml = r'''<?xml version="1.0"?>
<ol>
	<li><a href="/python">Python</a></li>
	<li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
```

```output
sax:start_element:ol, attrs:{}
sax:char_data:
sax:char_data:	
sax:start_element:li, attrs:{}
sax:start_element:a, attrs:{'href': '/python'}
sax:char_data:Python
sax:end_element: a
sax:end_element: li
sax:char_data:
sax:char_data:	
sax:start_element:li, attrs:{}
sax:start_element:a, attrs:{'href': '/ruby'}
```

## HTMLParser

用于解析HTML页面文件的类

## urllib

提供了一系列操作URL的功能
可以模拟浏览区执行各种操作

伪装方法:
监控浏览器发出的请求,
根据浏览器的请求头来伪装,
`User-Agent`头就是用来标识浏览器的

## 常用第三方模块

### PIL/Pillow

图像处理库
滤镜/生成验证码

### virtualenv

隔离运行环境,
为不同的应用提供不同的python运行环境

### 图形界面

- Tk
- wxWidgets
- Qt
- GTK

#### Tk

`Tk`是python自带的GUI库,无需另外安装

示例代码:

基本显示

```python
from tkinter import *

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self, text="Hello, world!")
		self.helloLabel.pack()
		self.quitButton = Button(self, text="Quit", command=self.quit)
		self.quitButton.pack()

app = Application()
app.master.title("Hello World")
app.mainloop()
```

输入框

```python
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self, text="Hello", command=self.hello)
		self.alertButton.pack()

	def hello(self):
		name = self.nameInput.get() or "world"
		messagebox.showinfo("Message", "Hello, %s" % name)

app = Application()
app.master.title("Hello World")
app.mainloop()
```

#### pack布局

- 参数:
	1. 我们使用pack函数的时候，默认先使用的放到上面，然后 依次向下排，它会给我们的组件一个自认为合适的位置和大小，这是默认方式，也是我们上面一直采用的方式。 
	2. pack函数也可以接受几个参数，side参数指定了它停靠在哪个方向，可以为LEFT,TOP,RIGHT,BOTTOM,分别代表左，上，右，下，它的fill参数可以是X,Y,BOTH和NONE,即在水平方向填充，竖直方向填充，水平和竖直方向填充和不填充。 
	3. 它的expand参数可以是YES和NO，它的anchor参数可以是N,E,S,W（这里的NESW分别表示北东南西，这里分别表示上右下左）以及他们的组合或者是CENTER（表示中间）。 
	4. 它的ipadx表示的是内边距的x方向，它的ipady表示的是内边距的y方向，padx表示的是外边距的x方向，pady表示的是外边距的y方向。

- 例子:

```python
root = Tk()
Button(root, text="A").pack(side=LEFT, expand=YES, fill = Y, anchor = NE)
```

### 网络编程

#### TCP/IP

IP是基础,是地址

IPv4是32位数:255.255.255.255
IPv6是128位数:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF

IP采用分包方式发送数据
不保证是否送达
不保证到达顺序

TCP是IP基础上的扩展,就是IP头后面加TCP数据
就是数据解析格式.
TCP保证送达数据完整
保证分包到达顺序.

HTTP,SMTP等协议都是在TCP的基础上扩展的,就是在TCP的头后面再加自己的数据.

#### TCP编程

创建socket时,可以指定使用的IP版本
IPv4:`AF_INET`
IPv6:`AF_INET6`

示例代码

客户端

```python
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(("www.sina.com.cn", 80))
# 发送数据
s.send(b"GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection:close\r\n\r\n")
# 接收数据
buffer = []
while True:
	# 每次最多接收1k字节
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
# 连接数据
data = b''.join(buffer)
# 关闭连接
s.close()
# 将header和html分开
header, html = data.split(b"\r\n\r\n", 1)
print(header.decode("utf-8"))
# 把接收到的数据写入文件
with open("sina.html", "wb") as f:
	f.write(html)
```

服务器

```python
"服务器"

import socket
import threading
import time

# 创建TCPsocket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定本机9999端口
s.bind(("127.0.0.1", 9999))
# 监听端口
s.listen(5) # 参数指定等待连接的最大数量
print("Waiting for connection...")

def tcplink(sock, addr):
	print("Accept new connection from %s:%s..." % addr)
	sock.send(b"Welcome!")
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode("utf-8") == "exit":
			break
		sock.send(("Hello, %s!" % data.decode("utf-8")).encode("utf-8"))
	sock.close()
	print("Connection from %s:%s closed." % addr)

while True:
	# 接受一个新连接
	sock, addr = s.accept()
	# 创建新线程来处理TCP连接:
	t = threading.Thread(target=tcplink, args=(sock, addr)) # 每个连接都必须创建新线程(或进程), 否则单线程在处理连接的过程中,无法接受其他客户端的连接
	t.start()
```

服务器对应的客户端

```python
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(("127.0.0.1", 9999))
# 接收欢迎消息
print(s.recv(1024).decode("utf-8"))
# 发送数据
for data in [b"Michael", b"Tracy", b"sarah"]:
	s.send(data)
	print(s.recv(1024).decode("utf-8"))
# 关闭连接
s.send(b"exit")
# 关闭socket
s.close()
```

##### 关于socket和端口的说明

==关于socket的端口:服务器的`accept`生成新的`socket`并不会在本机占用新的端口==
socket是通过4个属性决定的,如果这4个属性都一致,就判断为同一个socket

1. 本地ip
2. 本地端口
3. 远程ip
4. 远程端口

其中服务器`accept`后生成的新的`socket`的`1.本地ip`和`2.本地端口`和
`listen`是生成的监听`socket`的本地ip和本地端口都是一致的,
区别只是`3.远程ip`和`4.远程端口`.
所以服务器不会因为客户端的连接很多就占用很多个端口.
而防火墙也只需要处理好目标是指定端口的协议数据即可.

另外:
==TCP和UDP的端口不互相冲突,就是同一个端口,不同的程序可以同时使用,而不会发生冲突和错乱==

#### UDP编程

服务器

```python
import socket

# 创建
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定
s.bind(("127.0.0.1", 9999))
print("Bind UDP on 9999")
# 接收数据
while True:
	data, addr = s.recvfrom(1024)
	print("Receive from %s:%s" % addr)
	s.sendto(b"Hello, %s!" % data, addr)
```

客户端

```python
import socket

# 创建
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定
s.bind(("127.0.0.1", 9999)) # 不绑定会出现[WinError 10022]错误
for data in [b"Michael", b"Tracy", b"sarah"]:
	# 发送
	s.sendto(data, ("127.0.0.1", 9999))
	# 接收
	print(s.recv(1024).decode("utf-8"))
s.close()
```

### 收发邮件

SMTP协议

smtplib
email

### 数据库

#### SQLite3

以下示例代码包括:

- 创建数据库
- 创建表
- 插入数据
- 提交保存数据库
- 加载数据库
- 读取数据

```python
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在,会自动在当前目录创建
conn = sqlite3.connect("test.db")
# 创建一个cursor
cursor = conn.cursor()
# 直营一条SQL语句,创建user表
cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
# 继续执行一条sql语句,插入一条记录
cursor.execute("insert into user (id, name) values ('1', 'Michael')")
# 通过rowcount获得插入的行数
print(cursor.rowcount)
# 关闭cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭connection
conn.close()

# 查询
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
# 执行查询语句
cursor.execute("select * from user where id = ?", "1")
# 获取查询结果集
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
```

#### ORM计数

python的ORM库有`ORMAlchemy`
ORM就是`Object-Relational Mapping`,
将数据库字段和类关联起来的一种方法,
可以实现多表关联,将操作数据库就像操作内存对象一样使用,不需要写sql语句.

## 异步IO

### 协程(Coroutine)

单线程调用是通过栈来进行的.
最上端只有一个函数,后续的函数都是层层调用后产生的.

多线程是同时运行多个无关联的函数

协程在表现结果上和多线程一致,但是协程是运行在单一一个线程上的,
协程也会同时调用多个毫无关联的函数,每个函数都有各自的调用栈.

协程的优势

1. 协程比线程最大的优势就是执行效率高.因为子程序切换不是线程切换,而是由程序自身控制,
	因此没有线程切换的开销,和多线程比,线程数量越多,协程的性能优势就越明显.

2. 不需要多线程的锁机制,因为只有一个线程,也不存在同时写变量的冲突,所以在协程中
	控制共享资源不加锁,只需要判断状态就好了,所以还是执行效率高.

充分利用多核CPU的最简单方法是:多进程+协程
(python的多线程实际是在单核cpu上运行的,并不能提高效率)

子程序就是协程的一种特例

python的协程是通过generator实现的.

```python
def cunsumer():
	r = ""
	while True:
		n = yield r
		if not n:
			return
		print("[CONSUMER]Consuming %s..." % n)
		r = "200 OK"

def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n += 1
		print("[PRODUCER]Producing %s..." % n)
		r = c.send(n)
		print("[PRODUCER]Consumer return: %s" % r)
	c.close()

c = cunsumer()
produce(c)
```

```python
[PRODUCER]Producing 1...
[CONSUMER]Consuming 1...
[PRODUCER]Consumer return: 200 OK
[PRODUCER]Producing 2...
[CONSUMER]Consuming 2...
[PRODUCER]Consumer return: 200 OK
[PRODUCER]Producing 3...
[CONSUMER]Consuming 3...
[PRODUCER]Consumer return: 200 OK
[PRODUCER]Producing 4...
[CONSUMER]Consuming 4...
[PRODUCER]Consumer return: 200 OK
[PRODUCER]Producing 5...
[CONSUMER]Consuming 5...
```

### `send`和`nexe`的关系&区别

```python
对于普通的生成器，第一个next调用，相当于启动生成器，会从生成器函数的第一行代码开始执行，直到第一次执行完yield语句（第4行）后，跳出生成器函数。
然后第二个next调用，进入生成器函数后，从yield语句的下一句语句（第5行）开始执行，然后重新运行到yield语句，执行后，跳出生成器函数，
后面再次调用next，依次类推。下面是一个列子：
1 def consumer():
2     r = 'here'
3     for i in xrange(3):
4         yield r
5         r = '200 OK'+ str(i)
6
7 c = consumer()
8 n1 = c.next()
9 n2 = c.next()
10 n3 = c.next()

了解了next()如何让包含yield的函数执行后，我们再来看另外一个非常重要的函数send(msg)。其实next()和send()在一定意义上作用是相似的，区别是send()可以传递yield表达式的值进去，而next()不能传递特定的值，只能传递None进去。因此，我们可以看做c.next() 和 c.send(None) 作用是一样的。
需要提醒的是，第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，否则会出错的，因为没有Python yield语句来接收这个值。
下面来着重说明下send执行的顺序。当第一次send（None）（对应11行）时，启动生成器，从生成器函数的第一行代码开始执行，直到第一次执行完yield（对应第4行）后，跳出生成器函数。这个过程中，n1一直没有定义。
下面运行到send（1）时，进入生成器函数，注意这里与调用next的不同。这里是从第4行开始执行，把1赋值给n1，但是并不执行yield部分。下面继续从yield的下一语句继续执行，然后重新运行到yield语句，执行后，跳出生成器函数。
即send和next相比，只是开始多了一次赋值的动作，其他运行流程是相同的。
1 def consumer():
2     r = 'here'
3     while True:
4         n1 = yield r
5         if not n1:
6             return
7         print('[CONSUMER] Consuming %s...' % n1)
8         r = '200 OK'+str(n1)
9
10 def produce(c):
11     aa = c.send(None)
12     n = 0
13     while n < 5:
14         n = n + 1
15         print('[PRODUCER] Producing %s...' % n)
16         r1 = c.send(n)
17         print('[PRODUCER] Consumer return: %s' % r1)
18     c.close()
19
20 c = consumer()
21 produce(c)

运行结果：
[PRODUCER] Producing 1...
[CONSUMER] Consuming 1...
[PRODUCER] Consumer return: 200 OK1
[PRODUCER] Producing 2...
[CONSUMER] Consuming 2...
[PRODUCER] Consumer return: 200 OK2
[PRODUCER] Producing 3...
[CONSUMER] Consuming 3...
[PRODUCER] Consumer return: 200 OK3
[PRODUCER] Producing 4...
[CONSUMER] Consuming 4...
[PRODUCER] Consumer return: 200 OK4
[PRODUCER] Producing 5...
[CONSUMER] Consuming 5...
[PRODUCER] Consumer return: 200 OK5
```

## asyncio

表现:同一个线程可以同时执行多个函数而不阻塞.
通过yield实现(协程)

```python
import threading
import asyncio

@asyncio.coroutine
def hello():
	print("Hello world!(%s)" % threading.currentThread())
	yield from asyncio.sleep(1)
	print("Hello again!(%s)" % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
```

```python
Hello world!(<_MainThread(MainThread, started 8708)>)
Hello world!(<_MainThread(MainThread, started 8708)>)
# 等待约1秒
Hello again!(<_MainThread(MainThread, started 8708)>)
Hello again!(<_MainThread(MainThread, started 8708)>)
```

## async/await

`python`3.5以后的新增优化写法:

```python
import asyncio

async def hello():
	print("Hello world!")
	r = await asyncio.sleep(1)
	print("Hello again!")

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
```

简化了代码的写法.

## 变量作用域

### 几个概念

- python能够改变变量作用域的代码段是def、class、lamda.
- if/elif/else、try/except/finally、for/while 并不能涉及变量作用域的更改，也就是说他们的代码块中的变量，在外部也是可以访问的
- 变量搜索路径是：本地变量->全局变量


1. python能够改变变量作用域的代码段是def、class、lamda.

```python
def scopetest():  
    localvar=6;  
    print(localvar)  
    
scopetest()  
#print(localvar) #去除注释这里会报错，因为localvar是本地变量  
```

2. if/elif/else、try/except/finally、for/while

```python\
while True:  
    newvar=8  
    print(newvar)  
    break;  
  
print(newvar)  
  
try:  
    newlocal=7  
    raise Exception  
except:  
    print(newlocal)#可以直接使用哦  
```

输出结果：8 8 7
可见这个关键字中定义变量，他们的作用域跟外部是一致的，这个跟Java的作用域概念有点不一样。
变量搜索路径是：本地变量->全局变量

```python
def scopetest():  
    var=6;  
    print(var)#  
      
var=5   
print(var)  
scopetest()  
print(var)  
```

输出结果：5 6 5
这里var 首先搜索的是本地变量，scopetest()中 var=6相当于自己定义了一个局部变量，赋值为6. 当然如果的确要修改全局变量的值，则需要如下：

```python
def scopetest():  
    global var   
    var=6;  
    print(var)#  
      
var=5   
print(var)  
scopetest()  
print(var)  
```

输出结果：5 6 6
再看一种这种情况：
```python
def scopetest():  
    var=6;  
    print(var)#  
    def innerFunc():  
        print(var)#look here  
    innerFunc()  
      
var=5   
print(var)  
scopetest()  
print(var)  
```

输出结果：5 6 6 5
根据调用顺序反向搜索，先本地变量再全局变量，例如搜先在innerFunc中搜索本地变量，没有，好吧，找找调用关系上一级scopetest，发现本地变量var=6，OK，就用他了。

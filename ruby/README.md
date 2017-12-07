# RUBY学习笔记

## 语法

### Hello World!

```ruby
puts "Hello World!
```

### 开始和结束

```ruby
# -*- coding: utf-8 -*-

puts "main"

END {
	puts "end"
}

BEGIN {
	puts "begin"
}
```

```ruby
begin
main
end
```

### 注释/多行注释

```ruby
puts "1"
# puts "2"
puts "3"
=begin
puts "4"
puts "5"
=end
puts "6"
puts "7"
```

## 数据类型

Number
String
Ranges
Symbols
true/false
nil
Array
Hash

### 操作符

`+-*/`
指数:`**`
指数后面可以是小数,可以直接开方

### Number

1. 整型
	integer:32位有符号
	bignum:64位有符号
	数字前可以有一个基础指标:
		0:八进制octal
		0x:十六进制hex
		0b:binary
		下划线在数字字符串中被忽略

2. 浮点型
	float

3. 字符串
	string
	双引号标记的字符串允许替换和使用反斜线符号，单引号标记的字符串不允许替换，且只允许使用 \\ 和 \' 两个反斜线符号。

	```ruby
	puts "求和:#{1+2+3}"
	```
	```ruby
	求和:6
	```

4. 数组
	数组字面量通过[]中以逗号分隔定义，且支持range定义。
	- 数组通过[]索引访问
	- 通过赋值操作插入、删除、替换元素
	- 通过+，－号进行合并和删除元素，且集合做为新集合出现
	- 通过<<号向原数据追加元素
	- 通过`*`号重复数组元素
	- 通过｜和&符号做并集和交集操作（注意顺序）

	```ruby
	arr = ["a", 1, 1.5, true]
	arr.each do |i|
		puts i
	end
	```

	```ruby
	a
	1
	1.5
	true
	```

5. 哈希
	就是map

	```ruby
	colors = {"red"=>0xf00, "green"=>0x0f0, "blue"=>0x00f}
	colors.each do |key, value|
		print key, " is ", value, "\n"
	end
	```

	```ruby
	red is 3840
	green is 240
	blue is 15
	```

6. 范围类型
	开始到结束指定范围内的值,半闭半开区间

	```ruby
	(1..5).each do |n|
		print n, " "
	end
	```

	```ruby
	1 2 3 4 5 
	```

## 类和对象

Ruby 提供了四种类型的变量：
	-局部变量：局部变量是在方法中定义的变量。局部变量在方法外是不可用的。在后续的章节中，您将看到有关方法的更多细节。局部变量以小写字母或 _ 开始。
	- 实例变量：实例变量可以跨任何特定的实例或对象中的方法使用。这意味着，实例变量可以从对象到对象的改变。实例变量在变量名之前放置符号（@）。
	- 类变量：类变量可以跨不同的对象使用。类变量属于类，且是类的一个属性。类变量在变量名之前放置符号（@@）。
	- 全局变量：类变量不能跨类使用。如果您想要有一个可以跨类使用的变量，您需要定义全局变量。全局变量总是以美元符号（$）开始。

```ruby
class Person
	@@num=0
	def initialize(name)
		@name=name
		@@num+=1
	end

	def hello()
		puts "hello #{@name}!"
		puts "hello #@name!"
		puts "total num:#@@num"
	end
end

p1 = Person.new("a")
p2 = Person.new("b")
p1.hello
```

```ruby
hello a!
hello a!
total num:2
```

## 变量

支持五种类型的变量。
- 一般小写字母、下划线开头：变量（Variable）。
- $开头：全局变量（Global variable）。
- @开头：实例变量（Instance variable）。
- @@开头：类变量（Class variable）类变量被共享在整个继承链中
- 大写字母开头：常数（Constant）。

1. 全局变量

```ruby
$global_test = 10

def test()
	puts $global_test
end

test
```

```ruby
10
```

2. 类变量
3. 实例变量
4. 局部变量
局部变量以小写字母或下划线 _ 开头。局部变量的作用域从 class、module、def 或 do 到相对应的结尾或者从左大括号到右大括号 {}。
5. 常量
常量以大写字母开头。定义在类或模块内的常量可以从类或模块的内部访问，定义在类或模块外的常量可以被全局访问。
常量不能定义在方法内。引用一个未初始化的常量会产生错误。对已经初始化的常量赋值会产生警告。

```ruby
ABC = 10

def test()
	puts ABC, "#{ABC}"
end

test
```

```ruby
10
10
```

6. 伪变量
- self: 当前方法的接收器对象。
- true: 代表 true 的值。
- false: 代表 false 的值。
- nil: 代表 undefined 的值。
- __FILE__: 当前源文件的名称。
- __LINE__: 当前行在源文件中的编号。

## 运算符

- 算术运算符

假设变量 a 的值为 10，变量 b 的值为 20，那么：

运算符 | 描述 | 实例
-|
+ | 加法 - 把运算符两边的操作数相加 | a + b 将得到 30
- | 减法 - 把左操作数减去右操作数 | a - b 将得到 -10
* | 乘法 - 把运算符两边的操作数相乘 | a * b 将得到 200
/ | 除法 - 把左操作数除以右操作数 | b / a 将得到 2
% | 求模 - 把左操作数除以右操作数，返回余数 | b % a 将得到 0
** | 指数 - 执行指数计算 | a**b 将得到 10 的 20 次方

- 比较运算符

假设变量 a 的值为 10，变量 b 的值为 20，那么：

运算符 | 描述 | 实例
-|
== | 检查两个操作数的值是否相等，如果相等则条件为真。 | (a == b) 不为真。
!= | 检查两个操作数的值是否相等，如果不相等则条件为真。 | (a != b) 为真。
> | 检查左操作数的值是否大于右操作数的值，如果是则条件为真。 | (a > b) 不为真。
< | 检查左操作数的值是否小于右操作数的值，如果是则条件为真。 | (a < b) 为真。
>= | 检查左操作数的值是否大于或等于右操作数的值，如果是则条件为真。 | (a >= b) 不为真。
<= | 检查左操作数的值是否小于或等于右操作数的值，如果是则条件为真。 | (a <= b) 为真。
<=> | 联合比较运算符。如果第一个操作数等于第二个操作数则返回 0，如果第一个操作数大于第二个操作数则返回 1，如果第一个操作数小于第二个操作数则返回 -1。 | (a <=> b) 返回 -1。
=== | 用于测试 case 语句的 when 子句内的相等。 | (1...10) === 5 返回 true。
.eql? | 如果接收器和参数具有相同的类型和相等的值，则返回 true。 | 1 == 1.0 返回 true，但是 1.eql?(1.0) 返回 false。
equal? | 如果接收器和参数具有相同的对象 id，则返回 true。 | 如果 aObj 是 bObj 的副本，那么 aObj == bObj 返回 true，a.equal?bObj 返回 false，但是 a.equal?aObj 返回 true。

- 赋值运算符

假设变量 a 的值为 10，变量 b 的值为 20，那么：

运算符 | 描述 | 实例
-|
= | 简单的赋值运算符，把右操作数的值赋给左操作数 | c = a + b 将把 a + b 的值赋给 c
+= | 加且赋值运算符，把右操作数加上左操作数的结果赋值给左操作数 | c += a 相当于 c = c + a
-= | 减且赋值运算符，把左操作数减去右操作数的结果赋值给左操作数 | c -= a 相当于 c = c - a
\*= | 乘且赋值运算符，把右操作数乘以左操作数的结果赋值给左操作数 | c \*= a 相当于 c = c * a
/= | 除且赋值运算符，把左操作数除以右操作数的结果赋值给左操作数 | c /= a 相当于 c = c / a
%= | 求模且赋值运算符，求两个操作数的模赋值给左操作数 | c %= a 相当于 c = c % a
\*\*= | 指数且赋值运算符，执行指数计算，并赋值给左操作数 |  c \*\*= a 相当于 c = c \*\* a

- 并行赋值

Ruby 也支持变量的并行赋值。这使得多个变量可以通过一行的 Ruby 代码进行初始化。例如

```ruby
a = 10
b = 20
c = 30
```

使用并行赋值可以更快地声明：
`a, b, c = 10, 20, 30`

并行赋值在交换两个变量的值时也很有用：
`a, b = b, c`

- 位运算符

位运算符作用于位，并逐位执行操作。
假设如果 a = 60，且 b = 13，现在以二进制格式，它们如下所示：
a = 0011 1100
b = 0000 1101
-----------------
a&b = 0000 1100
a|b = 0011 1101
a^b = 0011 0001
~a  = 1100 0011
下表列出了 Ruby 支持的位运算符。

运算符 | 描述 | 实例
-|
& | 如果同时存在于两个操作数中，二进制 AND 运算符复制一位到结果中。 | (a & b) 将得到 12，即为 0000 1100
\| | 如果存在于任一操作数中，二进制 OR 运算符复制一位到结果中。 | (a \| b) 将得到 61，即为 0011 1101
^ | 如果存在于其中一个操作数中但不同时存在于两个操作数中，二进制异或运算符复制一位到结果中。 | (a ^ b) 将得到 49，即为 0011 0001
~ | 二进制补码运算符是一元运算符，具有"翻转"位效果，即0变成1，1变成0。 | (~a ) 将得到 -61，即为 1100 0011，一个有符号二进制数的补码形式。
<< | 二进制左移运算符。左操作数的值向左移动右操作数指定的位数。 | a << 2 将得到 240，即为 1111 0000
>> | 二进制右移运算符。左操作数的值向右移动右操作数指定的位数。 | a >> 2 将得到 15，即为 0000 1111

- 逻辑运算符

假设变量 a 的值为 10，变量 b 的值为 20，那么：

运算符 | 描述 | 实例
-|
and | 称为逻辑与运算符。如果两个操作数都为真，则条件为真。 | (a and b) 为真。
or | 称为逻辑或运算符。如果两个操作数中有任意一个非零，则条件为真。 | (a or b) 为真。
&& | 称为逻辑与运算符。如果两个操作数都非零，则条件为真。 | (a && b) 为真。
\|\| | 称为逻辑或运算符。如果两个操作数中有任意一个非零，则条件为真。 | (a \|\| b) 为真。
! | 称为逻辑非运算符。用来逆转操作数的逻辑状态。如果条件为真则逻辑非运算符将使其为假。 | !(a && b) 为假。
not | 称为逻辑非运算符。用来逆转操作数的逻辑状态。如果条件为真则逻辑非运算符将使其为假。 | not(a && b) 为假。

- 三元运算符

有一个以上的操作称为三元运算符。第一个计算表达式的真假值，然后根据这个结果决定执行后边两个语句中的一个。条件运算符的语法如下

运算符 | 描述 | 实例
-|
? : | 条件表达式 | 如果条件为真 ? 则值为 X : 否则值为 Y

- 范围运算符

在 Ruby 中，序列范围用于创建一系列连续的值 - 包含起始值、结束值（视情况而定）和它们之间的值。
在 Ruby 中，这些序列是使用 ".." 和 "..." 范围运算符来创建的。两点形式创建的范围包含起始值和结束值，三点形式创建的范围只包含起始值不包含结束值。

运算符 | 描述 | 实例
-|
.. | 创建一个从开始点到结束点的范围（包含结束点） | 1..10 创建从 1 到 10 的范围
... | 创建一个从开始点到结束点的范围（不包含结束点）| 1...10 创建从 1 到 9 的范围

- defined? 运算符

defined? 是一个特殊的运算符，以方法调用的形式来判断传递的表达式是否已定义。它返回表达式的描述字符串，如果表达式未定义则返回 nil。

`defined? variable # 如果 variable 已经初始化，则为 True`

```ruby
foo = 42
defined? foo    # => "local-variable"
defined? $_     # => "global-variable"
defined? bar    # => nil（未定义）
```

`defined? method_call # 如果方法已经定义，则为 True`

```ruby
defined? puts        # => "method"
defined? puts(bar)   # => nil（在这里 bar 未定义）
defined? unpack      # => nil（在这里未定义）
```

`defined? super # 如果存在可被 super 用户调用的方法，则为 True`

```ruby
defined? super     # => "super"（如果可被调用）
defined? super     # => nil（如果不可被调用）
```

`defined? yield   # 如果已传递代码块，则为 True`

```ruby
defined? yield    # => "yield"（如果已传递块）
defined? yield    # => nil（如果未传递块）
```

## 点运算符 "." 和双冒号运算符 "::"

你可以通过在方法名称前加上类或模块名称和 . 来调用类或模块中的方法。你可以使用类或模块名称和两个冒号 :: 来引用类或模块中的常量。
:: 是一元运算符，允许在类或模块内定义常量、实例方法和类方法，可以从类或模块外的任何地方进行访问。
请记住：在 Ruby 中，类和方法也可以被当作常量。
你只需要在表达式的常量名前加上 :: 前缀，即可返回适当的类或模块对象。
如果 :: 前的表达式为类或模块名称，则返回该类或模块内对应的常量值；如果 :: 前未没有前缀表达式，则返回主Object类中对应的常量值。 。

```ruby
MR_COUNT = 0        # 定义在主 Object 类上的常量
module Foo
  MR_COUNT = 0
  ::MR_COUNT = 1    # 设置全局计数为 1
  MR_COUNT = 2      # 设置局部计数为 2
end
puts MR_COUNT       # 这是全局常量	1
puts Foo::MR_COUNT  # 这是 "Foo" 的局部常量	2
```

```ruby
CONST = ' out there'
class Inside_one
   CONST = proc {' in there'}
   def where_is_my_CONST
      ::CONST + ' inside one'
   end
end
class Inside_two
   CONST = ' inside two'
   def where_is_my_CONST
      CONST
   end
end
puts Inside_one.new.where_is_my_CONST #  out there inside one
puts Inside_two.new.where_is_my_CONST #  inside two
puts Object::CONST + Inside_two::CONST #  out there inside two
puts Inside_two::CONST + CONST #  inside two out there
puts Inside_one::CONST # #<Proc:0x000000000278e130@D:/pan/test_ruby/test/test.rb:5>
puts Inside_one::CONST.call + Inside_two::CONST #  in there inside two
```

## 运算符的优先级

方法 | 运算符 | 描述
-|
是 | :: | 常量解析运算符
是 | [ ] [ ]= | 元素引用、元素集合
是 | ** | 指数
是 | ! ~ + - | 非、补、一元加、一元减（最后两个的方法名为 +@ 和 -@）
是 | * / % | 乘法、除法、求模
是 | + - | 加法和减法
是 | >> << | 位右移、位左移
是 | & | 位与
是 | ^ \| | 位异或、位或
是 | <= < > >= | 比较运算符
是 | <=> == === != =~ !~ | 相等和模式匹配运算符（!= 和 !~ 不能被定义为方法）
&& | 逻辑与
\|\| | 逻辑或
.. ... | 范围（包含、不包含）
? : | 三元 if-then-else
= %= { /= -= += \|= &= >>= <<= *= &&= \|\|= **= | 赋值
defined? | 检查指定符号是否已定义
not | 逻辑否定
or and | 逻辑组成

## 注释

### 单行注释

`#`

### 多行注释

```ruby
=begin
多行注释
多行注释
多行注释
=end
```

## 判断

```ruby
x=1
if x > 2
   puts "x 大于 2"
elsif x <= 2 and x!=0
   puts "x 是 1"
else
   puts "无法得知 x 的值"
end
```

### if 修饰符

语法
`code if condition`
if修饰词组表示当 if 右边之条件成立时才执行 if 左边的式子。即如果 conditional 为真，则执行 code。

```ruby
x=1
puts x if x == 1
```

### unless 语句

语法

```ruby
unless conditional [then]
   code
[else
   code ]
end
```

unless式和 if式作用相反，即如果 conditional 为假，则执行 code。如果 conditional 为真，则执行 else 子句中指定的 code。

```ruby
x=1
unless x>2
	puts "x <= 2"
else
	puts "x > 2"
end
```

### unless 修饰符

语法
`code unless conditional`

如果 conditional 为假，则执行 code。

```ruby
x=1
puts x unless x>2
```

### case 语句

语法

```ruby
case expression
[when expression [, expression ...] [then]
   code ]...
[else
   code ]
end
```

case先对一个 expression 进行匹配判断，然后根据匹配结果进行分支选择。
它使用 ===运算符比较 when 指定的 expression，若一致的话就执行 when 部分的内容。
通常我们省略保留字 then 。若想在一行内写出完整的 when 式，则必须以 then 隔开条件式和程式区块。如下所示:

`when a == 4 then a = 7 end`

因此：

```ruby
case expr0
when expr1, expr2
   stmt1
when expr3, expr4
   stmt2
else
   stmt3
end
```

基本上类似于：

```ruby
_tmp = expr0
if expr1 === _tmp || expr2 === _tmp
   stmt1
elsif expr3 === _tmp || expr4 === _tmp
   stmt2
else
   stmt3
end
```

例

```ruby
$age =  5
case $age
when 0 .. 2
    puts "婴儿"
when 3 .. 6
    puts "小孩"
when 7 .. 12
    puts "child"
when 13 .. 18
    puts "少年"
else
    puts "其他年龄段的"
end
```

当case的"表达式"部分被省略时，将计算第一个when条件部分为真的表达式。

```ruby
foo = false
bar = true
quu = false
 
case
when foo then puts 'foo is true'
when bar then puts 'bar is true'
when quu then puts 'quu is true'
end
# 显示 "bar is true"
```

## 循环

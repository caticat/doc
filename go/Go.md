# 学习笔记


[TOC]

## 阅读笔记
[书签](https://github.com/Unknwon/the-way-to-go_ZH_CN/blob/master/eBook/directory.md)
[当前阅读](https://github.com/Unknwon/the-way-to-go_ZH_CN/blob/master/eBook/04.4.md)

### 25个保留关键字
break|default|func|interface|select
-|
case|defer|go|map|struct
chan|else|goto|package|switch
const|fallthrough|if|range|type
continue|for|import|return|var

### 36个预定义标识符
append|bool|byte|cap|close|complex|complex64|complex128|uint16
-|
copy|false|float32|float64|imag|int|int8|int16|uint32
int32|int64|iota|len|make|new|nil|panic|uint64
print|println|real|recover|string|true|uint|uint8|uintptr

程序一般由关键字、常量、变量、运算符、类型和函数组成。

程序中可能会使用到这些分隔符：括号 ()，中括号 [] 和大括号 {}。

程序中可能会使用到这些标点符号：.、,、;、: 和 …。

程序的代码通过语句来实现结构化。每个语句不需要像 C 家族中的其它语言一样以分号 ; 结尾，因为这些工作都将由 Go 编译器自动完成。

如果你打算将多个语句写在同一行，它们则必须使用 ; 人为区分，但在实际开发中我们并不鼓励这种做法。

### 包
每个 Go 程序都是由包组成的。
程序运行的入口是包 main 。
按照惯例，包名与导入路径的最后一个目录一致。例如，"math/rand" 包由 package rand 语句开始。

### 导入
```go
import {
	"fmt"
	"math"
}
```
等同于
```go
import "fmt"
import "math"
```
推荐使用`{}`来表示

### 导出名
在 Go 中，首字母大写的名称是被导出的。
在导入包之后，你只能访问包所导出的名字，任何未导出的名字是不能被包外的代码访问的。
Foo 和 FOO 都是被导出的名称。名称 foo 是不会被导出的。

### 函数
函数可以没有参数或接受多个参数。
注意类型在变量名 之后 。
当两个或多个连续的函数命名参数是同一类型，则除了最后一个类型之外，其他都可以省略。
如:
```go
x int, y int
```
可以写成
```go
x, y int
```

### 多值返回
函数可以返回任意数量的返回值。

### 命名返回值
Go 的返回值可以被命名，并且就像在函数体开头声明的变量那样使用。
返回值的名称应当具有一定的意义，可以作为文档使用。
没有参数的 return 语句返回各个返回变量的当前值。这种用法被称作“裸”返回。
直接返回语句仅应当用在像下面这样的短函数中。在长的函数中它们会影响代码的可读性。
```go
package main

import "fmt"

func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func main() {
	fmt.Println(split(17))
}
```

### 变量
var 语句定义了一个变量的列表；跟函数的参数列表一样，类型在后面。
就像在这个例子中看到的一样， var 语句可以定义在包或函数级别。
```go
package main

import "fmt"

var c, python, java bool

func main() {
	var i int
	fmt.Println(i, c, python, java)
}
```

### 初始化变量
变量定义可以包含初始值，每个变量对应一个。
如果初始化是使用表达式，则可以省略类型；变量从初始值中获得类型。
```go
package main

import "fmt"

var i, j int = 1, 2

func main() {
	var c, python, java = true, false, "no!"
	fmt.Println(i, j, c, python, java)
}
```

### 短声明变量
在函数中， := 简洁赋值语句在明确类型的地方，可以用于替代 var 定义。
函数外的每个语句都必须以关键字开始（ var 、 func 、等等）， := 结构不能使用在函数外。
```go
package main

import "fmt"

func main() {
	var i, j int = 1, 2
	k := 3
	c, python, java := true, false, "no!"

	fmt.Println(i, j, k, c, python, java)
}
```

### 基本类型
Go 的基本类型有Basic types
```go
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // uint8 的别名

rune // int32 的别名
     // 代表一个Unicode码

float32 float64

complex64 complex128
```

### 零值
变量在定义时没有明确的初始化时会赋值为 零值 。
零值是：
数值类型为 0 ，
布尔类型为 false ，
字符串为 "" （空字符串）。

### 类型转换
表达式 T(v) 将值 v 转换为类型 T 。
一些关于数值的转换：
```go
var i int = 42
var f float64 = float64(i)
var u uint = uint(f)
```
或者，更加简单的形式：
```go
i := 42
f := float64(i)
u := uint(f)
```

### 类型推导
在定义一个变量却并不显式指定其类型时（使用 := 语法或者 var = 表达式语法）， 变量的类型由（等号）右侧的值推导得出。
当右值定义了类型时，新变量的类型与其相同：
```go
var i int
j := i // j 也是一个 int
```
但是当右边包含了未指名类型的数字常量时，新的变量就可能是 int 、 float64 或 complex128 。 这取决于常量的精度：
```go
i := 42           // int
f := 3.142        // float64
g := 0.867 + 0.5i // complex128
```

### 常量
常量的定义与变量类似，只不过使用 const 关键字。
常量可以是字符、字符串、布尔或数字类型的值。
常量不能使用 := 语法定义。
```go
package main

import "fmt"

const Pi = 3.14

func main() {
	const World = "世界"
	fmt.Println("Hello", World)
	fmt.Println("Happy", Pi, "Day")

	const Truth = true
	fmt.Println("Go rules?", Truth)
}
```

### for
Go 只有一种循环结构—— for 循环。

基本的 for 循环包含三个由分号分开的组成部分：

初始化语句：在第一次循环执行前被执行
循环条件表达式：每轮迭代开始前被求值
后置语句：每轮迭代后被执行
初始化语句一般是一个短变量声明，这里声明的变量仅在整个 for 循环语句可见。

如果条件表达式的值变为 false，那么迭代将终止。

注意：不像 C，Java，或者 Javascript 等其他语言，for 语句的三个组成部分 并不需要用括号括起来，但循环体必须用 { } 括起来。

```go
package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
}
```
循环初始化语句和后置语句都是可选的。
```go
package main

import "fmt"

func main() {
	sum := 1
	for ; sum < 1000; {
		sum += sum
	}
	fmt.Println(sum)
}

```
```go
package main

import "fmt"

func main() {
	sum := 1
	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)
}

```
死循环
```go
for {

}
```

### if
就像 for 循环一样，Go 的 if 语句也不要求用 ( ) 将条件括起来，同时， { } 还是必须有的。
```go
package main

import (
	"fmt"
)

func main() {
	i := 100
	if i < 10 {
		fmt.Println("<10")
	} else if i < 100 {
		fmt.Println("<100")
	} else {
		fmt.Println("else")
	}
}
```

### if 的便捷语句
跟 for 一样， if 语句可以在条件之前执行一个简单语句。
由这个语句定义的变量的作用域仅在 if 范围之内。
```go
package main

import (
	"fmt"
	"math"
)

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	}
	return lim
}

func main() {
	fmt.Println(
		pow(3, 2, 10),
		pow(3, 3, 20),
	)
}
```
在 if 的便捷语句定义的变量同样可以在任何对应的 else 块中使用。

### switch
除非以 fallthrough 语句结束，否则分支会自动终止。
```go
package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.", os)
	}
}

```

### switch 的执行顺序
switch 的条件从上到下的执行，当匹配成功的时候停止。
例如:
```go
switch i {
case 0:
case f():
}
```
当 i==0 时不会调用 f 。）
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("When's Saturday?")
	today := time.Now().Weekday()
	switch time.Saturday {
	case today + 0:
		fmt.Println("Today.")
	case today + 1:
		fmt.Println("Tomorrow.")
	case today + 2:
		fmt.Println("In two days.")
	default:
		fmt.Println("Too far away.")
	}
}

```

### 没有条件的 switch
没有条件的 switch 同 switch true 一样。
这一构造使得可以用更清晰的形式来编写长的 if-then-else 链。
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}
}
```

### defer
defer 语句会延迟函数的执行直到上层函数返回。

延迟调用的参数会立刻生成，但是在上层函数返回前函数都不会被调用。
```go
package main

import "fmt"

func main() {
	defer fmt.Println("world")

	fmt.Println("hello")
}
```
可以用来保证函数最后会关闭已经打开的文件流、解互斥锁等
调用顺序是最后defer的内容最先调用

### defer 栈
延迟的函数调用被压入一个栈中。当函数返回时， 会按照后进先出的顺序调用被延迟的函数调用。
```go
package main

import "fmt"

func main() {
	fmt.Println("counting")

	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}

	fmt.Println("done")
}

```

### 指针
Go 具有指针。 指针保存了变量的内存地址。

类型 *T 是指向类型 T 的值的指针。其零值是 nil 。
```go
var p *int
```
`&` 符号会生成一个指向其作用对象的指针。
```go
i := 42
p = &i
```
`*`符号表示指针指向的底层的值。
```go
fmt.Println(*p) // 通过指针 p 读取 i
*p = 21         // 通过指针 p 设置 i
```
这也就是通常所说的“间接引用”或“非直接引用”。
与 C 不同，Go 没有指针运算。
```go
package main

import "fmt"

func main() {
	i, j := 42, 2701

	p := &i         // point to i
	fmt.Println(*p) // read i through the pointer
	*p = 21         // set i through the pointer
	fmt.Println(i)  // see the new value of i

	p = &j         // point to j
	*p = *p / 37   // divide j through the pointer
	fmt.Println(j) // see the new value of j
}
```

### 结构体
一个结构体（ struct ）就是一个字段的集合。

（而 type 的含义跟其字面意思相符。）
```go
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	fmt.Println(Vertex{1, 2})
}
```

### 结构体字段
结构体字段使用点号来访问。
```go
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	v.X = 4
	fmt.Println(v.X)
}
```

### 结构体指针
结构体字段可以通过结构体指针来访问。

通过指针间接的访问是透明的。

```go
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9
	fmt.Println(v)
}
```

### 结构体文法
结构体文法表示通过结构体字段的值作为列表来新分配一个结构体。

使用 Name: 语法可以仅列出部分字段。（字段名的顺序无关。）

特殊的前缀 & 返回一个指向结构体的指针。
```go
package main

import "fmt"

type Vertex struct {
	X, Y int
}

var (
	v1 = Vertex{1, 2}  // 类型为 Vertex
	v2 = Vertex{X: 1}  // Y:0 被省略
	v3 = Vertex{}      // X:0 和 Y:0
	p  = &Vertex{1, 2} // 类型为 *Vertex
)

func main() {
	fmt.Println(v1, p, v2, v3)
}

```

### 数组
类型 [n]T 是一个有 n 个类型为 T 的值的数组。

表达式
```go
var a [10]int
```
定义变量 a 是一个有十个整数的数组。

数组的长度是其类型的一部分，因此数组不能改变大小。 这看起来是一个制约，但是请不要担心； Go 提供了更加便利的方式来使用数组。
```go
package main

import "fmt"

func main() {
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)
}
```

### slice
一个 slice 会指向一个序列的值，并且包含了长度信息。

[]T 是一个元素类型为 T 的 slice。

len(s) 返回 slice s 的长度。
```go
package main

import "fmt"

func main() {
	s := []int{2, 3, 5, 7, 11, 13}
	fmt.Println("s ==", s)

	for i := 0; i < len(s); i++ {
		fmt.Printf("s[%d] == %d\n", i, s[i])
	}
}

```

### slice 的 slice
slice 可以包含任意的类型，包括另一个 slice。
```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	// Create a tic-tac-toe board.
	game := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}

	// The players take turns.
	game[0][0] = "X"
	game[2][2] = "O"
	game[2][0] = "X"
	game[1][0] = "O"
	game[0][2] = "X"

	printBoard(game)
}

func printBoard(s [][]string) {
	for i := 0; i < len(s); i++ {
		fmt.Printf("%s\n", strings.Join(s[i], " "))
	}
}
```

### 对 slice 切片
slice 可以重新切片，创建一个新的 slice 值指向相同的数组。

表达式

`s[lo:hi]`
表示从 lo 到 hi-1 的 slice 元素，含前端，不包含后端。因此

`s[lo:lo]`
是空的，而

`s[lo:lo+1]`
有一个元素。
```go
package main

import "fmt"

func main() {
	s := []int{2, 3, 5, 7, 11, 13}
	fmt.Println("s ==", s)
	fmt.Println("s[1:4] ==", s[1:4])

	// 省略下标代表从 0 开始
	fmt.Println("s[:3] ==", s[:3])

	// 省略上标代表到 len(s) 结束
	fmt.Println("s[4:] ==", s[4:])
}

```

### 构造 slice
slice 由函数 make 创建。这会分配一个全是零值的数组并且返回一个 slice 指向这个数组：
```go
a := make([]int, 5)  // len(a)=5
```
为了指定容量，可传递第三个参数到 make：
```go
b := make([]int, 0, 5) // len(b)=0, cap(b)=5

b = b[:cap(b)] // len(b)=5, cap(b)=5
b = b[1:]      // len(b)=4, cap(b)=4
```
**容量必然要比长度大，否则报错**
```go
package main

import "fmt"

func main() {
	a := make([]int, 5)
	printSlice("a", a)
	b := make([]int, 0, 5)
	printSlice("b", b)
	c := b[:2]
	printSlice("c", c)
	d := c[2:5]
	printSlice("d", d)
}

func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n",
		s, len(x), cap(x), x)
}

```

### nil slice
slice 的零值是 nil 。

一个 nil 的 slice 的长度和容量是 0。

```go
package main

import "fmt"

func main() {
	var z []int
	fmt.Println(z, len(z), cap(z))
	if z == nil {
		fmt.Println("nil!")
	}
}

```

### 向 slice 添加元素
向 slice 的末尾添加元素是一种常见的操作，因此 Go 提供了一个内建函数 append 。 内建函数的文档对 append 有详细介绍。

`func append(s []T, vs ...T) []T`
append 的第一个参数 s 是一个元素类型为 T 的 slice ，其余类型为 T 的值将会附加到该 slice 的末尾。

append 的结果是一个包含原 slice 所有元素加上新添加的元素的 slice。

如果 s 的底层数组太小，而不能容纳所有值时，会分配一个更大的数组。 返回的 slice 会指向这个新分配的数组。
```go
package main

import "fmt"

func main() {
	var a []int
	printSlice("a", a)

	// append works on nil slices.
	a = append(a, 0)
	printSlice("a", a)

	// the slice grows as needed.
	a = append(a, 1)
	printSlice("a", a)

	// we can add more than one element at a time.
	a = append(a, 2, 3, 4)
	printSlice("a", a)
}

func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n",
		s, len(x), cap(x), x)
}
```

### range
for 循环的 range 格式可以对 slice 或者 map 进行迭代循环。

当使用 for 循环遍历一个 slice 时，每次迭代 range 将返回两个值。 第一个是当前下标（序号），第二个是该下标所对应元素的一个拷贝。
```go
package main

import "fmt"

var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

func main() {
	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}
}

```

可以通过赋值给 _ 来忽略序号和值。

如果只需要索引值，去掉 “ , value ” 的部分即可。
```go
package main

import "fmt"

func main() {
	pow := make([]int, 10)
	for i := range pow {
		pow[i] = 1 << uint(i)
	}
	for _, value := range pow {
		fmt.Printf("%d\n", value)
	}
}
```

### map
map 映射键到值。

map 在使用之前必须用 make 来创建；值为 nil 的 map 是空的，并且不能对其赋值。
```go
package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m map[string]Vertex

func main() {
	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40.68433, -74.39967,
	}
	fmt.Println(m["Bell Labs"])
}

```

### map 的文法
map 的文法跟结构体文法相似，不过必须有键名。
```go
package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m = map[string]Vertex{
	"Bell Labs": Vertex{
		40.68433, -74.39967,
	},
	"Google": Vertex{
		37.42202, -122.08408,
	},
}

func main() {
	fmt.Println(m)
}
```

若顶级类型只是一个类型名，你可以在文法的元素中省略它。
```go
package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m = map[string]Vertex{
	"Bell Labs": {40.68433, -74.39967},
	"Google":    {37.42202, -122.08408},
}

func main() {
	fmt.Println(m)
}

```

### 修改 map
在 map m 中插入或修改一个元素：

`m[key] = elem`
获得元素：

`elem = m[key]`
删除元素：

`delete(m, key)`
通过双赋值检测某个键存在：

`elem, ok = m[key]`
如果 key 在 m 中， ok 为 true。否则， ok 为 false，并且 elem 是 map 的元素类型的零值。

同样的，当从 map 中读取某个不存在的键时，结果是 map 的元素类型的零值。
```go
package main

import "fmt"

func main() {
	m := make(map[string]int)

	m["Answer"] = 42
	fmt.Println("The value:", m["Answer"])

	m["Answer"] = 48
	fmt.Println("The value:", m["Answer"])

	delete(m, "Answer")
	fmt.Println("The value:", m["Answer"])

	v, ok := m["Answer"]
	fmt.Println("The value:", v, "Present?", ok)
}
```

### 函数值
函数也是值。他们可以像其他值一样传递，比如，函数值可以作为函数的参数或者返回值。
```go
package main

import (
	"fmt"
	"math"
)

func compute(fn func(float64, float64) float64) float64 {
	return fn(3, 4)
}

func main() {
	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}
	fmt.Println(hypot(5, 12))

	fmt.Println(compute(hypot))
	fmt.Println(compute(math.Pow))
}

```

### 函数的闭包
Go 函数可以是一个闭包。闭包是一个函数值，它引用了函数体之外的变量。 这个函数可以对这个引用的变量进行访问和赋值；换句话说这个函数被“绑定”在这个变量上。

例如，函数 adder 返回一个闭包。每个返回的闭包都被绑定到其各自的 sum 变量上。
```go
package main

import "fmt"

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func main() {
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}
}
```

### 方法
Go 没有类。然而，仍然可以在结构体类型上定义方法。

方法接收者 出现在 func 关键字和方法名之间的参数中。

```go
package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func (v *Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := &Vertex{3, 4}
	fmt.Println(v.Abs())
}

```

你可以对包中的 任意 类型定义任意方法，而不仅仅是针对结构体。

但是，不能对来自其他包的类型或基础类型定义方法。

```go
package main

import (
	"fmt"
	"math"
)

type MyFloat float64

func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

func main() {
	f := MyFloat(-math.Sqrt2)
	fmt.Println(f.Abs())
}

```

### 接收者为指针的方法
方法可以与命名类型或命名类型的指针关联。

刚刚看到的两个 Abs 方法。一个是在 *Vertex 指针类型上，而另一个在 MyFloat 值类型上。 有两个原因需要使用指针接收者。首先避免在每个方法调用中拷贝值（如果值类型是大的结构体的话会更有效率）。其次，方法可以修改接收者指向的值。

尝试修改 Abs 的定义，同时 Scale 方法使用 Vertex 代替 *Vertex 作为接收者。

当 v 是 Vertex 的时候 Scale 方法没有任何作用。Scale 修改 v。当 v 是一个值（非指针），方法看到的是 Vertex 的副本，并且无法修改原始值。

Abs 的工作方式是一样的。只不过，仅仅读取 v。所以读取的是原始值（通过指针）还是那个值的副本并没有关系。
```go
package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func (v *Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := &Vertex{3, 4}
	fmt.Printf("Before scaling: %+v, Abs: %v\n", v, v.Abs())
	v.Scale(5)
	fmt.Printf("After scaling: %+v, Abs: %v\n", v, v.Abs())
}
```

### 接口
接口类型是由一组方法定义的集合。

接口类型的值可以存放实现这些方法的任何值。

注意： 示例代码的 22 行存在一个错误。 由于 Abs 只定义在 *Vertex（指针类型）上， 所以 Vertex（值类型）不满足 Abser。
```go
package main

import (
	"fmt"
	"math"
)

type Abser interface {
	Abs() float64
}

func main() {
	var a Abser
	f := MyFloat(-math.Sqrt2)
	v := Vertex{3, 4}

	a = f  // a MyFloat 实现了 Abser
	a = &v // a *Vertex 实现了 Abser

	// 下面一行，v 是一个 Vertex（而不是 *Vertex）
	// 所以没有实现 Abser。
	a = v

	fmt.Println(a.Abs())
}

type MyFloat float64

func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

type Vertex struct {
	X, Y float64
}

func (v *Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
```

### 隐式接口
类型通过实现那些方法来实现接口。 没有显式声明的必要；所以也就没有关键字“implements“。

隐式接口解藕了实现接口的包和定义接口的包：互不依赖。

因此，也就无需在每一个实现上增加新的接口名称，这样同时也鼓励了明确的接口定义。

包 io 定义了 Reader 和 Writer；其实不一定要这么做。
```go
package main

import (
	"fmt"
	"os"
)

type Reader interface {
	Read(b []byte) (n int, err error)
}

type Writer interface {
	Write(b []byte) (n int, err error)
}

type ReadWriter interface {
	Reader
	Writer
}

func main() {
	var w Writer

	// os.Stdout 实现了 Writer
	w = os.Stdout

	fmt.Fprintf(w, "hello, writer\n")
}

```

### Stringers
一个普遍存在的接口是 fmt 包中定义的 Stringer。

```go
type Stringer interface {
    String() string
}
```
Stringer 是一个可以用字符串描述自己的类型。`fmt`包 （还有许多其他包）使用这个来进行输出。
```go
package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func (p Person) String() string {
	return fmt.Sprintf("%v (%v years)", p.Name, p.Age)
}

func main() {
	a := Person{"Arthur Dent", 42}
	z := Person{"Zaphod Beeblebrox", 9001}
	fmt.Println(a, z)
}
```

### 错误
Go 程序使用 error 值来表示错误状态。

与 fmt.Stringer 类似， error 类型是一个内建接口：
```go
type error interface {
    Error() string
}
```
（与 fmt.Stringer 类似，fmt 包在输出时也会试图匹配 error。）

通常函数会返回一个 error 值，调用的它的代码应当判断这个错误是否等于 nil， 来进行错误处理。
```go
i, err := strconv.Atoi("42")
if err != nil {
    fmt.Printf("couldn't convert number: %v\n", err)
    return
}
fmt.Println("Converted integer:", i)
```
error 为 nil 时表示成功；非 nil 的 error 表示错误。
```go
package main

import (
	"fmt"
	"time"
)

type MyError struct {
	When time.Time
	What string
}

func (e *MyError) Error() string {
	return fmt.Sprintf("at %v, %s",
		e.When, e.What)
}

func run() error {
	return &MyError{
		time.Now(),
		"it didn't work",
	}
}

func main() {
	if err := run(); err != nil {
		fmt.Println(err)
	}
}

```

### Readers
io 包指定了 io.Reader 接口， 它表示从数据流结尾读取。

Go 标准库包含了这个接口的许多实现， 包括文件、网络连接、压缩、加密等等。

io.Reader 接口有一个 Read 方法：

`func (T) Read(b []byte) (n int, err error)`
Read 用数据填充指定的字节 slice，并且返回填充的字节数和错误信息。 在遇到数据流结尾时，返回 io.EOF 错误。

例子代码创建了一个 strings.Reader。 并且以每次 8 字节的速度读取它的输出。

```go
package main

import (
	"fmt"
	"io"
	"strings"
)

func main() {
	r := strings.NewReader("Hello, Reader!")

	b := make([]byte, 8)
	for {
		n, err := r.Read(b)
		fmt.Printf("n = %v err = %v b = %v\n", n, err, b)
		fmt.Printf("b[:n] = %q\n", b[:n])
		if err == io.EOF {
			break
		}
	}
}

```

### Web 服务器
包 http 通过任何实现了 http.Handler 的值来响应 HTTP 请求：
```go
package http

type Handler interface {
    ServeHTTP(w ResponseWriter, r *Request)
}
```
在这个例子中，类型 Hello 实现了 http.Handler。

访问 http://localhost:4000/ 会看到来自程序的问候。

*注意：* 这个例子无法在基于 web 的指南用户界面运行。为了尝试编写 web 服务器，可能需要安装 Go。
```go
package main

import (
	"fmt"
	"log"
	"net/http"
)

type Hello struct{}

func (h Hello) ServeHTTP(
	w http.ResponseWriter,
	r *http.Request) {
	fmt.Fprint(w, "Hello!")
}

func main() {
	var h Hello
	err := http.ListenAndServe("localhost:4000", h)
	if err != nil {
		log.Fatal(err)
	}
}

```

### goroutine
goroutine 是由 Go 运行时环境管理的轻量级线程。

`go f(x, y, z)`
开启一个新的 goroutine 执行

`f(x, y, z)`
f，x，y 和 z 是当前 goroutine 中定义的，但是在新的 goroutine 中运行 f。

goroutine 在相同的地址空间中运行，因此访问共享内存必须进行同步。sync 提供了这种可能，不过在 Go 中并不经常用到，因为有其他的办法。（在接下来的内容中会涉及到。）
```go
package main

import (
	"fmt"
	"time"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}

func main() {
	go say("world")
	say("hello")
}
```

### channel
channel 是有类型的管道，可以用 channel 操作符 <- 对其发送或者接收值。
```go
ch <- v    // 将 v 送入 channel ch。
v := <-ch  // 从 ch 接收，并且赋值给 v。
```
（“箭头”就是数据流的方向。）

和 map 与 slice 一样，channel 使用前必须创建：

`ch := make(chan int)`
默认情况下，在另一端准备好之前，发送和接收都会阻塞。这使得 goroutine 可以在没有明确的锁或竞态变量的情况下进行同步。
```go
package main

import "fmt"

func sum(a []int, c chan int) {
	sum := 0
	for _, v := range a {
		sum += v
	}
	c <- sum // 将和送入 c
}

func main() {
	a := []int{7, 2, 8, -9, 4, 0}

	c := make(chan int)
	go sum(a[:len(a)/2], c)
	go sum(a[len(a)/2:], c)
	x, y := <-c, <-c // 从 c 中获取

	fmt.Println(x, y, x+y)
}
```

### 缓冲 channel
channel 可以是 带缓冲的。为 make 提供第二个参数作为缓冲长度来初始化一个缓冲 channel：

`ch := make(chan int, 100)`
向带缓冲的 channel 发送数据的时候，只有在缓冲区满的时候才会阻塞。 而当缓冲区为空的时候接收操作会阻塞。

修改例子使得缓冲区被填满，然后看看会发生什么。
```go
package main

import "fmt"

func main() {
	ch := make(chan int, 2)
	ch <- 1
	ch <- 2
	fmt.Println(<-ch)
	fmt.Println(<-ch)
}
```

### range 和 close
发送者可以 close 一个 channel 来表示再没有值会被发送了。接收者可以通过赋值语句的第二参数来测试 channel 是否被关闭：当没有值可以接收并且 channel 已经被关闭，那么经过

`v, ok := <-ch`
之后 ok 会被设置为 false。

循环 `for i := range c` 会不断从 channel 接收值，直到它被关闭。

*注意：* 只有发送者才能关闭 channel，而不是接收者。向一个已经关闭的 channel 发送数据会引起 panic。 *还要注意：* channel 与文件不同；通常情况下无需关闭它们。只有在需要告诉接收者没有更多的数据的时候才有必要进行关闭，例如中断一个 range。

```go
package main

import (
	"fmt"
)

func fibonacci(n int, c chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c)
}

func main() {
	c := make(chan int, 10)
	go fibonacci(cap(c), c)
	for i := range c {
		fmt.Println(i)
	}
}

```

### select
select 语句使得一个 goroutine 在多个通讯操作上等待。

select 会阻塞，直到条件分支中的某个可以继续执行，这时就会执行那个条件分支。当多个都准备好的时候，会随机选择一个。
```go
package main

import "fmt"

func fibonacci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

func main() {
	c := make(chan int)
	quit := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println(<-c)
		}
		quit <- 0
	}()
	fibonacci(c, quit)
}
```

### 默认选择
当 select 中的其他条件分支都没有准备好的时候，default 分支会被执行。

为了非阻塞的发送或者接收，可使用 default 分支：
```go
select {
case i := <-c:
    // 使用 i
default:
    // 从 c 读取会阻塞
}
```
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	tick := time.Tick(100 * time.Millisecond)
	boom := time.After(500 * time.Millisecond)
	for {
		select {
		case <-tick:
			fmt.Println("tick.")
		case <-boom:
			fmt.Println("BOOM!")
			return
		default:
			fmt.Println("    .")
			time.Sleep(50 * time.Millisecond)
		}
	}
}
```

### sync.Mutex
我们已经看到 channel 用来在各个 goroutine 间进行通信是非常合适的了。

但是如果我们并不需要通信呢？比如说，如果我们只是想保证在每个时刻，只有一个 goroutine 能访问一个共享的变量从而避免冲突？

这里涉及的概念叫做 互斥，通常使用 _互斥锁_(mutex)_来提供这个限制。

Go 标准库中提供了 sync.Mutex 类型及其两个方法：
```go
Lock
Unlock
```
我们可以通过在代码前调用 Lock 方法，在代码后调用 Unlock 方法来保证一段代码的互斥执行。 参见 Inc 方法。

我们也可以用 defer 语句来保证互斥锁一定会被解锁。参见 Value 方法。
```go
package main

import (
	"fmt"
	"sync"
	"time"
)

// SafeCounter 的并发使用是安全的。
type SafeCounter struct {
	v   map[string]int
	mux sync.Mutex
}

// Inc 增加给定 key 的计数器的值。
func (c *SafeCounter) Inc(key string) {
	c.mux.Lock()
	// Lock 之后同一时刻只有一个 goroutine 能访问 c.v
	c.v[key]++
	c.mux.Unlock()
}

// Value 返回给定 key 的计数器的当前值。
func (c *SafeCounter) Value(key string) int {
	c.mux.Lock()
	// Lock 之后同一时刻只有一个 goroutine 能访问 c.v
	defer c.mux.Unlock()
	return c.v[key]
}

func main() {
	c := SafeCounter{v: make(map[string]int)}
	for i := 0; i < 1000; i++ {
		go c.Inc("somekey")
	}

	time.Sleep(time.Second)
	fmt.Println(c.Value("somekey"))
}

```

### 接口/map/循环/range的使用
```go
package main

import (
	"fmt"
	"strconv"
	"strings"
)

type IPAddr [4]byte

func (ip IPAddr) String() string {
	var s []string
	for _, v := range ip {
		s = append(s, strconv.Itoa(int(v)))
	}
	return strings.Join(s, ".")
}

func main() {
	ip := IPAddr{127, 0, 0, 1}
	fmt.Println(ip)

	addrs := map[string]IPAddr{
		"loopback":  {127, 0, 0, 1},
		"googleDNS": {8, 8, 8, 8},
	}

	for k, v := range addrs {
		fmt.Printf("%v:%v\n", k, v)
	}
}
```

### 错误
```go
package main

import (
	"fmt"
	"strconv"
)

func main() {
	i, err := strconv.Atoi("4a2")
	if err != nil {
		fmt.Printf("couldn't convert number:%v\n", err)
		return
	}
	fmt.Println("Converted integer:", i) // couldn't convert number:strconv.Atoi: parsing "4a2": invalid syntax
}
```

### 模拟web服务器
```go
package main

import (
	"fmt"
	"log"
	"net/http"
)

type Hello struct{}

func (h Hello) ServeHTTP(
	w http.ResponseWriter,
	r *http.Request) {
	fmt.Fprint(w, "Hello!")
}

func main() {
	var h Hello
	err := http.ListenAndServe("localhost:4000", h)
	if err != nil {
		log.Fatal(err)
	}
}

```

### goroutine
```go
package main

import (
	"fmt"
	"time"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}

func main() {
	go say("world")
	say("hello")
}
```

### channel
```go
package main

import (
	"fmt"
)

func sum(a []int, c chan int) {
	sum := 0
	for _, v := range a {
		sum += v
	}
	c <- sum
}

func main() {
	a := []int{7, 2, 8, -9, 4, 0}

	c := make(chan int)
	go sum(a[:len(a)/2], c)
	go sum(a[len(a)/2:], c)
	x, y := <-c, <-c
	fmt.Println(x, y, x+y)
}

```

### 缓冲channel
```go
package main

import (
	"fmt"
)

func main() {
	ch := make(chan int, 2)
	ch <- 1
	ch <- 2
	fmt.Println(<-ch)
	fmt.Println(<-ch)
}

```

### range和close
```go
package main

import (
	"fmt"
)

func fibonacci(n int, c chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c)
}

func main() {
	c := make(chan int, 10)
	go fibonacci(cap(c), c)
	for i := range c {
		fmt.Println(i)
	}
}
```

###select
```go
package main

import (
	"fmt"
)

/*
	当c没有读出数据时，才会执行quit，因为c已经阻塞了
*/

func fibonacci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

func main() {
	c := make(chan int)
	quit := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println(<-c)
		}
		quit <- 0
	}()
	fibonacci(c, quit)
}

```

### 默认选择
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	tick := time.Tick(100 * time.Millisecond)
	boom := time.After(500 * time.Millisecond)
	for {
		select {
		case <-tick:
			fmt.Println("tick.")
		case <-boom:
			fmt.Println("BOOM!")
			return
		default:
			fmt.Println("   .")
			time.Sleep(50 * time.Millisecond)
		}
	}
}

```

### sync.Mutex
```go
package main

import (
	"fmt"
	"sync"
	"time"
)

type SafeCounter struct {
	v   map[string]int
	mux sync.Mutex
}

func (c *SafeCounter) Inc(key string) {
	c.mux.Lock()
	c.v[key]++
	c.mux.Unlock()
}

func (c *SafeCounter) Value(key string) int {
	c.mux.Lock()
	defer c.mux.Unlock()
	return c.v[key]
}

func main() {
	c := SafeCounter{v: make(map[string]int)}
	for i := 0; i < 1000; i++ {
		go c.Inc("somekey")
	}
	time.Sleep(time.Second)
	fmt.Println(c.Value("somekey"))
}
```

## 目录结构
转自:http://blog.studygolang.com/2012/12/go%E9%A1%B9%E7%9B%AE%E7%9A%84%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84/

项目目录结构如何组织，一般语言都是没有规定。但Go语言这方面做了规定，这样可以保持一致性
1. 一般的，一个Go项目在GOPATH下，会有如下三个目录：
```
|--bin
|--pkg
|--src
```
其中，bin存放编译后的可执行文件；pkg存放编译后的包文件；src存放项目源文件。一般，bin和pkg目录可以不创建，go命令会自动创建（如 go install），只需要创建src目录即可。
对于pkg目录，曾经有人问：我把Go中的包放入pkg下面，怎么不行啊？他直接把Go包的源文件放入了pkg中。这显然是不对的。pkg中的文件是Go编译生成的，而不是手动放进去的。（一般文件后缀.a）
对于src目录，存放源文件，Go中源文件以包（package）的形式组织。通常，新建一个包就在src目录中新建一个文件夹。

2. 举例说明
比如：我新建一个项目，test，开始的目录结构如下：
```
test--|--src
```
为了编译方便，我在其中增加了一个install文件，目录结构：
```
test/
|-- install
`-- src
```
其中install的内容如下：（linux下）

```bash
#!/usr/bin/env bash
if [ ! -f install ]; then
echo 'install must be run within its container folder' 1>&2
exit 1
fi

CURDIR=`pwd`
OLDGOPATH="$GOPATH"
export GOPATH="$CURDIR"

gofmt -w src

go install test

export GOPATH="$OLDGOPATH"

echo 'finished'
```

之所以加上这个install，是不用配置GOPATH（避免新增一个GO项目就要往GOPATH中增加一个路径）

接下来，增加一个包：config和一个main程序。目录结构如下：
```
test
|-- install
`-- src
    |-- config
    |   `-- config.go
    `-- test
        `-- main.go
```
注意，config.go中的package名称必须最好和目录config一致，而文件名可以随便。main.go表示main包，文件名建议为main.go。（注：不一致时，生成的.a文件名和目录名一致，这样，在import 时，应该是目录名，而引用包时，需要包名。例如：目录为myconfig，包名为config，则生产的静态包文件是：myconfig.a，引用该包：import “myconfig”，使用包中成员：config.LoadConfig()）

config.go和main.go的代码如下：

config.go代码
```go
package config
 
func LoadConfig() {
 
}
```

main.go代码
```go
package main
 
import (
    "config"
    "fmt"
)
 
func main() {
    config.LoadConfig()
    fmt.Println("Hello, GO!")
}
```
接下来，在项目根目录执行./install

这时候的目录结构为：
```
test
|-- bin
|   `-- test
|-- install
|-- pkg
|   `-- linux_amd64
|       `-- config.a
`-- src
    |-- config
    |   `-- config.go
    `-- test
        `-- main.go
```
（linux_amd64表示我使用的操作系统和架构，你的可能不一样）
其中config.a是包config编译后生成的；bin/test是生成的二进制文件

这个时候可以执行：bin/test了。会输出：Hello, GO!

3. 补充说明
	1. 包可以多层目录，比如：net/http包，表示源文件在src/net/http目录下面，不过源文件中的包名是最后一个目录的名字，如http
而在import包时，必须完整的路径，如：import “net/http”

	2. 有时候会见到local import（不建议使用），语法类似这样：

import “./config”

当代码中有这样的语句时，很多时候都会见到类似这样的错误：local import “./config” in non-local package

我所了解的这种导入方式的使用是：当写一个简单的测试脚本，想要使用go run命令时，可以使用这种导入方式。
比如上面的例子，把test/main.go移到src目录中，test目录删除，修改main.go中的import “config”为import “./config”，然后可以在src目录下执行：go run main.go

可见，local import不依赖于GOPATH

4. Windows下的install.bat

```
@echo off
 
setlocal
 
if exist install.bat goto ok
echo install.bat must be run from its folder
goto end
 
:ok
 
set OLDGOPATH=%GOPATH%
set GOPATH=%~dp0
 
gofmt -w src
 
go install test
 
:end
echo finished
```
注,冒号和ok之间不应该有空格，但是放在一起总是会被wordpress转成一个表情。汗……

5、更新日志
1）2012-12-05 发布
2）2013-04-13 修正：目录名可以和包名不同，但建议一致；将make文件名改为install

## fmt.Printf的使用

```
Fmt包  
  
import "fmt"  
  
简介 ▾  
  
Package fmt包含有格式化I/O函数，类似于C语言的printf和scanf。格式字符串的规则来源于C但更简单一些。  
  
输出  
  
格式：  
  
一般：  
  
%v   基本格式的值。当输出结构体时，扩展标志(%+v)添加成员的名字。the value in a default format.  
  
     when printing structs, the plus flag (%+v) adds field names  
  
%#v  值的Go语法表示。  
  
%T   值的类型的Go语法表示。  
  
%%   百分号。  
  
布尔型：  
  
%t   值的true或false  
  
整型：  
  
%b   二进制表示  
  
%c   数值对应的Unicode编码字符  
  
%d   十进制表示  
  
%o   八进制表示  
  
%q   字节转化成字符
  
%x   十六进制表示，使用a-f  
  
%X   十六进制表示，使用A-F  
  
%U   Unicode格式： U+1234，等价于"U+%04X"  
  
浮点数：  
  
%b   无小数部分、两位指数的科学计数法，和strconv.FormatFloat的'b'转换格式一致。举例：-123456p-78  
  
%e   科学计数法，举例：-1234.456e+78  
  
%E   科学计数法，举例：-1234.456E+78  
  
%f   有小数部分，但无指数部分，举例：123.456  
  
%g   根据实际情况采用%e或%f格式（以获得更简洁的输出）  
  
%G   根据实际情况采用%E或%f格式（以获得更简洁的输出）  
  
字符串和byte切片类型：  
  
%s   直接输出字符串或者[]byte  
  
%q   双引号括起来的字符串  
  
%x   每个字节用两字符十六进制数表示（使用小写a-f）  
  
%X   每个字节用两字符十六进制数表示（使用大写A-F）  
  
指针：  
  
%p   0x开头的十六进制数表示  
  
木有'u'标志。如果是无类型整数，自然会打印无类型格式。类似的，没有必要去区分操作数的大小(int8, int64)。  
  
宽度和精度格式化控制是指的Unicode编码字符的数量（不同于C的printf，它的这两个因子指的是字节的数量。）两者均可以使用'*'号取代（任一个或两个都），此时它们的值将被紧接着的参数控制，这个操作数必须是整型。  
  
对于数字，宽度设置总长度，精度设置小数部分长度。例如，格式%6.2f 输出123.45。  
  
对于字符串，宽度是输出字符数目的最低数量，如果不足会用空格填充。精度是输出字符数目的最大数量，超过则会截断。  
  
其它符号：  
  
+    总是输出数值的正负号；对%q(%+q)将保证纯ASCII码输出  
  
-    用空格在右侧填充空缺而不是默认的左侧。  
  
#    切换格式：在八进制前加0(%#o)，十六进制前加0x(%#x)或0X(%#X)；废除指针的0x(%#p)；  
  
     对%q (%#q)如果可能的话输出一个无修饰的字符串；  
  
     对%U(%#U)如果对应数值是可打印字符输出该字符。  
  
' '  对数字(% d)空格会留一个空格在数字前并忽略数字的正负号；  
  
     对切片和字符串(% x, % X)会以16进制输出。  
  
0    用前置0代替空格填补空缺。  
  
每一个类似Printf的函数，都会有一个同样的Print函数，此函数不需要format字符串，等价于对每一个参数设置为%v。另一个变体Println会在参数之间加上空格并在输出结束后换行。  
  
如果参数是一个接口值，将使用内在的具体实现的值，而不是接口本身，%v参数不会被使用。如下：  
  
var i interface{} = 23  
  
fmt.Printf("%v\n", i)  
  
将输出23。  
  
如果参数实现了Formatter接口，该接口可用来更好的控制格式化。  
  
如果格式（标志对Println等是隐含的%v）是专用于字符串的(%s %q %v %x %X)，还提供了如下两个规则：  
  
1. 如果一个参数实现了error接口，Error方法会用来将目标转化为字符串，随后将被按给出的要求格式化。  
  
2. 如果参数提供了String方法，这个方法将被用来将目标转换为字符串，然后将按给出的格式标志格式化。  
  
为了避免有可能的递归循环，例如：  
  
type X string  
  
func (x X) String() string { return Sprintf("<%s>", x) }  
  
会在递归循环前转换值：  
  
func (x X) String() string { return Sprintf("<%s>", string(x)) }  
  
错误的格式：  
  
如果提供了一个错误的格式标志，例如给一个字符串提供了%d标志，生成的字符串将包含对该问题的描述，如下面的例子：  
  
错误或未知的格式标志: %!verb(type=value)  
  
     Printf("%d", hi):          %!d(string=hi)  
  
太多参数: %!(EXTRA type=value)  
  
     Printf("hi", "guys"):      hi%!(EXTRA string=guys)  
  
缺少参数: %!verb(MISSING)  
  
     Printf("hi%d"):            hi %!d(MISSING)  
  
使用非整数提供宽度和精度: %!(BADWIDTH) or %!(BADPREC)  
  
     Printf("%*s", 4.5, "hi"):  %!(BADWIDTH)hi  
  
     Printf("%.*s", 4.5, "hi"): %!(BADPREC)hi  
  
所有的错误都使用"%!"起始，（紧随单字符的格式标志）以括号包围的错误描述结束。  
  
输入  
  
一系列类似的函数读取格式化的文本，生成值。Scan，Scanf和Scanln从os.Stdin读取；Fscan，Fscanf和Fscanln 从特定的io.Reader读取；Sscan，Sscanf和Sscanln 从字符串读取；Scanln，Fscanln和Sscanln在换行时结束读取，并要求数据连续出现；Scanf，Fscanf和Sscanf会读取一整行以匹配格式字符串；其他的函数将换行看着空格。  
  
Scanf, Fscanf, and Sscanf根据格式字符串解析数据，类似于Printf。例如，%x将读取一个十六进制数，%v将读取值的默认表示。  
  
格式行为类似于Printf，但有如下例外：  
  
%p没有提供  
  
%T没有提供  
  
%e %E %f %F %g %G是等价的，都可以读取任何浮点数或者复合数（非复数，指科学计数法表示的带指数的数）  
  
%s 和 %v字符串使用这两个格式读取时会因为空格而结束  
  
不设格式或者使用%v读取整数时，如果前缀为0(八进制)或0x(十六进制)，将按对应进制读取。  
  
宽度在输入中被解释（%5s意思是最多从输入读取5个字符赋值给一个字符串），但输入系列函数没有解释精度的语法(木有%5.2f，只有%5f)。  
  
输入系列函数中的格式字符串，所有非空的空白字符（除了换行符之外），无论在输入里还是格式字符串里，都等价于1个空白字符。格式字符串必须匹配输入的文本，如果不匹配将停止读取数据并返回函数已经赋值的参数的数量。  
  
所有的scan系列函数，如果参数包含Scan方法（或者说实现了Scanner接口），该参数将使用该方法读取文本。另外，如果被填写的参数的数量少于提供的参数的数量，将返回一个错误。  
  
所有要被输入的参数都应该是基础类型或者实现了Scanner接口的数据类型的指针。  
  
注意：Fscan等函数可以从输入略过一些字符读取需要的字符并返回，这就意味着一个循环的读取程序可能会跳过输入的部分数据。当数据间没有空白时就会导致出现问题。如果读取这提供给Fscan系列函数ReadRune 方法，这个方法可以用来读取字符。如果读取者还提供了UnreadRune 方法，该方法将被用来保存字符以使成功的调用不会丢失数据。为了给一个没有这些功能的读取者添加这俩方法，使用bufio.NewReader。 
```

## 资源整理
1. Learning Go 《学习Go语言》
[英文版](http://www.miek.nl/projects/learninggo/)
[中文版](http://mikespook.com/learning-go/)

2. [Go by Example](https://gobyexample.com/)
Go is an open source programming language designed for building simple, fast, and reliable software.
Go by Example is a hands-on introduction to Go using annotated example programs. Check out the first exampleor browse the full list below.

3. [Network programming with Go](http://jan.newmarch.name/go/)
An e-book on building network applications using the Google Go programming language (golang)

4. [goroutine背后的系统知识](http://www.sizeofvoid.net/goroutine-under-the-hood/)
Go语言从诞生到普及已经三年了，先行者大都是Web开发的背景，也有了一些普及型的书籍，可系统开发背景的人在学习这些书籍的时候，总有语焉不详的感觉，网上也有若干流传甚广的文章，可其中或多或少总有些与事实不符的技术描述。希望这篇文章能为比较缺少系统编程背景的Web开发人员介绍一下goroutine背后的系统知识。
	1. 操作系统与运行库
	2. 并发与并行 (Concurrency and Parallelism)
	3. 线程的调度
	4. 并发编程框架
	5. goroutine

5. [An Introduction to Programming in Go.](http://www.golang-book.com/)

6. [《Go Web 编程》](https://github.com/astaxie/build-web-application-with-golang/blob/master/ebook/preface.md)

7. [Go语言博客实践](https://github.com/achun/Go-Blog-In-Action)
Go Blog In Action 中文名 Go语言博客实践. 是对 TypePress 开发过程中的想法, 方法, 探讨等任何方面同步整理成的电子书.

8. [go samples when learning golang.](https://github.com/philsong/golang_samples)
大量实操的例子

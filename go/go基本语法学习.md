# go基本语法学习

[TOC]

## 循环

- 方式1
```go
i := []int{1, 2, 8, 4, 5}
for k, v := range i {
	fmt.Println(k, v)
}
```

- 方式2
```go
for i := 0; i < 10; i++ {
	fmt.Println(i)
}
```

- 方式3
```go
i := 0
for i < 10 {
	fmt.Println(i)
}
```

- 方式4
```go
i := 0
for {
	i++
	if i%2 == 0 {
		continue
	} else if i > 15 {
		break
	}
	fmt.Println(i)
}
```

## switch

- 基本用法
```go
test := 10
switch test {
case 1:
	fmt.Println("111")
case 10:
	fmt.Println("101010")
	fallthrough
default:
	fmt.Println("unknown")
}
```

- 代替if/else用法
```go
test := 10
switch {
case test < 10:
	fmt.Println("111")
case test < 100:
	fmt.Println("101010")
	fallthrough
default:
	fmt.Println("unknown")
}
```
```go
if i := 10; i < 100 {	// 可以直接赋值参数
	fmt.Println("1")
} else {
	fmt.Println("2")
}
```

## 数组

- 固定类型
- 固定长度
- 内存连续
- 多维数组有效

```go
var a [5]int
for i := 0; i < len(a); i++ {
	a[i] = i * i
}
for _, v := range a {
	fmt.Println(v)
}
```

## slice

就是链表

- 块内使用
以下测试显示出了需要注意的地方
`sa=sb`时，如果cap不发生改变,
`sa`/`sb`为引用关系，修改任意一方会导致另一个也发生变化。
cap变化后`sa`/`sb`完全脱离引用，修改不会导致另一方发生变化。
`copy`函数提供了深拷贝的方法，使双方完全独立互不影响。

```go
a := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
fmt.Println(a, len(a), cap(a))
b := a[:2]
c := a[8:]
d := a[1:3]
fmt.Println(b, len(b), cap(b))
fmt.Println(c, len(c), cap(c))
fmt.Println(d, len(d), cap(d))
d[0] = 10
fmt.Println(d, len(d), cap(d), a)
d = append(d, 11)
fmt.Println(d, len(d), cap(d), a)
c[0] = 12
fmt.Println(c, len(c), cap(c), a)
c = append(c, 13)
fmt.Println(c, len(c), cap(c), a)
c[1] = 14
fmt.Println(c, len(c), cap(c), a)

a = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
b = a
e := make([]int, len(a))
copy(e, a)
fmt.Println(a, len(a), cap(a))
fmt.Println(b, len(b), cap(b))
fmt.Println(e, len(e), cap(e))
a[0] = 10
fmt.Println(a, len(a), cap(a))
fmt.Println(b, len(b), cap(b))
fmt.Println(e, len(e), cap(e), "eee")
a = append(a, 11)
fmt.Println(a, len(a), cap(a))
fmt.Println(b, len(b), cap(b))
```

- 函数调用

同上，只要cap不发生变化，修改的就是原始数据

```go
func main() {
	a := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
	t1(a)
	fmt.Println(a)
}

func t1(x []int) {
	x[0] = 100
	x = append(x, 200)
	x[1] = 300
}
```

## map

```go
var m map[string]string
m = make(map[string]string)
fmt.Println(m)
m["a"] = "aaa"
m["b"] = "bbb"
fmt.Println(m)
m["b"] = "ccc"
for k, v := range m {
	fmt.Printf("%s=>%s\n", k, v)
}
k, v := m["b"]
k1, v1 := m["c"]
fmt.Println(k, v, m["b"])
fmt.Println(k1, v1, m["c"])
delete(m, "b")
fmt.Println(m)

m1 := map[string]int{"a": 1, "b": 2}
fmt.Println(m1)
```

## 多返回值

==多返回不能只获得第一个参数，返回几个值就要接收几个值，不能省略参数==

```go
func main() {
	a, b := t2()
	fmt.Println(a, b)
}

func t2() (int, int) {
	// panic("abcde")
	return 1, 2
}
```

## 可变参数

++可以接收0+个同数据类型参数的函数，数组slice可以解包传入++
*参数没有默认值，没有重载*

```go
func main() {
	fmt.Println(t3(1, 2, 3, 4, 5))
	fmt.Println(t3(2, 3, 4, 5))
	fmt.Println(t3(5))
	fmt.Println(t3())
	nums := []int{3, 4, 5}
	fmt.Println(t3(nums...))
}

func t3(nums ...int) (sum int) {
	for _, v := range nums {
		sum += v
	}
	return
}
```

## closure

闭包，生成器

```go
func main() {
	one := t4()
	fmt.Println(one())
	fmt.Println(one())
	fmt.Println(one())
	two := t4()
	fmt.Println(two())
	fmt.Println(two())
	fmt.Println(one())
	fmt.Println(two())

	for i := one(); i < 10; i = one() {
		fmt.Println(i)
	}
}

func t4() func() int {
	i := 0
	return func() int {
		i += 1
		return i
	}
}
```

## 递归

```go
func main() {
	fmt.Println(t5(7))
}

func t5(n int) int {
	if n == 0 {
		return 1
	}
	return n * t5(n-1)
}
```

## 指针

`&`取地址
`*`解引用

## 结构体

```go
func main() {
	fmt.Println(person{"p", 10})
	fmt.Println(person{name: "pp", age: 20})
	fmt.Println(person{name: "ppp"})
	fmt.Println(person{age: 30})
	fmt.Println(&person{name: "pppp"})
	p1 := &person{"ppppp", 40}
	p2 := p1
	p2.name += "q"
	fmt.Println(p1, p2)
	fmt.Println(&p1, &p2)
	i := &person{}
	p2 = i
	fmt.Println(&p1, &p2, &i, p2, i)
	p2.name = "a"
	fmt.Println(p2, i)
}

type person struct {
	name string
	age  int
}
```

## 方法

==一般都应使用指针作为类方法的参数==

```go
unc main() {
	r := rect{height: 20, width: 10}
	fmt.Println(r.area())
	fmt.Println(r.perim())
	r.extend()
	fmt.Println(r)
	r.extendp()
	fmt.Println(r)
	r.extendpby(10)
	fmt.Println(r)
}

type rect struct {
	width, height int
}

func (r *rect) area() int {
	return r.width * r.height
}

func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func (r *rect) extendp() {
	r.width *= 2
	r.height *= 2
}

func (r rect) extend() {
	r.width *= 2
	r.height *= 2
}

func (r *rect) extendpby(rate int) {
	r.width *= rate
	r.height *= rate
}
```

## 接口

感觉写法有点奇怪，使用接口作为参数时，注意不要使用接口的指针

```go
type geomety interface {
	area() float64
	perim() float64
}

type rect struct {
	width, height float64
}

type circle struct {
	radius float64
}

func (r *rect) area() float64 {
	return r.width * r.height
}

func (r *rect) perim() float64 {
	return 2*r.width + 2*r.height
}

func (c *circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c *circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

func measure(g geomety) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	r := rect{width: 10, height: 20}
	c := circle{radius: 5}

	measure(&r)
	measure(&c)
}

```

## 接口转换回原型的方法

`__原型转换结果,是否转换成功:=接口类型.(*原型)__`
不能直接强制转换

```txt
type act interface {
	area() int
}

type rect struct {
	w, h int
}

type circle struct {
	r int
}

func (r *rect) area() int {
	return r.w * r.h
}

func (c *circle) area() int {
	return 3 * c.r
}

func t9(a act) {
	fmt.Println(a.area())
	if b, ok := a.(*rect); ok {
		fmt.Println("ok:", b)
	} else {
		fmt.Println("not ok")
	}
}

func main() {
	r := rect{10, 20}
	t9(&r)

	c := circle{10}
	t9(&c)
}
```

## 错误

```go
func f7(i int) (int, error) {
	if (i % 2) == 0 {
		return 0, errors.New("error even")
	} else {
		return i, nil
	}
}

type T8Error struct {
	arg  int
	info string
}

func (e *T8Error) Error() string {
	return fmt.Sprintf("%d->%s", e.arg, e.info)
}

func t8(i int) (int, error) {
	if (i % 2) == 0 {
		return 0, &T8Error{i, "error even t8"}
	} else {
		return i, nil
	}
}

func main() {
	for i := 0; i < 10; i++ {
		if r, e := f7(i); e != nil {
			fmt.Println(e)
		} else {
			fmt.Println(r)
		}
	}

	fmt.Println("...")

	for i := 0; i < 10; i++ {
		if r, e := t8(i); e != nil {
			fmt.Println(e)
		} else {
			fmt.Println(r)
		}
	}
}
```

## goroutine

```go
func f10(info string) {
	for i := 0; i < 3; i++ {
		fmt.Println(info, "->", i)
	}
}

func main() {
	f10("a")
	go f10("b")
	go func(info string) {
		fmt.Println("info:", info)
	}("going")

	var input string
	fmt.Scanln(&input)
	fmt.Println("done")
}
```

## channel

是阻塞的，用于不同的routine数据传输

```go
func main() {
	m := make(chan string)
	go func() { m <- "ping" }()
	msg := <-m
	fmt.Println(msg)
}
```

有buffer长度的channel
超过长度会报错(没有线程可以继续运行的情况下，就是说在非主线程里下面的注释代码不会有问题)
```go
func main() {
	m := make(chan string, 2)
	m <- "a"
	fmt.Println(<-m)
	m <- "b"
	m <- "c"
	fmt.Println(<-m)
	fmt.Println(<-m)
	// m <- "d"
	// m <- "e"
	// m <- "f"
	// fmt.Println(<-m)
	// fmt.Println(<-m)
	// fmt.Println(<-m)
}
```

==无缓冲与缓冲长度是1的是完全不同的概念，无缓冲只要读/写一次数据就会阻塞，缓冲长度是1的第一次读/写数据不会阻塞，只会在后面一次==

我们在初始化一个通道时将其容量设置成0，或者直接忽略对容量的设置，那么就称之为非缓冲通道
```go
ch1 := make(chan int, 1) //缓冲通道
ch2 := make(chan int, 0) //非缓冲通道
ch3 := make(chan int) //非缓冲通道
```
1. 向此类通道发送元素值的操作会被阻塞，直到至少有一个针对该通道的接收操作开始进行为止。
2. 从此类通道接收元素值的操作会被阻塞，直到至少有一个针对该通道的发送操作开始进行为止。
3. 针对非缓冲通道的接收操作会在与之相应的发送操作完成之前完成。
对于第三条要特别注意，发送操作在向非缓冲通道发送元素值的时候，会等待能够接收该元素值的那个接收操作。并且确保该元素值被成功接收，它才会真正的完成执行。而缓冲通道中，刚好相反，由于元素值的传递是异步的，所以发送操作在成功向通道发送元素值之后就会立即结束(它不会关心是否有接收操作)。

## routine的同步

下面的方式使用chan相当于其他语言的join()

```go
func t11(c chan bool) {
	fmt.Println("work start")
	time.Sleep(time.Second)
	fmt.Println("work done")
	c <- true
}

func main() {
	c := make(chan bool)
	go t11(c)

	fmt.Println("wait")
	<-c
	fmt.Println("done")
}

```

## select

```go
func main() {
	c1 := make(chan string)
	c2 := make(chan string)

	go func() {
		time.Sleep(time.Second)
		c1 <- "one"
	}()

	go func() {
		time.Sleep(time.Second * 2)
		c2 <- "two"
	}()

	for i := 0; i < 2; i++ {
		select {
		case m1 := <-c1:
			fmt.Println(m1)
		case m2 := <-c2:
			fmt.Println(m2)
		}
	}
}
```

## timer和ticker

ticker是重复执行同一个任务的，timer是一段时间后执行一次任务的

```ticker
func main() {
	ticker := time.NewTicker(time.Second)

	go func() {
		for i := range ticker.C {
			fmt.Println("输出内容:", i)
		}
	}()

	time.Sleep(time.Second * 5)
	ticker.Stop()
	fmt.Println("done")
}
```

## 字符串格式化输出

符号 | 功能
-|
%v|各种数据
%+v|含有字段名的各种数据
%#v|含有包名.类名的各种数据
%T|数据类型
%t|bool类型
%d|10进制数字
%b|2进制
%f|浮点数
%c|数字转char
%x|数字转16进制
%e|科学计数法
%p|指针地址
%s|字符串

%后各种数字的规范同C++

```go
type point struct {
	x, y int
}

func main() {

	// Go offers several printing "verbs" designed to
	// format general Go values. For example, this prints
	// an instance of our `point` struct.
	p := point{1, 2}
	fmt.Printf("%v\n", p)

	// If the value is a struct, the `%+v` variant will
	// include the struct's field names.
	fmt.Printf("%+v\n", p)

	// The `%#v` variant prints a Go syntax representation
	// of the value, i.e. the source code snippet that
	// would produce that value.
	fmt.Printf("%#v\n", p)

	// To print the type of a value, use `%T`.
	fmt.Printf("%T\n", p)

	// Formatting booleans is straight-forward.
	fmt.Printf("%t\n", true)

	// There are many options for formatting integers.
	// Use `%d` for standard, base-10 formatting.
	fmt.Printf("%d\n", 123)

	// This prints a binary representation.
	fmt.Printf("%b\n", 14)

	// This prints the character corresponding to the
	// given integer.
	fmt.Printf("%c\n", 33)

	// `%x` provides hex encoding.
	fmt.Printf("%x\n", 456)

	// There are also several formatting options for
	// floats. For basic decimal formatting use `%f`.
	fmt.Printf("%f\n", 78.9)

	// `%e` and `%E` format the float in (slightly
	// different versions of) scientific notation.
	fmt.Printf("%e\n", 123400000.0)
	fmt.Printf("%E\n", 123400000.0)

	// For basic string printing use `%s`.
	fmt.Printf("%s\n", "\"string\"")

	// To double-quote strings as in Go source, use `%q`.
	fmt.Printf("%q\n", "\"string\"")

	// As with integers seen earlier, `%x` renders
	// the string in base-16, with two output characters
	// per byte of input.
	fmt.Printf("%x\n", "hex this")

	// To print a representation of a pointer, use `%p`.
	fmt.Printf("%p\n", &p)

	// When formatting numbers you will often want to
	// control the width and precision of the resulting
	// figure. To specify the width of an integer, use a
	// number after the `%` in the verb. By default the
	// result will be right-justified and padded with
	// spaces.
	fmt.Printf("|%6d|%6d|\n", 12, 345)

	// You can also specify the width of printed floats,
	// though usually you'll also want to restrict the
	// decimal precision at the same time with the
	// width.precision syntax.
	fmt.Printf("|%6.2f|%6.2f|\n", 1.2, 3.45)

	// To left-justify, use the `-` flag.
	fmt.Printf("|%-6.2f|%-6.2f|\n", 1.2, 3.45)

	// You may also want to control width when formatting
	// strings, especially to ensure that they align in
	// table-like output. For basic right-justified width.
	fmt.Printf("|%6s|%6s|\n", "foo", "b")

	// To left-justify use the `-` flag as with numbers.
	fmt.Printf("|%-6s|%-6s|\n", "foo", "b")

	// So far we've seen `Printf`, which prints the
	// formatted string to `os.Stdout`. `Sprintf` formats
	// and returns a string without printing it anywhere.
	s := fmt.Sprintf("a %s", "string")
	fmt.Println(s)

	// You can format+print to `io.Writers` other than
	// `os.Stdout` using `Fprintf`.
	fmt.Fprintf(os.Stderr, "an %s\n", "error")
}
```
```go
{1 2}
an error
{x:1 y:2}
main.point{x:1, y:2}
main.point
true
123
1110
!
1c8
78.900000
1.234000e+08
1.234000E+08
"string"
"\"string\""
6865782074686973
0xc0420381d0
|    12|   345|
|  1.20|  3.45|
|1.20  |3.45  |
|   foo|     b|
|foo   |b     |
a string
```

## 排序

- 基本使用方法

```go
func main() {
	arr := []int{5, 2, 0, 8, 3, 6}
	fmt.Println(arr, sort.IntsAreSorted(arr))
	sort.Ints(arr)
	fmt.Println(arr, sort.IntsAreSorted(arr))
}
```

- 自定义排序

按照分数从低到高排序

```go
package main

import (
	"fmt"
	"sort"
)

type Student struct {
	name  string
	score int
}

type StuArr []Student

func (arr StuArr) Len() int {
	return len(arr)
}

func (arr StuArr) Swap(x, y int) {
	arr[x], arr[y] = arr[y], arr[x]
}

func (arr StuArr) Less(x, y int) bool {
	return arr[x].score < arr[y].score
}

func main() {
	arr := StuArr{{"a", 20}, {"b", 30}, {"c", 10}}
	fmt.Printf("%+v\n", arr)
	sort.Sort(arr)
	fmt.Printf("%+v\n", arr)
}

```

## 简易单元测试

hello.go
```go
package hello

func hello() string {
	words := []string{"hello", "func", "in", "package", "hello"}
	wl := len(words)

	sentence := ""
	for key, word := range words {
		sentence += word
		if key < wl-1 {
			sentence += " "
		} else {
			sentence += "."
		}
	}
	return sentence
}
```
hello_test.go
```go
package hello

import (
	"fmt"
	"testing"
)

func TestHello(t *testing.T) {
	got := hello()
	expect := "hello func in package hello."

	if got != expect {
		t.Errorf("got [%s] expected [%s]", got, expect)
	}
}

func BenchmarkHello(b *testing.B) {
	for i := 0; i < b.N; i++ {
		hello()
	}
}

func ExampleHello() {
	hl := hello()
	fmt.Println(hl)
	// Output:hello func in package hello.
}
```
测试命令
```go
go test
go test -v
go test -v -bench
go test -v -bench -cover
```

## 杂项

- `if`只能使用`bool`值类判断，`0`/`nil`/`""`等空值无法代替
- `if`/`for`条件语句中声明的变量其他地方无法使用，但是在`else`里面可以
- 参数列表没有默认值
- 没有继承
- 接口实现不需要`implement`
- 指针用法和实例用法相同都是用`.`
- 支持多行注释`/**/`
- 没有`++i`这种功能
- `switch`可以当连续的`if`语句使用
- `defer`会简化写法，像是`finally`一样的功能
- `slice`的看似是引用的方法用起来十分危险
- 自定义排序要实现的sort接口要有三个函数
- map的key顺序是随机的，无法根据key进行自动排序
- 局部变量使用范围
```go
func main() {
	for _, v := range []int{1, 2, 3} {
		v := v + 10
		fmt.Println(v)
	}
	v := 10
	fmt.Println(v)
	for _, v := range []int{1, 2, 3} {
		v := v + 10
		fmt.Println(v)
	}
	fmt.Println(v)
	{
		v++
		fmt.Println(v)
		v := 20
		fmt.Println(v)
		v++
		fmt.Println(v)
	}
	fmt.Println(v)
}
```
```go
11
12
13
10
11
12
13
10
11
20
21
11
```

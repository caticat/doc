# Redis学习笔记

[TOC]

[新手教程地址](http://blog.csdn.net/wq343502916/article/details/47405977)

## 程序结构

./redis-benchmark //用于进行redis性能测试的工具
./redis-check-dump //用于修复出问题的dump.rdb文件
./redis-cli //redis的客户端
./redis-server //redis的服务端
./redis-check-aof //用于修复出问题的AOF文件
./redis-sentinel //用于集群管理

## 启动

`./redis-server ../redis.conf`
`redis.conf`为配置文件，可以修改端口

## 使用客户端

- 直接使用
`./redis-cli`

- 修改端口后使用
`./redis-cli -p 9903`

- 测试操作
	- 设置
			set pan "pa works"	// OK
	- 读取
			get pan	// "pa works"
	- 删除
			del pan	// (integer)1
	- 退出
			quit
	- 查看类型
			type pan
	- 可能报错
			(error) WRONGTYPE Operation against a key holding the wrong kind of value
			就是操作数据用的命令错了，需要使用对应数据类型的命令来操作。
			string可以使用get/set，但是hash需要使用hget/hset。

## 简介

redis是一种高级的key:value存储系统，其中value支持五种数据类型：
1. 字符串（strings）
2. 字符串列表（lists）
3. 字符串集合（sets）
4. 有序字符串集合（zset|sorted sets）
5. 哈希（hashes）

而关于key，有几个点要提醒大家：
1. key不要太长，尽量不要超过1024字节，这不仅消耗内存，而且会降低查找的效率；
2. key也不要太短，太短的话，key的可读性会降低；
3. 在一个项目中，key最好使用统一的命名模式，例如user:10000:passwd。

## 基本字符串操作

```redis
> set pan "2"
OK
> type pan
string
> incr pan
(integer) 3
> get pan
"3"
> incrby pan 2
"5"
> decr pan
(inter) 4
> del pan
(integer) 1
```

## lists

就是链表(不是数组)

### 常用方法
- lpush
- rpush
- lrange

### 例子
```redis
> lpush pan "1"
(integer) 1
> rpush pan "2"
(integer) 2
> lpush pan "0"
(integer) 3
> lrange pan 0 1
1) "0"
2) "1"
> lrange pan 0 -1
1) "0"
2) "1"
3) "2"
```

## 集合

set

```redis
>sadd pan "a"
(integer) 1
>sadd pan "b"
(integer) 1
> type pan
set
>smembers pan
1) "b"
2) "a"
```

## 有序集合

sorted sets(zsets)

```redis
>zadd pan 1 "baidu"
(integer) 1
>zadd pan 2 "qq"
(integer) 1
>zadd pan 0 "taobao"
(integer) 1
>zrange pan 0 -1
1) taobao
2) baidu
3) qq
>zrange pan 0 -1 withscores
1) taobao
2) "0"
3) baidu
4) "1"
5) qq
6) "2"
```

## 哈希

就是hashmap

```redis
> hmset pan name "pan" age 31
OK
> hgetall pan
1) "name"
2) "pan"
3) "age"
4) "31"
> hget pan name
"pan"
> hget pan age
"31"
> hset pan age 13
(integer) 0
> hget pan age
"13"
```

## redis持久化

两种方式
- RDB(Redis DataBase)
	就是在不同的时间点，将redis存储的数据生成快照并存储到磁盘等介质上
- AOF(Append Only File)
	是换了一个角度来实现持久化，那就是将redis执行过的所有写指令记录下来，在下次redis重新启动时，只要把这些写指令从前到后再重复执行一遍，就可以实现数据恢复了。

## 事物

1. `multi`组装
2. `exec`执行
3. `discard`取消
4. `watch`监视key，再key变化时取消执行

```redis
redis> MULTI //标记事务开始
OK
redis> INCR user_id //多条命令按顺序入队
QUEUED
redis> INCR user_id
QUEUED
redis> INCR user_id
QUEUED
redis> PING
QUEUED
redis> EXEC //执行
1) (integer) 1
2) (integer) 2
3) (integer) 3
4) PONG
```

- 调用exec之前的错误
有可能是由于语法有误导致的，也可能时由于内存不足导致的。只要出现某个命令无法成功写入缓冲队列的情况，redis都会进行记录，在客户端调用EXEC时，redis会拒绝执行这一事务。
- 调用exec之后的错误
redis则采取了完全不同的策略，即redis不会理睬这些错误，而是继续向下执行事务中的其他命令。这是因为，对于应用层面的错误，并不是redis自身需要考虑和处理的问题，所以一个事务中如果某一条命令执行失败，并不会影响接下来的其他命令的执行。

```watch
127.0.0.1:6379> set age 23
OK
127.0.0.1:6379> watch age //开始监视age
OK
127.0.0.1:6379> set age 24 //在EXEC之前，age的值被修改了
OK
127.0.0.1:6379> multi
OK
127.0.0.1:6379> set age 25
QUEUED
127.0.0.1:6379> get age
QUEUED
127.0.0.1:6379> exec //触发EXEC
(nil) //事务无法被执行
```

## 客户端连接方式

- 本地连接
`redis-cli`

- 远程连接
以下实例演示了如何连接到主机为 127.0.0.1，端口为 6379 ，密码为 mypass 的 redis 服务上。
`redis-cli -h 127.0.0.1 -p 6379 -a "mypass"`

## redis的db的操作

- 清空所有库的所有数据
`$redis->flushall()`

- 清空某个db
清空当前选中库的所有key
```redis
$redis->select(0); // 0-15
$redis->flushdb();
```

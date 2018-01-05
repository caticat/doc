# 安装PHP中的zookeeper扩展

[原文](http://www.huangxiaobai.com/archives/1437)

HP的安装以及配置都非常的简单，可以参考文章：Zookeeper的安装，今儿来看看PHP扩展的安装。
现在官方已经有0.3.2的版本了，查看 https://pecl.php.net/package/zookeeper


安装zookeeper Lib
下载参考：Zookeeper的安装

# tar -xzf zookeeper-3.4.9.tar.gz
# cd zookeeper-3.4.9/src/c
# ./configure –prefix=/usr/local/zookeeper-lib/
# make && make install
下载
官方下载地址：https://pecl.php.net/package/zookeeper
百度网盘下载地址：https://pan.baidu.com/s/1c1M6AI0

# tar xzf zookeeper-0.3.1.tgz
# cd zookeeper-0.3.1
# phpize
# ./configure -with-php-config=/usr/local/php7/bin/php-config 
-with-libzookeeper-dir=/usr/local/zookeeper-lib/
# make 
# make install

在php.ini的末尾增加
extension=zookeeper.so
安装过程中错误
error: zookeeper support requires libzookeeper. Use –with-libzookeeper-dir=<DIR> to specify the prefix where libzookeeper headers and library are located
需要加上-with-libzookeeper-dir的配置
configure: error: Can’t find zookeeper headers under “/usr/local/zookeeper-lib”
缺少zookeeper的lib，本人使用的zookeeper-3.4.9.tar.gz，解压后直接使用的zookeeper，并没有lib。这个时候打开cd ./src/c，执行 ./configure –prefix=/usr/local/zookeeper-lib（生成zookeeper lib）
appending configuration tag “CXX” to libtool
php的扩展版本和zookeeper的版本不兼容，刚开始使用的0.2.3的稳定，zookeeper使用的最新的版本，始终安装不成功，之后下载了最新的0.3.1的扩展版本，才安装成功

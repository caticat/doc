# mountWindows共享目录

## 步骤

1. 计算机(win)
	1. 管理
	2. 本地用户和组
	3. 用户
	4. 创建
2. 控制面板(win)
	1. 用户帐户
	2. 管理用户帐户
	3. 查看域
3. 新建共享目录(win)
	1. 创建目录
	2. 目录属性
	3. 共享按钮
	4. 查找用户
	5. 位置
	6. 选择`2`中查找的域名
	7. 输入对象名称中输入`1`中创建的用户
	8. 确定
	9. 在列表中个更改权限级别为`读取/写入`
	10. 共享
4. 安装共享组件(linux)
	1. `yum install -y cifs-utils`
5. 在linux上挂载目录(linux)
	1. 创建共享目录`makedir`
	2. 挂载共享目录`mount -t cifs -o username='帐号名',password='密码',file_mode=0777,dir_mode=0777,iocharset=utf8,sec=ntlm //ip地址/共享目录名 刚创建的目录的路径`
		1. `-t`代表协议格式cifs(Common Internet File System)
		2. `xxx_mode`代表文件权限
		3. `iocharset`代表通信字符编码格式
		4. `sec`标识密码hash格式,我这边测试使用`ntlm`成功

## 额外命令

- `mount`可以直接查看所有挂载目录
- `umount 目录`可以弹出挂载目录
- `df -h`看挂在目录更清晰

## 临时记录

帐号
sharepanj
zzzz!1234

域
UPC2195

命令
`mount -t cifs -o username='sharepanj',password='zzzz!1234',file_mode=0777,dir_mode=0777,iocharset=utf8,sec=ntlm //192.168.119.185/sharepanj /home/pan/test/sharepanj`

`df -h`

1. 安装ftp和ftp服务	`yum install vsftpd ftp -y`
2. 添加防火墙端口	`firewall-cmd --zone=public --add-port=21/tcp --permanent`
3. 重启防火墙	`systemctl restart firewalld`
4. 修改`/etc/vsftpd/user_list`在最后增加准许使用ftp的用户
5. 修改`/etc/vsftpd/vsftpd.conf`配置为如下内容
	1. 关闭匿名访问功能	`anonymous_enable=NO`
	2. 准许本地用户登录	`local_enable=YES
	3. 只准访问自己的`/home`目录	`chroot_list_enable=YES`
	4. 打开注释	`chroot_list_file=/etc/vsftpd/chroot_list`
	5. 自己创建`chroot_list_file=/etc/vsftpd/chroot_list`文件并将相应用户列入列表
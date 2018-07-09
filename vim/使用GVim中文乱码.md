# 使用GVim中文乱码

## 解决方法

修改`D:\Program Files (x86)\Vim`类似路径下的`_vimrc`文件,追加一下内容即可
第一行:文档编码
第二行:恢复菜单编码
第三行:提示编码(去掉也好用,没注意过效果)

```txt
set encoding=utf-8
source $VIMRUNTIME/delmenu.vim
language messages zh_CN.utf-8
```
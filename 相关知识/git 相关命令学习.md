##  [**git 基本操作中文教程**]( https://backlog.com/git-tutorial/cn/contents/)

## git账号登录（git ssh登录）：

1. 配置账号  
`git config user.email "xx@xx.com" `  
`git config user.name "loveshanshan"`
 >> 如果是全局的话：  
`git config --global user.name  "yourname"`  
`git config --global user.email  "email@email.com "`

2.  生成ssh key  
   >>执行下面的命令，一路默认，会看到生成.ssh的文件夹  
`ssh-keygen -t rsa -C "邮箱"` 

>>把文件中key复制到github的setting中的SSH Key中  
`cat /home/kedeng/.ssh/id_rsa.pub `  

3.  本地添加远程仓库  
`git remote add  origin git@github.com:loveshanshan/MyPython.git`
4. 可正常使用git push / pull / fetch进行操作  


## 常用语句
> 本地删除与远程仓库的连接   
`git remote rm origin`

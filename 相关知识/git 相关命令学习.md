git 基本操作中文教程： https://backlog.com/git-tutorial/cn/contents/
git remote rm origin # 删除远程仓库链接
1, git账号登录：
使用git的ssh登录的话：
如果只是本项目的话
git config user.email "xx@xx.com"   
git config user.name "loveshanshan"
如果是全局的话：
git config --global user.name  "yourname"
git config --global user.email  "email@email.com "

ssh-keygen -t rsa -C "邮箱" 一路默认，可看到有文件生成在./ssh文件中
cat /home/kedeng/.ssh/id_rsa.pub 
把这个文件中的内容复制到 github的setting中的SSH key中

git remote add  origin git@github.com:loveshanshan/MyPython.git



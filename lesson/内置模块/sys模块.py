import sys
# 1， 查看系统是linux, windows, mac[在selenium 时可以自动判断进行使用]
print("1，当前系统是:", sys.platform)  # 分别会是win32,  darwin, linux

# 2， 查看python版本 [可与python版本对比][项目可以要求]
print("当前python版本是:", sys.version.split(" ")[0])
print("当前python版本大于3.6.5: ", sys.version_info > (3, 6, 5))

# 3， 查看当前的python 环境路径
print(sys.path)

# 4， 查看当前内存中的所有模块
print(sys.modules)

# 5，查看python支持递归的个数
print(sys.getrecursionlimit())

# 6，  查看当前有多个少引用(这里有3个调用，最后一个是查询时自己的调用)
a = [1, 2, 3]
b = a
print(sys.getrefcount(a))

# 7， 查看当前默认编码
print(sys.getdefaultencoding())
# 可以引入参数,sys.argv是个list, 第0个是脚本本身[传参时可以使用]
print(sys.argv)

# int , str, bool, list , tuple, dict, set
# 1, int 类型，
a = 5
print(a.bit_length())  # 查看这个int类型的数字占多少bit
# 2, bool 类型
b_a = 0
print(type(b_a))
s_a = str(b_a)  # int 转字符串
i_a = int(s_a)  # str转int
print(bool(b_a))
print(bool(None))
# {}, [], ''  , 0 , None, bool值都是False
# 3, 字符串类型
# 索引和切片
# 切片，只有两个参数时，只能从左往右切
# 如果第三个步长为正时，只能从左往右切
# 如果第三个步长为负时，只能从右往左切
a = "Hello , this is all the world:  abcdefgh \
ijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = a[-1:-10:-3]  # 可以切
y = a[-1:-10:3]  # 不可以切
print(x)
# str常用的方法
print(a.capitalize())  # 首字母变大写
print(a.lower())  # 全转小写  也可以用casefold  与lower的区别，也会识别其它语言（如俄德）
print(a.upper())  # 全转大写
print(a.swapcase())  # 大小写互转
print(a.title())  # 所有单词首字母大写 （以非字母为切分，所有的非字母后面的字母变大写）

aa = "hello , python"
print(aa.center(20))  # 分20个字符，居中
print(aa.center(20, "*"))  # 居中后，其它位置可填充
bb = "hello\tpython"
print(bb)
print(bb.expandtabs(20))  # 更改 \t 的长度，默认是更改为8
cc = " hello,  check it "
print(cc.strip())  # 去掉两边的 空格 /n /t
# 常用的其它方法：
# strip()--->去掉左右两边的空或指定的字符串
# replace('','') 替换时，还可以指定替换的次数
# split（）切割字符串，返回list; 切割的内容不存在时返回原字符串组成的列表
print(cc.split())
# 字符串的格式化（a，占位符；b,  {}）
# 查找类
# startswith() endswith() 返回bool类型

# 下面的三个，可以指定开始位置和结束位置
# find() 返回int; 返回第一次出现的位置，没有则返回-1
# index() 返回int； 返回第一次出现的位置，没有时报错
# count()  返回int ; 返回要字符串的某个字符串的个数

# 判断字符串是一些特性
dd = '119999我99a9999999999999999999999999999999'
print(dd.isdigit())  # 是否数字
print(dd.isalnum())  # 是否数字和字母汉字
print(dd.isascii())
print(dd.isnumeric())  # 能识别  伍五拾十  这样的数字

xx = "abcd"
print(xx[::-1])  # 回文


# 列表  索引 切片
a = []

# 下面方法对原列表操作
# 列表直接添加一个元素--append, 按位置添加 insert, 批量添加extend-->需要传的是一个迭代对象
a.append("hello")  # 添加，在原有的基础上
a.insert(10, "wo")  # 在某个索引位置添加，其它后移，要是超过列表长度，就在最后面追加
a.extend(["hello", "hh"])  # extend进扩展，要扩展的对像必须是可迭代的，然后在原列表后面追加
print(a)

# 列表删除
a.pop()  # 可以填写位置，根据位置删除，返回删除的内容
a.remove('hello')  # 根据元素删除
print(a)
del a[1]  # 按位置删除
del a[1:3:2]  # 切片所包含的元素删除
print(a)
a.clear()  # 清空列表

# 改
a = [1, 2, 3, 4]
a[0] = "swi"  # 按位置替换
a[1:3] = "ai ya"  # 先按位置删除，然后将后面的可迭代对象依次添加到列表中
print(a[1:11:2])
a[1:11:2] = [2, 3, 4]  # 如果添加了步长，上面结果有3个，实际上传了4个
# 需要考虑根据步长所得的元素个数是否与可以迭代对象的个数相等
print(a)


# list的相关操作：
# count(), sort()
a = [1, 2, 3, 9, 8, 7, [3, 2, 1, 7, 8, 9]]
# print(a.sort(reverse=True))   # 降序
a.reverse()  # 反转
# sort 的排序只能针对里面全是数字的或是全是字母的

# 元组： 不能增删改, 但是里面的内容是可变的话，这个可变的内容倒是可以变的
a = (1, 2, ['hello'])
a[2][0] = "wwww"
print(a)


# 针对字符串， join 和 split 是相反的功能；一个是分割字符串为列表，一个是合并列表为字符串
# list  tuple转为拼接的字符串
a = ["hello", "check"]
b = ("hhhh", "hhhh")
print("___".join(a))
print("   ".join(b))

# set集合
# 特点一：元素不重复(所以可以用来去重)
# 特点二：无序(没有索引)
# 特点三：里面的元素可哈希（所以没有索引，没法直接定位元素）
# 可变
st = {"hello", "word"}

# 增加，
# add, 添加一个元素
# update, 迭代更新 ，update 一个可迭代对象

# 删除
# pop 随机删除一个
# remove 删除某一个元素，没有这个元素就会报错
# clear 清空集合

s1 = {2, 3}
s2 = {2, "hello"}
# 两个集合操作
# 交集： &   intersection
# 并集： | union
# 差集：-  differenc 前面有，后面没有的
# 反交集： ^ symmetric_difference, 结果是两个中各自独立的生成一个新的set
# 子集： < issubset
# 超集：> issuperset

# 集合的其它操作,   可以将set变成一个有序的，可hash的
frozenset(s1)

# 列表中的每一个元素可哈希才能进行排序

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


# 字典 key, value;   key 用不可变的数据类型就可以了，像是1, ''hel',  (1,1,2)， True等都可以
# 在python中的字典中作为key来用

dic = {"a": 1, "b": "you see"}
# 增、改
dic['b'] = 2
dic.update({"hello": "world", "aiya": 2})  # 更新或添加多个键值对
dic.setdefault("newKye", "newValue")
dic.setdefault("newKye", "newValue2")
# 第一个元素是key, 第二个元素是value
# 使用setdefault时，如果key 已在字典中，则不会修改字典；像是newValue2的就不会生效
# 如果key不在字典中，刚新增一个键值对
print(dic)
# 删除 pop, del , clear
dic.pop('a')  # 删除一个并返回键对应的值
dic.popitem()  # 默认删除最后一个
del dic['b']  # 删除一个
# dic.clear()  # 清空所有
print(dic)

# 查
print(dic)
# dic['a']  # 没有键的时候查询会报错
print(dic.get('newKye', "没有key，返回我呀"))  # 没有键的时候，会返回None；没有键时还可又返回指定的内容
print(dic.setdefault('newKye'))  # 没有对应的键时,会返回None， 原字典中还会多一个键值对, 有对应的
#  键时会返回对应的值
print(dic)
#  返回所有keys
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.popitem())
print(dic.items())

lia = {"age": 10, "name": "xiaohua", "aihao": "changge"}
# 直接for 循环，默认拿到的是键
for x in lia:
    print(x)
# 直接for 循环，默认拿到的是键
for x in lia.items():
    print(x)

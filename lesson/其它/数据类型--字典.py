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
dic.popitem()  # 随机删除
del dic['b']  # 删除一个  不写key则会删除全部
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
print(dic.keys())  # 返回所有的keys
print(dic.values())  # 返回所有的值
print(dic.items())  # 返回所有的键值对
print(dic.popitem())  # 随机删除


lia = {"age": 10, "name": "xiaohua", "aihao": "changge"}
# 直接for 循环，默认拿到的是键
for x in lia:
    print(x)
# 直接for 循环，默认拿到的是键
for x in lia.items():
    print(x)

xx = {}
xx = xx.fromkeys(("xia", "aa", "asdf"), "x")   # 批量生成一个字典
print(xx)




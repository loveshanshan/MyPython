import copy
# 赋值操作，共用一份数据，改一个，其它列表也会改
list1 = ["hello", "peiqi", "qiaozhi"]   # 这个列表产生了一个内存地址
# list1指向头指针，也就是这个列表的首地址
list2 = list1  # 未产生新的数据，将list1的地址赋值给list2,所以也是列表的首地址-0
list1.append("lai de")
print(list1, id(list1))
print(list2, id(list2))


list1 = ["hello", "peiqi", "qiaozhi"]   # 这个列表产生了一个内存地址
# list1指向头指针，也就是这个列表的首地址
list2 = list1[:]  # 切片会产生新列表  -->这种浅拷贝， 生成的内容各自会改各自的
list2 = list1.copy()  # 跟上面的copy效果一样
print(list1, id(list1))
print(list2, id(list2))

# 拷贝所有内容，可哈希的内容各自是各自的；不可哈希的内容，还是共用一份
list1 = ['peiqi', 'qiaozhi', ['lai de', 'a li']]
list2 = list1.copy()
list2[2][0] = "a zhu"
print(list1, id(list1))
print(list2, id(list2))
print(id(list1[2]),  id(list2[1]))


# 用deepcopy，可哈希的内容各自是各自的；不可哈希的内容，也是各自一份
list1 = ['peiqi', 'qiaozhi', ['lai de', 'a li']]
list2 = copy.deepcopy(list1)
list2[2][0] = "a zhu"
print(list1, id(list1))
print(list2, id(list2))
print(id(list1[2]),  id(list2[1]))

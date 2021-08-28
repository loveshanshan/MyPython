# 1, while / for循环中使用了break时，else语句不会被执行; 否则，当正常
# 循环结束时，会执行else
def test_while():
    n = 10
    i = 0
    while i < n:
        print("i is", i)
        i = i+1
        break
    else:
        print("this is while else")


def test_for():
    for i in range(4):
        print("i is ", i)
        # if i > 2:
        #     break
    else:
        print("for else")


test_for()

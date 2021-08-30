
class A1:
    pass


class A2:
    pass


class A3:
    pass


class B1(A1, A2):
    pass


class B2(A2):
    pass


class B3(A2, A3):
    pass


class C3(B3):
    pass


class C2(B1, B2):
    pass


class C1(B1):
    pass


class D(C1, C2, C3):
    pass


print(*D.__mro__, sep='\n')

r"""
       O
   /    |     \
A1  A2  A3
  |  /  |  \   |
  |/    |    \ |
B1  B2  B3
  |  \  |       |  
  |    \|       |
C1  C2  C3
   \    |    /
        D
"""
# c3 算法，先找第一层父类，左边第一个，对每一个元素都是先深度后广度
#  1，第一步，查看第一层父类C1，C2，C3，先取C1
#  2， 查看C1的父类B1,   B1还有子类C2 , 取C2
#  3,    查看B1， B1无其它子类，取B1
#  4,    查看B1的父类，A1，A1无其它父类，取A1
#  5,    A1 的父类为object, 本例中object 还有其它子类，取底层左则未取完的类B2
#  6， 查看B2父类A2, A2还有其它子类B3，B3最底层C3
#  7,     取C3, 查看C3 父类B3
#  8,     取B3, 查看B3的父类A2
#  9，  取A2， 查看A2的父类为object, object还有其它子类继承A3
#  10,   取A3
#  11,   取object

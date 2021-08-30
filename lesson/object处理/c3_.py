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


class C3(B2, B3):
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
  |  \  |  \   |  
  |    \|    \ |
C1  C2  C3
   \    |    /
        D
"""

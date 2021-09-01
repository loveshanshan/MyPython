# encode , 相对应的二进制编码
# decode, 解码
# 常用的编码, ord是转为ASCII， encode编码：
# ASCII 英文，数字，一部分特殊符号 1 byte ； 一个字节 8bit
# GBK : 每个字符占2个字节，16位， 汉字
# UTF-8：每个字符最少占1个字节，8位（能覆盖所有ASCII表示）；汉字是3个
# UTF-16：每个字符最少占2个字节，16位
# unicode: 万国码，每个字符两个字节，16位
# 每四位可以用一个16进制表示；每三位可以用一个8进制表示
# 1字节  1byte=8bit  1KB=1024byte MB ,GB,TB,PB,EB,ZB,YB,NB


a = "你"
b = "a"
print("GBK    :编码", a.encode("GBK"), ord(a))
print("GBK    :编码", b.encode("GBK"), ord(b))
print("UTF-8  :编码", a.encode("UTF-8"), ord(a))
# UTF-8下
# 英文 8bit ,   1byte
# 欧洲  16bit ,   2 bytes
# 中文  32bit ,   3 bytes
print("UTF-8  :编码", b.encode("UTF-8"), ord(b))
print("UTF-16 :编码", a.encode("UTF-16"), ord(a))
print("UTF-16 :编码", b.encode("UTF-16"), ord(b))

# python2 默认ASCII码
# python3 默认UTF-8
aa = '我r'
print(len(aa), len(aa.encode("utf-8")))
# 结果是2，4

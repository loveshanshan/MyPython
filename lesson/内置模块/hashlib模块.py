import hashlib
my_md5 = hashlib.md5("你好".encode('utf-8'))
my_md5.update("你好".encode('utf-8'))
d = my_md5.hexdigest()
print('md5: ', d, 'md5 长度:', len(d), 'md5 bits:', len(d)*4)
# md5:  54094f7d50d36a81e1e79bb237c46805 md5 长度: 32 md5 bits: 128
# 7eca689f0d3389d9dea66ae112e5cfd7 32个16进制（16位）,  128 bit 来表示；
# 1个16进制是4 bit, 1个字节是两个16进制，是8bit
# 加盐就是在要加密的字符串上再加上其它内容，像是账号+一个固定值等，
my_sha1 = hashlib.sha1("你好".encode('utf-8'))
my_sha1.update("你好".encode('utf-8'))
d = my_sha1.hexdigest()
print('sha1: ', d, 'sha1 长度:', len(d), 'sha1 bits:', len(d)*4)

my_sha224 = hashlib.sha224("你好".encode('utf-8'))
my_sha224.update("你好".encode('utf-8'))
d = my_sha224.hexdigest()
print('sha224: ', d, 'sha224 长度:', len(d), 'sha224 bits:', len(d)*4)

my_sha256 = hashlib.sha256("你好".encode('utf-8'))
my_sha256.update("你好".encode('utf-8'))
d = my_sha256.hexdigest()
print('sha256: ', d, 'sha256 长度:', len(d), 'sha256 bits:', len(d)*4)

my_sha384 = hashlib.sha384("你好".encode('utf-8'))
my_sha384.update("你好".encode('utf-8'))
d = my_sha384.hexdigest()
print('sha384: ', d, 'sha384 长度:', len(d), 'sha384 bits:', len(d)*4)

my_sha3_256 = hashlib.sha3_256("你好".encode('utf-8'))
my_sha3_256.update("你好".encode('utf-8'))
d = my_sha3_256.hexdigest()
print('sha3_256: ', d, 'sha3_256 长度:', len(d), 'sha3_256 bits:', len(d)*4)

my_shake_256 = hashlib.shake_256("你好".encode('utf-8'))
my_shake_256.update("你好".encode('utf-8'))
d = my_shake_256.hexdigest(10)  # 可以指定生成的长度
print('shake_256: ', d, 'shake_256 长度:', len(d), 'shake_256 bits:', len(d)*4)
"""
md5:  54094f7d50d36a81e1e79bb237c46805 md5 长度: 32 md5 bits: 128
sha1:  ac9efadac7a9971fcd242109fc0fbb3555c6a801 sha1 长度: 40 sha1 bits: 160
sha224:  a0d1438b87e31b37a984011c6d70f6c28e42382ae44d011cf4bd46f9 sha224 长度: 56 sha224 bits: 224
sha256:  6bd3255eeefac7a295f7bc81e7b288c36dc479e1a590cce3309104295ec17c33 sha256 长度: 64 sha256 bits: 256
sha384:  c5f60d687261253adbf6538401037ab1b03a254b7d30d40787c1671e2a40b80c2bb749a3b6fe3737e7ca16ad09bf4499 sha384 长度: 96 sha384 bits: 384
sha3_256:  830d44fa365cb4e62559a77b6d53a5135fd2f5ed8add7a20470e780dd3d0e892 sha3_256 长度: 64 sha3_256 bits: 256
shake_256:  99008b67062c148137fa shake_256 长度: 20 shake_256 bits: 80
"""

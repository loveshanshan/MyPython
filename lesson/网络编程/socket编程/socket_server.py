import socket
s_r = socket.socket()
s_r.bind(("127.0.0.1", 8099))
s_r.listen(3)
while True:
    con, c_info = s_r.accept()
    d = con.recv(1024)
    print(c_info)
    print(d, len(d))
    print(d.decode("utf-8"))
    con.send("over".encode("utf-8"))
    con.close()
s_r.close()

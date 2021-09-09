import socket
s_r = socket.socket()
s_r.bind(("127.0.0.1", 8099))
s_r.listen(3)
while True:
    con, c_info = s_r.accept()
    d1 = con.recv(10)
    d2 = con.recv(10) 
    print(d1.decode("utf-8"))
    print(d2.decode("utf-8"))
    con.send("over".encode("utf-8"))
    con.close()
s_r.close()

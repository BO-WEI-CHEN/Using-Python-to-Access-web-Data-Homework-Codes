# -*- coding:utf-8 -*-
# 2017_01_15_Web Browser by using Socket
import socket
homework = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
homework.connect(('data.pr4e.org', 80))  # NOTICE: every url has different writing
homework.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')
while True:
    data = homework.recv(512)
    if len(data) < 1:
        break
    print data
homework.close()
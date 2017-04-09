#!/usr/bine/env python

import pwn
import r2pipe
import json

bin = './crackme0x03'

r = r2pipe.open(bin)
t = pwn.process(bin)

r.cmd('aaa')
token = r.cmd('? ' + '0x52b24') # Discovered with binary ninja at 0x80484f8
print '[+] Using {} as the password'.format(token)

t.readline()
t.sendline(token)
print t.readline()

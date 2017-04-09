#!/usr/bine/env python

import pwn
import r2pipe
import json

bin = './crackme0x05'

r = r2pipe.open(bin)
t = pwn.process(bin)

r.cmd('aaa')
token = str(r.cmd('pd 1 @0x0804851a').split('=')[1])
token = r.cmd('? ' + token)

print '[+] Using {} as the password'.format(token)

t.readline()
t.sendline(token)
print t.readline()

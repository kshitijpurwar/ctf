#!/usr/bine/env python

import pwn
import r2pipe

bin = './crackme0x04'

r = r2pipe.open(bin)
t = pwn.process(bin)

r.cmd('aaa')
token = str(r.cmd('pd 1 @0x080484bb').split('=')[1].split(';')[0])

print '[+] Using {} as the password'.format(token)

t.readline()
t.sendline(token)
print t.readline()

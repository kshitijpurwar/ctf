#!/usr/bine/env python

import pwn
import r2pipe
import json

bin = './crackme0x01'

r = r2pipe.open(bin)
t = pwn.process(bin)

r.cmd('aaa')
token = str(r.cmdj('pdj 1 @0x0804842b')[0]['opcode'].split('=')[2].split()[0])
token = r.cmd('? ' + token)

print '[+] Using {} as the password'.format(token)

t.readline()
t.sendline(token)
print t.readline()

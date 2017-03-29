#!/usr/bine/env python

import pwn
import r2pipe
import json

bin = './crackme0x00'

r = r2pipe.open(bin)
t = pwn.process(bin)

token = r.cmdj('izj')[2]['string'].decode('base64')

print '[+] Using {} as the password'.format(token)

t.readline()
t.sendline(token)
print t.readline()

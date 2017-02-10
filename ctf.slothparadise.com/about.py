#!/usr/bin/env python

import requests
import sys

while True:
    r = requests.get('http://ctf.slothparadise.com/about.php')
    if 'KEY' in r.text:
        print r.text
        sys.exit()

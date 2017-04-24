#!/usr/bin/env python3

import linecache as ln
from random import uniform

pw = ''

for i in range(5):
	pw += ln.getline('words.txt', int(uniform(0, 354985)))[:-1] + ' '

print(pw)

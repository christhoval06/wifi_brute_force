#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open("passwords.txt", "w")

template = 'WiFi-{}\n'
length = 8


for number in range(int('1{}'.format('0' * (length - 1))) - 1, int('9' * length) + 1):
    number = str(number).rjust(length, '0')
    f.write(template.format(number))

f.close()

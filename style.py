#!/usr/bin/env python3
import os
import sys

def enable_style(style):
 os.system('i3-style %s -o ~/.i3/config '%style)
 os.system('i3-msg restart')

styles = ['archlinux', 'base16-tomorrow', 'debian', 'deep-purple', 'default', 'flat-gray', 'gruvbox', 'icelines', 'lime', 'okraits', 'purple', 'seti', 'slate', 'solarized', 'tomorrow-night-80s', 'ubuntu']

def gen_char(c, x):
 o = list()
 for y in range(x):
  o.append(c)
 return "".join(o)

while True:
  for k in styles:
   print(str(styles.index(k)) + ": " + str(gen_char(" ", (3-len(str(styles.index(k)))) )) + k)
  enable_style(styles[int(input("\nChoice?\n>"))])


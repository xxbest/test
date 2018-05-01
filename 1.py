#!/usr/bin/python3
 
for x in range(1, 11):
  print(repr(x).rjust(2), repr(x*x).rjust(5),repr(x*x*x).rjust(3))
 # 注意前一行 'end' 的使用


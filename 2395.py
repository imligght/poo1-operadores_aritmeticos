# -*- coding: utf-8 -*-

a, b, c = input().split()
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
a = int(a)
b = int(b)
c = int(c)

ax = x//a
by = y//b
cz = z//c

print(f"{ax * by * cz}")
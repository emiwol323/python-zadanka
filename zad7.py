#!/usr/bin/python
import math

a=int(input("Podaj pierwszą liczbę: "))

b=int(input("Podaj drugą liczbę: "))


print(a+b)
print(a-b)
print(b-a)
print(a*b)

if b==0 or a==0:
    print("Nie dziel przez zero!!!")
else:
    print(a/b)
    print(b/a)

print(a^b)
print(b^a)

print ("hypot: ",  math.hypot(3, 2))
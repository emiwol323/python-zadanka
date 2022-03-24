#!/usr/bin/python
import random

liczba = random.randint(1,20)
próby = []

a=int(input("Jaka liczba została wylosowana? "))
próby.append(a)

if a==liczba:
    print("Brawo! Zgadłeś wylosowaną liczbę po 1 próbie!")
else:
    while a!=liczba:
        próby.append(a)
        a=int(input("Próbuj kolejny raz "))

print(f"Trafiłeś za {len(próby)} razem")

    


    




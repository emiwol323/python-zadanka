#!/usr/bin/python
import random
liczbyK = []
liczbyU = []

for i in range(6):
    liczba = random.randint(1,50)
    liczbyK.append(liczba)

for i in range(6):
     liczba = int(input("Podaj liczbę od 1 do 50 "))
     while liczba>50 or liczba<1:
          print("Podałeś złą liczbę. ")
          liczba = int(input("Wprowadź jeszcze raz"))

     liczbyU.append(liczba)
    

print("Wylosowane liczby: ")
print(*liczbyK, sep=', ')
print("Twoje liczby: " )
print(*liczbyU, sep=', ' )

trafione=set(liczbyK)&set(liczbyU)

if len(trafione)>0:
     print(f"Twoje liczby zgadzają się z {len(trafione)} liczbami wylosowanymi")
else:
     print("Nie trafiłeś adnej z liczb")
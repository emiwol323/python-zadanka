#!/usr/bin/python
import random
from re import L

wybor=["kamień", "papier", "nozyce"]

k=0
u=0

while k<3 and u<3:
    losK= random.choice(wybor)
    losU=input("kamień, papier, nozyce?")
    if losK==losU:
        print("Remis! Podaj jeszcze raz!")
    elif losK=="kamień" and losU=="papier":
        print("Przegrałeś tą rundę! Podaj jeszcze raz")
        k=k+1
    elif losK=="kamień" and losU=="nozyce":
        print("Wygrałeś tą rundę! Podaj jeszcze raz")
        u=u+1
    elif losK=="papier" and losU=="kamień":
        print("Wygrałeś tą rundę! Podaj jeszcze raz")
        u=u+1
    elif losK=="papier" and losU=="nozyce":
        print("Przegrałeś tą rundę! Podaj jeszcze raz")
        k=k+1
    elif losK=="nozyce" and losU=="kamień":
        print("Wygrałeś tą rundę! Podaj jeszcze raz")
        u=u+1
    elif losK=="nozyce" and losU=="papier":
        print("Przegrałeś tą rundę! Podaj jeszcze raz")
        k=k+1
    else:
        print("Nie podałeś nic z (kamień, papier, nozyce)")
    if k==3 or u==3:
        if(k>u):
            print("Niestety przegrałeś!")
        else:
            print("Brawo! Wygrałeś!")






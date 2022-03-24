# 2, 2 - I
# -2, 2 - II
# -2, -2 - III
# 2, -2 - IV

a=int(input("Podaj współrzędną x punktu: "))
b=int(input("Podaj współrzędną y punktu: "))

if a>0 and b>0:
    print(f"Twój punkt {a}, {b} lezy w I ćwiartce układu współrzędnych ")
elif a<0 and b>0:
    print(f"Twój punkt {a}, {b} lezy w II ćwiartce układu współrzędnych ")
elif a<0 and b<0:
        print(f"Twój punkt {a}, {b} lezy w III ćwiartce układu współrzędnych ")
elif a>0 and b<0:
        print(f"Twój punkt {a}, {b} lezy w IV ćwiartce układu współrzędnych ")
else:
        print(f"Twój punkt {a}, {b} lezy na osi ")

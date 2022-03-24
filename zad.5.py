a=int(input("Podaj długość pierwszego boku: "))

b=int(input("Podaj długość drugiego boku: "))

c=int(input("Podaj długość trzeciego boku: "))

if a+b>c and b+c>a and a+c>b and a>0 and b>0 and c>0:  
    print("Taki trójkąt mozna zbudować")
else:
    print("Taki trójkąt nie mozna zbudować")



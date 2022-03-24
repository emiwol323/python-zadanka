

waga=float(input("Podaj swoją wagę (w kilogramach): "))
wzrost=float(input("Podaj swój wzrost (w metrach): "))

BMI=waga/(wzrost)** 2

if BMI<20:
    print("Niedowaga")
elif 20<BMI<25:
    print("Prawidłowa waga ")
elif 25<BMI<30:
    print("Nadwaga ")
else:
    print("Otyłość ")

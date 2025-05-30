#1 ZADATAK
#Očekujem da rezultat bude: 5.0 - 4.935 = 0.065
#a)

rezultat = 5.0 - 4.935
print(rezultat)

#Dobila sam 0.06500000000000039 jer decimalni brojevi u binarnom sustavu ne mogu uvijek biti točno predstavljeni; python koristi floating-point aritmetiku koja može dovesti do malih grešaka u preciznosti.
#b)

suma = 0.1 + 0.2 + 0.3
print(suma == 0.6)  # False ili True?
print(suma)         

#Dobila sam False jer 0.1 + 0.2 + 0.3 u binarnom sustavu ne daje točno 0.6, već nešto poput 0.6000000000000001 zbog istog razloga kao i prethodno.

#2 ZADATAK

def zbroji_i_oduzmi(N):
    broj = 5.0
    for _ in range(N):
        broj += 1/3
    for _ in range(N):
        broj -= 1/3
    print(f"N = {N}, rezultat = {broj}")

zbroji_i_oduzmi(200)
zbroji_i_oduzmi(2000)
zbroji_i_oduzmi(20000)

#rezultat će biti različit za različite vrijednosti N zbog greške u floating-point aritmetici. Kako N raste, greška se može povećati zbog načina na koji se decimalni brojevi predstavljaju u binarnom sustavu.

#3 ZADATAK

#a)

brojevi = []
print("Unesi 10 brojeva:")

for i in range(10):
    broj = float(input(f"Broj {i + 1}: "))
    brojevi.append(broj)

zbroj = 0
for x in brojevi:
    zbroj += x
sredina = zbroj / 10

suma_razlika_kvadrat = 0
for x in brojevi:
    suma_razlika_kvadrat += (x - sredina) ** 2

standardna_devijacija = (suma_razlika_kvadrat / (10 * (10 - 1))) ** 0.5

print("Aritmetička sredina:", sredina)
print("Standardna devijacija:", standardna_devijacija)

#b)

import statistics

brojevi = []
print("Unesi 10 brojeva:")

for i in range(10):
    broj = float(input(f"Broj {i + 1}: "))
    brojevi.append(broj)

# Računanje pomoću modula
sredina = statistics.mean(brojevi)
standardna_devijacija = statistics.stdev(brojevi)

print("Aritmetička sredina:", sredina)
print("Standardna devijacija:", standardna_devijacija)


#4 ZADATAK

# linregress.py





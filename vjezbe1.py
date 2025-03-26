#1. ZADATAK

msg = "Hello world!"
print(msg)

#3. ZADATAK

while True:
    try:
        x1 = float(input("Unesite x koordinatu prve točke: "))
        y1 = float(input("Unesite y koordinatu prve točke: "))
        break 
    except:
        print("Pogrešan unos! Molimo unesite brojeve.")

while True:
    try:
        x2 = float(input("Unesite x koordinatu druge točke: "))
        y2 = float(input("Unesite y koordinatu druge točke: "))
        break  
    except:
        print("Pogrešan unos! Molimo unesite brojeve.")

if x1 == x2:  
    print(f"Jednadžba pravca: x = {x1}")
else:
    m = (y2 - y1) / (x2 - x1)  
    b = y1 - m * x1  
    print(f"Jednadžba pravca je: y = {m}x + {b}")

#4. ZADATAK 

def izracunaj_jednadzbu_pravca(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1

    print(f"Jednadzba pravca je: y = {m}x + {b}")

x1 = float(input("Unesite x1: "))
y1 = float(input("Unesite y1: "))
x2 = float(input("Unesite x2: "))
y2 = float(input("Unesite y2: "))

izracunaj_jednadzbu_pravca(x1, y1, x2, y2)

#5. ZADATAK

import matplotlib.pyplot as plt
def plot_coordinates():
    xlabel = list(map(float, input("Unesite x koordinate (razmak): ").split()))
    ylabel = list(map(float, input("Unesite y koordinate (razmak): ").split()))

    if len(xlabel) != len(ylabel):
       print("Koordinate moraju imati istu duljinu!")
    return xlabel, ylabel

xlabel, ylabel = plot_coordinates()

plt.scatter(xlabel, ylabel, color='blue', label='Točke')

if len(xlabel) > 1:

    plt.plot(xlabel, ylabel, color='pink', label='Pravac kroz točke')


plt.title("Graf koordinata i pravca")

plt.xlabel("X os")

plt.ylabel("Y os")

plt.legend()

save_as_pdf = input("Želite li spremiti graf kao PDF? (da/ne): ").lower()

if save_as_pdf == "da":

    filename = input("Unesite ime za PDF datoteku (npr. 'graf.pdf'): ")
    plt.savefig(filename, format='pdf')
    print(f"Graf je spremljen kao {filename}")

else:
    plt.show()



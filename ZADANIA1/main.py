#zadanie1
x='A'
y='Lazoryszyn'

def dane(dan1,dan2):
    return dan1 +'.'+ dan2
print (dane(x,y))
print (dane('A','Lazoryszyn'))


#zadanie2
def dane(dan1, dan2):
    return dan1.capitalize()+'.'+dan2.capitalize()
print(dane("A", "Lazoryszyny"))

#zadanie3
def dane(rok1, rok2, wiek):
    return int(rok1 + rok2) - wiek
print(dane("20", "21", 23))

#zadanie4
def dane1(dan1,dan2):
    return dan1.capitalize() + '.' + dan2.capitalize()
def dane2(imie, nazwisko, funkcja):
    return funkcja(imie, nazwisko) + " funkcja_z_zadania_2"
print(dane2("A", "Lazoryszyn",dane1))

#zadanie5
def dane(dziel1, dziel2):
    if dziel1 >=0 and dziel2 > 0 : return dziel1 / dziel2
print(dane(6, 3))
print(dane(15,0))

#zadanie6

suma = 0
while(suma<100):
    suma = suma + int(input())

#zadanie7
danex = [1,2,3]
daney= ['Ang','La','zor']
def daned(xxx):
    return tuple(xxx)
print(daned(danex))
print(daned(daney))
#zadanie8_faster
def dane():
    dan = []
    for i in range(5):
        dan.append(int(input()))
    return tuple(dan)
print(dane())
#zadanie9
def dane(dan):
    tyg = {1: "poniediałek",2:"wtorek",3:"środa",4:"czwartek",5:"piątek",6:"sobota",7:"niedziela"}
    return tyg[dan]
print(dane(7))
#zadanie10
def dane10(slowa):
    return slowa[::-1]==slowa
print(dane10(str(input())))



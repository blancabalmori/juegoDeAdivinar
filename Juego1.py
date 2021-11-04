import random
numero = random.randint (0, 99)
print (numero)
intento = int(input("Intente adivinar el número del 0 al 99: "))
numero_de_intentos = 1

if intento < numero :
    print ("Demasiado pequeño")
elif intento > numero :
    print ("Demasiado grande")

if intento == numero : 
    print ("¡Has ganado!")

while intento != numero :
    numero_de_intentos += 1
    intento = int(input("Intente adivinar el número: "))
    if intento < numero :
        print ("Demasiado pequeño")
    elif numero > numero : 
        print ("Demasiado pequeño")
    elif intento == numero : 
        print ("¡Has ganado!")

print ("Número de intentos: " + str (numero_de_intentos))
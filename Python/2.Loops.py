print ( "Estructura Repetitivas")
#For
for i in range ( 1,11):
    print (f'Numero{i}')
for letra in ("Hola mundo"):
    print(letra)  
#While
contador = 1
while contador <=3:
    print(f'Intento {contador}')
    contador +=1
#Do While

while True :
    numero = int (input ("Ingrese numero >0: "))
    if numero>0:
        break
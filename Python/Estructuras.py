print ("Estructuras Condicionales ")
#Condicional Simple
nota_TBI = 17
if nota_TBI>= 10.51:
    print("Aprobaste")
# Condicional Doble
edad= 17
if edad >= 18:
    print ("Tomar bebidas en exceso no es bueno")
else:
    print ("No apto para menores")
    # Condicional anidado
    nota =20 
    if nota>17 & nota <=20:
        print ("Alumno Brillante")
    elif nota>=14 & nota<17:
        print ("Alumno Excelente")

#condiciona multiple 
## se trabaja con match
num =4 
match num: 
    case 1 : print("Volcal A")
    case 2 : print("Volcal A")
    case 3 : print("Volcal A")
    case 4 : print("Volcal A")
    case 5 : print("Volcal A")
    case _ : print("Numero no corresponde a vocal")

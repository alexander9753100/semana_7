cara = 'Realizar una multiplicación con 3 y una división entera con 2 variables distintas.Luego sumarlos en una variable de resultados'
print(cara)
print("")
p1 = ("Realizar una multiplicación con numeros enteros con 3 variables distintas " )
print(p1)
print("")
ini = "introduce tres numeros enteros"
print(ini)

mul1 = int(input("introduce el primer numero: "))
mul2 = int(input("introduce el segundo numero: "))
mul3 = int(input("introduce el tercer numero: "))
print(" el resultado de la multiplicasion de esos tres numeros enteros es:",mul1 * mul2 * mul3)
print("")
p2 = "realisar una división con numeros enteros con 2 variables distintas"

ini_ = "introduce dos numeros enteros"
print(ini_)

di1 = int(input("introduce el primer numero: "))
di2 = int(input("introduce el segundo numero: "))
print("el resultado de la divicion de esos dos numeros enteros es:",di1 / di2)
print("")
resultado = di1 / di2 + mul1 * mul2 * mul3
print("la suma de la respuesta de la multiplicacion de los tres numeros enteros mas la respuesta dela division es:",resultado)
print("")

cara2 = "Realizar el exponencial con 2 y el modulo con 2 Luego restarlos en una variable de resultadosY realizar la división entre el resultado de la suma"
print(cara2)
print("")
print("numeros exponenciales")

ex1 = float(input("primer numero exponencial: "))
ex2 = float(input("ingresa el numero del exponente: "))
print("")
print("modulos")
mo1 = float(input("primer modulo: "))
mo2 =float(input("segundo modulo: "))
ex5 = ex1 ** ex2
mo3 = mo1 % mo2 
mo4 = ex5 - mo3 
print("resultado de la resta del numero exponencial con el modulo: ",mo4)
print("")
de = "aqui se ara la divicion entre el sesultado dela suma por el resultado de resta del modulo y exponencial"
print(de)
resultado2 = mo4 / resultado
print("esta esla respuesta dela division entre el resultado dela suma por el resultado de resta del modulo y exponencial:",resultado2)
print("")
p3 = "Complejo (Complex) Definir 4 variables complejos distintas"
print(p3)
print("")
ca = "acontinuacin introduce tres numeros complejos por ejemplo 7j"
print(ca)
con1 = complex(input("introduce el primer numero complejo: "))
con2 = complex(input("introduce el segundo numero complejo: "))
con3 = complex(input("introduce el tercer numero complejo: "))
con4 = complex(input("introduce el cuarto numero complejo: "))
print("estos son los numero complejos5: ",con1,con2,con3,con4)
print("")
fruta1 = "banana"
fruta2 = "mandarina"
fruta3 = "Uva"
fruta4 = "Fresa"
fruta5 = "Naranja"
fruta6 = "kiwi"
print("nombres de las frutas")
print("1-banana")
print("2-mandarina")
print("3-Uva")
print("4-Fresa")
print("5-Naranja")
print("6-kiwi")
nombre_fruta  =  input ( "Ingrese el nombre de una fruta: " )
if  nombre_fruta  ==  fruta1 :
    print ( fruta1  +  " es la fruta favorita de Abigail." )
elif  nombre_fruta  ==  fruta2 :
    print ( fruta2  +  "es la fruta favorita de Luis." )
elif  nombre_fruta  ==  fruta3 :
    print ( fruta3  +  " es la fruta favorita de Wendy." )
elif  nombre_fruta  ==  fruta4 :
    print ( fruta4  +  "es la fruta favorita de Alexander." )
elif  nombre_fruta  ==  fruta5 :
    print ( fruta5  +  " es la fruta favorita de Eduardo." )
elif  nombre_fruta  ==  fruta6 :
    print ( fruta6  +  " es la fruta favorita de Rodrigo." )

print("fin")
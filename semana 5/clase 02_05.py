"""enero = float(input())
febrero = float(input())
marzo = float(input())
CT = (enero*1.25)+(febrero*1.38)+(marzo*1.14)
print(CT)

dias=["lunes", "martes", "miercoles", "jueves", "viernes"]
lunes = int(input())
dias[0]=lunes
print(dias)
martes = int(input())
dias[1]=martes
print(dias)
miercoles = int(input())
dias[2]=miercoles
print(dias)
jueves = int(input())
dias[3]=jueves
print(dias)
viernes = int(input())
dias[4]=viernes
print(dias)

frutas = ["uno", "dos", "tres"]
ninio = int(input()) #numero de niño
fruta = input() #fruta fav

frutas [ninio] = fruta
print(frutas)

ninio = int(input()) #numero de niño
fruta = input() #fruta fav

frutas [ninio] = fruta
print(frutas)

ninio = int(input()) #numero de niño
fruta = input() #fruta fav

frutas [ninio] = fruta
print(frutas)

alumnos = ["Juan", "Pedro", "Carlos"]
orden = int(input("Orden en el que entraste (1-3): "))
print(f"El niño que entro en orden {orden} se llama {alumnos[orden-1]}")

n = input("ingrese su nombre: ")
a = input("ingrese su apellido: ")
print(f"{n.lower()}.{a.lower()}@ISND.com")
print(f"{n.lower()[0]}.{a.lower()}@ISND.com")"""

salario = input("ingrese su salario: ")
print(salario[0]=="$")
print(salario.count("$")==1)
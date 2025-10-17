A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())
F = float(input())
Z = A+B+C+D+E+F
lista = [A,B,C,D,E,F]
print(f"Maximo: {max(lista):.2f}")
print(f"Minimo: {min(lista):.2f}")
print(f"Diferencia: {max(lista)-min(lista):.2f}")
print(f"Suma: {Z:.2f}")
print(f"Promedio: {Z/6:.2f}")

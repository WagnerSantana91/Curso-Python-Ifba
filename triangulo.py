"""escreva um programa em python
que receba 3 numeros
que corresponde a 3 angulos do trinagulo
e imprima se é um trinagulo ou não
caso seja um trinagulo diga se ele é equilateros isosceles e escaleno"""

lado1=0
lado2=0
lado3 = 0;

lado1 = int(input("Infome o primeiro lado: "))
lado2 = int(input("Infome o segundo lado: "))
lado3 = int(input("Infome o terceiro lado: "))

soma = lado1 + lado2 + lado3;

if soma == 180:
    print("É um triangulo")
    if (lado1 == lado2 and lado2 == lado3):
        print("Triangulo Equilatero")
    elif(lado1 != lado2 or lado2 != lado3):
        print("Triangulo Escaleno")
    else:
        print("Trinagulo Isosceles")
else:
    print("Não é um triangulo")
#Curso basico de Python
#Nome do desenvolvedor: Guilherme Xavier Dos Santos
#versão 1.0
#Exercicio de logica de programação
#Exercicio de calculo da area do hexagono

import math

print("Calcule a area do  hexagono\n")

lado = float(input("Digite o valor do lado do hexagono: "))
area = (3*math.sqrt(3)*lado**2)/2

print('A area do hexagono é: ', area)

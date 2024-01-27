"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa"""

from math import hypot
catOposto = float(input("Digite o valor do cateto oposto: "));
catAdjacente= float(input("Digite o valor do cateto adjacente: "));

print('A hipotenusa vai medir {:.2f}'.format(hypot(catOposto, catAdjacente)))

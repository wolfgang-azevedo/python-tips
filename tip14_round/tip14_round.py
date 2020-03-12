#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Round Built-in Function
# 2020-03-12
#
########################################
#
#

num_1 = input("Digite um número tipo float: ") # ex.: 1.13
num_2 = input("Digite segundo número tipo float: ") #ex.: 2.15

soma = float(num_1) + float(num_2)

print(f'\nsem arredondar o valor: {soma}')

# Built-in round function, rounds numbers
# Função embarcada Round, faz o arredondamento de números

print(f'valor arredondado: {round(soma)}\n')
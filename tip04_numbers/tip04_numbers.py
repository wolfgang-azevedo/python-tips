#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Numbers
# 2020-03-02
#
########################################
#
#
# Numbers in Python not have any quotes |
# Numeros em Python não possuem aspas

# Integer variable | 
# Variaveis do tipo inteiro não utilizando aspas
inteiro = 10 
print(f'Dado da variavel inteiro do tipo: {type(inteiro)}')

# Float Point variables have a . (point) to be indentified | 
# Variaveis do tipo ponto flutuante possuem um . (ponto) como identificação
float_point = 10.5
print(f'Dado da variavel float_point do tipo: {type(float_point)}')

# Use + operator to sum number | 
# Utilize o operador + para efetuar soma
soma = 6 + 4

# Use - operator to subtraction number | 
# Utilize o operador - para efetuar subtração
subtracao = 10 - 5

# Use / operator to divide number | 
# Utilize o operador / para efetuar divisão
divisao = 10 / 2

# Use ** operator to power number | 
# Utilize o operador ** para calcular a potencia
potencia = 2 ** 3

# Use ** operator to get the rest | 
# Utilize o operador % para obter o resto
resto = 100 % 3

print(f'\n Inteiro: {inteiro}\n\n Float: {float_point}\n\n Soma: {soma}\n\n Subtracao: {subtracao}\n\n Divisao: {divisao}\n\n \
Potencia: {potencia}\n\n Resto: {resto}\n')

#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Range method
# 2020-03-10
#
########################################
#
#
# The built-in module range you can generate integer number with a stop integer
# O módulo interno range você pode gerar números inteiros definindo um número inteiro como limite/stop
#
for i in range(10):
    print(f'Número: {i}')

# Or you can define a "Range" by designating the start and stop integers
# Ou você pode definir um "Range" designando um número inteiro como start e outro como stop
for i in range(1, 6):
    print(f'Número limitado: {i}')

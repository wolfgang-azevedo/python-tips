#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# IF Condition
# 2020-03-09
#
########################################
#
#
import time
from datetime import datetime


num = input("Digite um número: ")

# If the test returns TRUE, execute the block of code
# Se o teste retornar, execute o bloco de código
if int(num) == 10:
    print(f'O número {num}, é igual a 10')

# Else-If (multiples true) the test returns TRUE, execute the block of code
# E-Se o teste retornar verdadeiro (multiplos verdadeiros), execute o bloco de código
elif int(num) <9:
    print(f'O número {num}, é menor que 10')

# Else the value returns FALSE, execute the block of code
# Se o valor for falso, execute o bloco de código
else:
    print(f'O número {num}, é maior que 10')


#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Loop While
# 2020-03-08
#
########################################
#
#
import time
from datetime import datetime


num = input("Digite um número: ") 

try:

    # While the value returns true, execute the loop
    # Enquanto o valor for verdadeiro, execute o loop
    while True:

        # If the conditional is true, loop will continue
        # Se a condicional retornar verdade, o loop continuará
        if num == '1':
            print(f'Hoje {datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")} vamos aprender Python!!!')
            time.sleep(1)

        # If the conditional is false, stop the loop
        # Se a condicional retornar falso, paramos o loop
        else:
            print("Numero inválido!!!!")
            break

# Throw and exception when keyboard CTRl+C is pressed
# Lança uma execeção quando interrompido pela combinação CTRL+C
except KeyboardInterrupt as e: 
    print("Fim, loop interrompido pelo usuario")
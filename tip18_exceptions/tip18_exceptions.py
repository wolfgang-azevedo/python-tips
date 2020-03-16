#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Exceptions
# 2020-03-16
#
########################################
#
#
import os

# With Dir built-in function you can list all availble arguments for an object
# Com a função interna Dir, você lista todos os argumentos disponíveis de um objeto

try:
    processe = os.getenv()

    print(processe)

except TypeError as e:
    print(f'Aconteceu um erro -> : {e}')
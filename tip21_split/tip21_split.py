#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Built-in method Split
# 2020-03-20
#
########################################
#
#

string_comma = '1,2,3'
string_space = '1 2 3'

### Built-in method split, without arguments will consider a space between the values and will create a list as a return
### O método embarcado Split, sem argumentos considera o espaço entre os valores e irá criar uma lista como retorno
lista = string_space.split()
print(string_space.split())
print(type(lista))

### You can set a separator as an argument
### Você pode definir um separador como argumento
print(string_comma.split(','))

### You can also set a limit for the split method
### Você também pode definir um limite para método split
print(string_comma.split(',', maxsplit=1))


#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Strings
# 2020-03-01
#
########################################
#
#

# Could be enclosed in single (' ') quotes | Pode ser encapsulada utilizando aspas simples
string01_var = 'Wolfgang'

# Could be enclosed in double (" ") quotes | Pode ser encapsulada utilizando aspas duplas
string02_var = ' Azevedo'

# You can use the built-inf function type() to check the type of data | 
# Você pode utilizar a função interna type() para checar o tipo do dado
print(type(string01_var), type(string02_var)) 

# You can use the + sign as one of various methods to concatenate two strings |
# Você pode utilizar o sinal + como um dos varios métodos para concatenação
print(string01_var + string02_var)

# The built-in len() will return the length of a string, you can know the index of each characters | 
# A função interna len() vai retornar o tamanho da string, você poderá indentificar o indice de cada caracter
print(len(string01_var))

# Will return the first 3 characters of the string
# Vai retornar os 3 primeiros caracteres da string
print(string01_var[0:3])
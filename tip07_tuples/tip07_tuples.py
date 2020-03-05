#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Tuples
# 2020-03-05
#
########################################
#
#

# Tuples are declared using parentheses
# Tuplas são declaradas utilizando parenteses
tupla = ("Wolfgang", "V. Gogh", "Chaplin")

# You can use the built-in function type() to check the type of data, in this case will show <class 'tuple'>
# Você pode utilizar a função interna type() para verificar o tipo de dado, neste caso de uma tupla, retornará <class 'tuple'>
print(type(tupla))

# To print the element on the first position (starts with 0)
# Para exibir o elemento da primeira posição (começando com 0)
print(tupla[0])

# Tuples are immutables, in the following example you can see an error message if you try to append a value to the tuple
# Tuplas são imutáveis, no exemplo abaixo você pode ver a mensagem de error ao tentar adicionar um valor a uma tupla
try:

   add_name = tupla.append("Beethoven")
   
except Exception as e:
    print(e)
    pass
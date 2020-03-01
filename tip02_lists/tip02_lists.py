#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Lists
# 2020-02-29
#
########################################
#
#
list_02 = ['Charlie Chaplin', 'Vincent van Gogh', 'Wolfgang A. Mozart', 'Ludwig van Beethoven']

print(len(list_02)) # To know the length of the list / Para saber o tamanho da lista

print(list_02[0]) # To print the element on the first position (starts with 0) / Para exibir o elemento na primeira posição (começa com 0)

for i in list_02: # To iterate over a list and print all items / Para exibir todos os itens de uma lista
    print(i)

for index, names in enumerate(list_02): # To index a list and iterate over all items / Para indexar uma lista e exibir todos os itens
    print(index, names)

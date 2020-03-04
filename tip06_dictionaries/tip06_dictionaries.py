#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Dictionaries
# 2020-03-04
#
########################################
#
#

# Dictionaries are declared using a pair of braces in a key-pair value schema
# Dicionarios são declarados utilizando um par de chaves em um  esquema de chave/valor
e_mails = {'Charlie Chaplin': 'c_chaplin@heaven.sky', 'Vincent van Gogh': 'v_gogh@heaven.sky', 
          'Ludwig van Beethoven': 'l_beethoven@heaven.sky'} 

# The built-in function list(), lists all key values
# A função interna list(), lista todas as chaves do dicionario
print(list(e_mails))

# You can access the value just calling the var and puting the key inside a pair of brackets
# Você pode acessar o valor chamando a variavel e colocando o valor dentro de um par de colchetes
print(e_mails['Charlie Chaplin'])

# Or You can use the .get method to the key
# Ou você pode utilizar o métod interno .get
print(e_mails.get('Vincent van Gogh')) 

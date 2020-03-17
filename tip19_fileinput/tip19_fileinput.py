#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Fileinput module
# 2020-03-17
#
########################################
#
#
import fileinput

# With fileinput module you can iterates over lines from multiples files/streams
# Com o módulo fileinput você pode nas iterar sobre as linhas de varios arquivos

try:
    with fileinput.input(files=('test_file01.txt', 'test_file02')) as f:
        for line in f:
            print(line)

except FileNotFoundError as e:
    print(f'Arquivo não encontrado, verifique o path! -> : {e}')
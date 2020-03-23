#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Built-in method Open
# 2020-03-22
#
########################################
#
#

### Built-in method Open, you can open a file for reading, writing an append output
### O método embarcado Open, você pode abrir um arquivo para leitura, escrita ou acrescentar

with open('arquivo.txt', 'w') as file:
    file.write("Um belo dia para ficar em casa\n")
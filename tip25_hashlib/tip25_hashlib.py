#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Module Hashlib
# 2020-03-25
#
########################################
#
#
import hashlib

### With hashlib Module you can generates secure hashes
### Com o módulo hashlib você pode gerar hashes de segurança 

value_to_hash = 'tobehashed'

# You can select the algorithm (this example uses MD5), you have to encode unicode (utf-8) and generates the digest... 
# ...in this case we are using a hexdigest method.
# Você pode selecionar o algoritmo (no exemplo estamos usando MD5), você deve codificar caracteres unicode e gerar um digest...
# ...neste caso estamos usando o método hexdigest
md5_hash = hashlib.md5(value_to_hash.encode("utf-8")).hexdigest()

print(md5_hash)
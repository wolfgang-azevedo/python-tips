#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Module Requests
# 2020-03-27
#
########################################
#
#
import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'


response = requests.get(url)

print(response.text)
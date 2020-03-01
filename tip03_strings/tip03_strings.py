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
string01_var = 'Wolfgang' # Could be enclosed in single (' ') quotes
string02_var = ' Azevedo' # Could be enclosed in double (" ") quotes

print(type(string01_var), type(string02_var)) # You can use the built-inf function type() to check the type of data

print(string01_var + string02_var) # You can use the + sign as one of various methods to concatenate two strings

print(len(string01_var)) # The built-in len() will return the length of a string, you can know the index of each characters

print(string01_var[0:3]) # Will return the first 3 characters of the string
#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Input
# 2020-03-06
#
########################################
#
#
import random

nome = input("Digite seu Nome: ")
sobrenome = input("Digite seu Sobrenome: ")
telefone = input("Digite seu Telefone: ")

idx = random.randrange(10)

print(f'Olá, {nome} {sobrenome}! O seu telefone {telefone} foi cadastrado com sucesso. Sua senha é {idx}')


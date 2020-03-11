#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Random Module
# 2020-03-11
#
########################################
#
#
import random


def main():

    numero = input("Digite um número de 0 a 2: ")
    
    # With Random module you can generate numbers randomicaly
    # Com o módulo Random, você pode gerar números randomicamente
    numero_sorte = random.randrange(3)
    
    if numero == str(numero_sorte):
        print("Parabéns você Ganhou!")

    else:
        print(f'Tente novamente...., o número da sorte foi: {numero_sorte}')


def try_again():
    return input("Tentar Novamente? ").lower() == "y"


if __name__ == "__main__":

    while True:
        main()

        if not try_again(): 
            break

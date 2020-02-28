#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Function / Methods and Class
#
########################################
#


class ShowDisclaimer:


    def __init__(self, message): #### Método construtor
        self.message = message


    def disclaimer(self): #### Método onde realizará uma ação, neste caso ele vai dar o print da msg....
        print(f'\nVocê Digitou esta mensagem: {self.message}') 


type_msg = input("\nDigite a Msg: ") #### Definimos uma variavel e utilizamos a função built-in input para digitarmos uma mensagem

msg = ShowDisclaimer(type_msg) #### Neste ponto instanciamos a classe e atribuimos um objeto, neste caso a mensagem digitada na variavel type_msg

msg.disclaimer() #### Ao Final, chamamos a função disclaimer classe ShowDisclaimer que foi instanciada na variavel msg.
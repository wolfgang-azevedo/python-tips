#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Loop For
# 2020-03-07
#
########################################
#
#
import time

vendors = ["CISCO", "HUAWEI", "JUNIPER", "ERICSSON", "MICROTIK"]

for i in vendors:
    
    if i == 'CISCO':
        print("Connecting to CISCO device....")
        time.sleep(5)
        print('.' * 1000)
        time.sleep(5)
        print("Wait 5 sec...")
        time.sleep(5)
        print("Connected!")
        print('-+' * 50)
        print('\n\n')

    elif i == 'HUAWEI':
        print('Connecting to HUAWEI device...')
        time.sleep(5)
        print('.' * 1000)
        time.sleep(5)
        print("Wait 5 sec...")
        time.sleep(5)
        print("Connected!")
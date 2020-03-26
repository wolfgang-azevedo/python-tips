#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Module Secrets
# 2020-03-26
#
########################################
#
#
import secrets

secret_length = 16

#Getting systemRandom class instance out of secrets module
print(secrets.token_urlsafe(secret_length))

print(secrets.choice('wolfgang'))
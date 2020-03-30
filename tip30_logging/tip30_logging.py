#!/usr/bin/env python3.8
#
########################################
# 
# Python Tips, by Wolfgang Azevedo
# https://github.com/wolfgang-azevedo/python-tips
#
# Module Logging
# 2020-03-30
#
########################################
#
#
import logging
from datetime import datetime

timestamp = datetime.now()

logging.basicConfig(filename='logging_module.log', level=logging.DEBUG)

logging.debug(f'[{timestamp}] - Seu arquivo de log! Bom Trabalho!')

with open('logging_module.log', 'rt') as logfile:
    content = logfile.read()

print(content)

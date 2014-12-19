#!/usr/bin/python

#============================ adjust path =====================================

import sys
import os
if __name__ == "__main__":
    here = sys.path[0]
    sys.path.insert(0, os.path.join(here, '..', '..'))

#============================ imports =========================================

from SmartMeshSDK.HartMgrConnector import HartMgrConnector
from SmartMeshSDK.ApiDefinition   import ApiDefinition,         \
                                         HartMgrDefinition
from SmartMeshSDK.ApiException    import CommandError,          \
                                         ConnectionError

#============================ main ============================================

print 'Simple Application which interacts with the HART manager - (c) Dust Networks'
                                         
print '\n\n================== Step 1. Connecting to the manager =============='

connect = raw_input('\nDo you want to connect to a manager XML API? [y/n] ')

if connect.strip()!='y':
    raw_input('\nScript ended. Press Enter to exit.')
    sys.exit()

print '\n=====\nCreating connector'
connector = HartMgrConnector.HartMgrConnector()
print 'done.'

hartHost = raw_input('\nEnter the Manager\'s ip address (Factory default is 192.168.99.100) ')
#hartHost = raw_input('\nEnter the Manager\'s ip address (leave blank for '+DEFAULT_HOST+') ')
if not hartHost:
    hartHost = DEFAULT_HOST
   
hartPort = raw_input('\nEnter the Manager\'s port (It is normally 4445) ')
#hartPort = raw_input('\nEnter the Manager\'s port (leave blank for '+str(DEFAULT_PORT)+') ')
if hartPort:
    hartPort = int(hartPort)
else:
    hartPort = DEFAULT_PORT



print '\n=====\nConnecting to Hart manager'
try:
    connector.connect({
                        'host': hartHost,
                        'port': hartPort,
                        'user':     'admin',
                        'password': 'admin',
                        'use_ssl':  False,
                     })
except ConnectionError as err:
    print err
    raw_input('\nScript ended. Press Enter to exit.')
    sys.exit(1)
print 'done.'

keepgoing = raw_input('\nDo you want to keep going? [y/n] ')

if keepgoing.strip()!='y':
    raw_input('\nScript ended. Press Enter to exit.')
    sys.exit()

###########


raw_input('\nScript ended. Press Enter to exit.')

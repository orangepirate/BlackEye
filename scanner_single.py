import nmap
import re

commonPrefix = '[++]'
essentialPrefix = '[++]'
midfix = '[--]'

targetIp = input('input the target ip address: ')
#targetIp = '123.58.182.251'

nm = nmap.PortScanner()
ret = nm.scan(targetIp)
commandLine = ret['nmap']['command_line']
scanStats = ret['nmap']['scanstats']
scanResult = ret['scan']

scanTime = scanStats['timestr']
hostName = scanResult[targetIp]['hostnames'][0]['name']
hostType = scanResult[targetIp]['hostnames'][0]['type']
#ipv4 = scanResult[targetIp]['addresses']['ipv4']
#macAddr = scanResult[targetIp]['addresses']['mac']
#vendor = scanResult[targetIp]['vendor'][macAddr]
#status = scanResult[targetIp]['status']['state']
#statusReason = scanResult[targetIp]['status']['reason']
#ports = scanResult[targetIp]['tcp']

print('{}command line: {}'.format(commonPrefix,commandLine))
print('{}scan time; {}'.format(commonPrefix,scanTime))

for key,value in scanResult[targetIp].items():
    if key == 'tcp':
        for subkey,subvalue in value.items():
            print('{}{}:{}\n'.format(essentialPrefix,subkey,subvalue))
            
    else:
        print('{}{}:{}\n'.format(essentialPrefix,key,value))
        print('\n')
    

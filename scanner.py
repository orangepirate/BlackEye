import nmap
import re

commonPrefix = '[++]'
essentialPrefix = '[***]'

targetIp = '192.168.1.80'

nm = nmap.PortScanner()
ret = nm.scan(targetIp)
commandLine = ret['nmap']['command_line']
scanStats = ret['nmap']['scanstats']
scanResult = ret['scan']

scanTime = scanStats['timestr']
hostName = scanResult[targetIp]['hostnames'][0]['name']
hostType = scanResult[targetIp]['hostnames'][0]['type']
ipv4 = scanResult[targetIp]['addresses']['ipv4']
macAddr = scanResult[targetIp]['addresses']['mac']
vendor = scanResult[targetIp]['vendor'][macAddr]

printInfo = {'scanTime':scanTime, 'hostName':hostName, 'hostType':hostType,
        'ipv4':ipv4, 'macAddr':macAddr, 'vendor':vendor}

print('{}command line: {}'.format(commonPrefix,commandLine))
print('{}scan time; {}'.format(commonPrefix,scanTime))

for key,value in printInfo.items():
    print('{}{}: {}'.format(essentialPrefix, key, value)) 




#print('{}scanStats: {}\n'.format(prefix,scanStats))
#print('{}scan result: {}\n'.format(prefix,scanResult))
#print(ret)

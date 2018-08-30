import nmap
import re

commonPrefix = '[++]'
essentialPrefix = '[##]'
midfix = '[--]'

#targetIp = input('input the target ip address: ')
scanIp = '123.58.182.251-252'
targets = {}

nm = nmap.PortScanner()
ret = nm.scan(scanIp)
commandLine = ret['nmap']['command_line']
scanStats = ret['nmap']['scanstats']
scanResult = ret['scan']
scanTime = scanStats['timestr']

print('commandline:{}'.format(commandLine))
print('scanStats:{}'.format(scanStats))
#print('scanresult:{}'.format(scanResult))

def parseTargetResu(targetResult):
    state = targetResult['status']['state']
    vendor = targetResult['vendor']
    portsInfo = targetResult['tcp']
    ports = list(targetResult['tcp'].keys())

    print('state:{}'.format(state))
    print('vendor:{}'.format(vendor))
    print('ports:{}'.format(ports))


for targetIp,targetResult in scanResult.items():
    targets[targetIp] = targetResult
    #print('{}:{}'.format(target,result))
    parseTargetResu(targetResult)

import os
from IPy import IP
import datetime
from update_database import MySqlCommand
from check_modules import checkModules

commonPrefix = '[++]'
essentialPrefix = '[##]'
midfix = '[--]'
portfix = '[port]'

ip_list = []
scaned_ip_list = []
total_ip_list = []

scan_os_service = 'nmap -oX - -sV {}'

def save(text, targetIp):
    f = open('{}.xml'.format(targetIp),'a')
    f.write(text)
    f.close()

def scan_single(command, targetIp='123.58.182.251'):
    print('scanning target ip : {}\n'.format(targetIp))
    scan_command = command.format(targetIp)
    result = os.popen(scan_command).read()
    # save result
    save(result,targetIp)

def parseIps(s):
    for ip in IP(s):
        ip_list.append(ip)


if __name__ == '__main__':
    ips = IP('123.58.182.248/30')
    # parse ips into ip_list
    parseIps(ips)
    # scan target according to ip_list
    for ip in ip_list:
        scan_single(scan_os_service,ip)
from xml.etree.ElementTree import *

class parseScanResult(object):
    # initialization
    def __init__(self):
        self.dev_ip = ''
        self.dev_domain = ''
        self.dev_hostname = ''
        self.dev_hosttype = ''
        self.dev_vendor = ''
        self.dev_state = ''
        self.dev_ports = ''
        self.dev_cpes = ''
        self.dev_portsprotocals = ''
        self.update_time = ''
    # parse nmap scan result xml
    def parseScanResultXml(self,xml):
        txt = parse()


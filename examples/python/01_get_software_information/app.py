from jnpr.junos import Device
from pprint import pprint
import json


with Device(host='192.168.43.201', user='ansible', password='hol-leap!bru6PSOO') as dev:
    try:
        show_version = dev.rpc.get_software_information({'format': 'json'})
    except:
        pass
print('show version: \n' + str(show_version))

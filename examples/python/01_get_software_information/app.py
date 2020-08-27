from jnpr.junos import Device
from pprint import pprint
import json


with Device(host='10.6.5.201', user='automation', password='juniper123') as dev:
    try:
        show_version = dev.rpc.get_software_information({'format': 'json'})
    except:
        pass
print('show version: \n' + str(show_version))

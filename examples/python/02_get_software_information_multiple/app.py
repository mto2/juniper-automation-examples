from jnpr.junos import Device
from pprint import pprint
import requests
import json

devices = [
        "192.168.43.201",
        "192.168.43.202",
        "192.168.43.203",
        "192.168.43.204",
        "192.168.43.205",
        "192.168.43.206"
    ]


list_of_device_output = []
for device in devices:
    with Device(host=device, user='ansible', password='hol-leap!bru6PSOO') as dev:
        try:
            show_version = dev.rpc.get_software_information({'format':'json'})
            payload = {'hostname': device, 'payload': show_version}
            list_of_device_output.append(payload)
        except:
            pass
print('show versions: \n' + str(list_of_device_output))

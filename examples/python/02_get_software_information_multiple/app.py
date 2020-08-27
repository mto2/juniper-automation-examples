from jnpr.junos import Device
from pprint import pprint
import requests
import json

devices = [
        "10.6.5.201",
        "10.6.5.202",
        "10.6.5.203",
        "10.6.5.204",
        "10.6.5.205",
        "10.6.5.206",
        "10.6.5.207",
        "10.6.5.208",
        "10.6.5.209",
        "10.6.5.210"
    ]


list_of_device_output = []
for device in devices:
    with Device(host=device, user='automation', password='juniper123') as dev:
        try:
            show_version = dev.rpc.get_software_information({'format':'json'})
            payload = {'hostname': device, 'payload': show_version}
            list_of_device_output.append(payload)
        except:
            pass
print('show versions: \n' + str(list_of_device_output))

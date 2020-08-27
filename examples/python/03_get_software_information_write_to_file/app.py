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


def write_to_file(device, payload):
    # Open function to open the file "hostname.py" 
    # (same directory) in append mode 
    filename = f"./output/{device}.py"
    file1 = open(filename,"a")
    file1.write(str(payload) + "\n")
    file1.close()
    pass


for device in devices:
    with Device(host=device, user='automation', password='juniper123') as dev:
        try:
            show_version = dev.rpc.get_software_information({'format':'json'})
            write_to_file(device, show_version)
        except:
            pass

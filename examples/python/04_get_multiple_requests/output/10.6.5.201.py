{'multi-routing-engine-results': [{'multi-routing-engine-item': [{'re-name': [{'data': 'fpc0'}], 'software-information': [{'host-name': [{'data': 'core-sw1'}], 'product-model': [{'data': 'vqfx-10000'}], 'product-name': [{'data': 'vqfx-10000'}], 'junos-version': [{'data': '19.4R1.10'}], 'junos-edition': [{'data': 'limited'}], 'package-information': [{'name': [{'data': 'junos'}], 'comment': [{'data': 'JUNOS Base OS boot [19.4R1.10]'}]}, {'name': [{'data': 'jdocs'}], 'comment': [{'data': 'JUNOS Online Documentation [19.4R1.10]'}]}, {'name': [{'data': 'jcrypto'}], 'comment': [{'data': 'JUNOS Crypto Software Suite [19.4R1.10]'}]}, {'name': [{'data': 'jbase'}], 'comment': [{'data': 'JUNOS Base OS Software Suite [19.4R1.10]'}]}, {'name': [{'data': 'jpfe'}], 'comment': [{'data': 'JUNOS Packet Forwarding Engine Support (qfx-10-f) [19.4R1.10]'}]}, {'name': [{'data': 'jkernel'}], 'comment': [{'data': 'JUNOS Kernel Software Suite [19.4R1.10]'}]}, {'name': [{'data': 'jroute'}], 'comment': [{'data': 'JUNOS Routing Software Suite [19.4R1.10]'}]}, {'name': [{'data': 'jswitch'}], 'comment': [{'data': 'JUNOS Enterprise Software Suite [19.4R1.10]'}]}, {'name': [{'data': 'jsdn-i386'}], 'comment': [{'data': 'JUNOS SDN Software Suite [19.4R1.10]'}]}, {'name': [{'data': 'jsd'}], 'comment': [{'data': 'JUNOS jsd [i386-19.4R1.10-jet-1]'}]}, {'name': [{'data': 'jweb'}], 'comment': [{'data': 'JUNOS Web Management [19.4R1.10]'}]}, {'name': [{'data': 'py-base-i386'}], 'comment': [{'data': 'JUNOS py-base-i386 [19.4R1.10]'}]}, {'name': [{'data': 'py-base2-i386'}], 'comment': [{'data': 'JUNOS py-base2-i386 [19.4R1.10]'}]}, {'name': [{'data': 'py-extensions-i386'}], 'comment': [{'data': 'JUNOS py-extensions-i386 [19.4R1.10]'}]}, {'name': [{'data': 'py-extensions2-i386'}], 'comment': [{'data': 'JUNOS py-extensions2-i386 [19.4R1.10]'}]}]}]}]}]}
{'chassis-inventory': [{'chassis': [{'attributes': {'junos:style': 'inventory'}, 'name': [{'data': 'Chassis'}], 'serial-number': [{'data': '87114577881'}], 'description': [{'data': 'QFX3500'}]}]}]}
{'configuration': {'@': {'xmlns': 'http://xml.juniper.net/xnm/1.1/xnm', 'junos:changed-seconds': '1598542474', 'junos:changed-localtime': '2020-08-27 10:34:34 CDT'}, 'version': '20191212.201431_builder.r1074901', 'groups': [{'name': 'IRB_OPTIONS', 'interfaces': {'interface': [{'name': 'irb', 'unit': [{'name': '<*>', 'proxy-macip-advertisement': [None], 'virtual-gateway-accept-data': [None], 'family': {'inet': {'address': [{'name': '<*>', 'primary': [None], 'preferred': [None]}]}}, 'virtual-gateway-v4-mac': '00:5e:5e:5e:00:01'}]}]}}, {'name': 'AE_MTU_JUMBO', 'interfaces': {'interface': [{'name': '<*>', 'mtu': 9192}]}}, {'name': 'AE_LACP_BOND', 'interfaces': {'interface': [{'name': '<*>', 'aggregated-ether-options': {'lacp': {'active': [None], 'periodic': 'slow'}}}]}}], 'system': {'host-name': 'core-sw1', 'root-authentication': {'encrypted-password': '$6$eG4FXiQW$J4/a.5GZlXlrKcvJTpbaMl.qIelPqjR5lFk.POmxo5O3Vp5OdjHFFJ97PMqvABuZZOGXrdvSE6YF3f33wilgO.'}, 'login': {'user': [{'name': 'automation', 'uid': 3001, 'class': 'super-user', 'authentication': {'encrypted-password': '$6$po1LNlij$s7XhHlhUWX.3t3AMepFvfC5BLuxKManQmTbGHwQ8inei5If8aMiP8J4V8qPEu8L9VZkJbT.1Wm8h02d8nnb6e.'}}, {'name': 'cremsburg', 'uid': 3006, 'class': 'super-user', 'authentication': {'encrypted-password': '$6$JX8v3CWG$oLWOKFK0phWqtGrFx7HdeeVcgFRyQULVxgoTD4jMMGVNA87UUxTOYgewuWRwoosfwFqRTLO8zHQXkGWM0yxmT1'}}, {'name': 'cwallace', 'uid': 3004, 'class': 'super-user', 'authentication': {'encrypted-password': '$6$E3nzPlGE$g/SfhM2mAfY4PKusTalWKVXydNR3n8//MRhjwi5LuZ4Xc3C/BLD.f62IuxEAIrTZAP1oB8j3y6F2tM.Bux/ZK1'}}, {'name': 'jthompson', 'uid': 3005, 'class': 'super-user', 'authentication': {'encrypted-password': '$6$9ZDIN/o1$ctt1V9WYpG8LA2iKB7Wn8bSCx785vDBZrSEyJIOGbtyFdXujNsR7fpjKJWpS6m97IpGT0wmJmWdZOB11hI/vQ0'}}, {'name': 'nornir', 'uid': 3003, 'class': 'super-user', 'authentication': {'encrypted-password': '$6$O.kXS5OW$0HsqaFeAb1EXcHaLACw60bFgl/vA9SxxHHRcw1.BZdQwHygXQ0HvSdiKdgIUltO2OGXJWhTXhktZFAoJ2y85W1'}}, {'name': 'packetferret', 'uid': 3002, 'class': 'super-user', 'authentication': {'encrypted-password': '$6$.HKuZDyY$H2rjpnC8wAnzz71hn0WisOjjrg5Ap.Mpqui4/0CMj6G.b5VF6m4ZrsUMkG7stBc3Q8i.HPFleceoM6Kwa7D5c.'}}]}, 'services': {'ssh': {'root-login': 'allow'}, 'netconf': {'ssh': [None]}, 'rest': {'http': {'port': 8080}, 'enable-explorer': [None]}}, 'time-zone': 'America/Chicago', 'name-server': [{'name': '10.6.6.20'}, {'name': '10.6.6.21'}], 'syslog': {'user': [{'name': '*', 'contents': [{'name': 'any', 'emergency': [None]}]}], 'host': [{'name': '10.6.6.101', 'contents': [{'name': 'any', 'any': [None]}], 'port': 5514, 'source-address': '192.168.43.201', 'structured-data': [None]}], 'file': [{'name': 'messages', 'contents': [{'name': 'any', 'notice': [None]}, {'name': 'authorization', 'info': [None]}]}, {'name': 'interactive-commands', 'contents': [{'name': 'interactive-commands', 'any': [None]}]}, {'name': 'default-log-messages', 'contents': [{'name': 'any', 'info': [None]}], 'match': "(requested 'commit' operation)|(requested 'commit synchronize' operation)|(copying configuration to juniper.save)|(commit complete)|ifAdminStatus|(FRU power)|(FRU removal)|(FRU insertion)|(link UP)|transitioned|Transferred|transfer-file|(license add)|(license delete)|(package -X update)|(package -X delete)|(FRU Online)|(FRU Offline)|(plugged in)|(unplugged)|GRES", 'structured-data': [None]}]}}, 'chassis': {'aggregated-devices': {'ethernet': {'device-count': 64}}}, 'interfaces': {'interface': [{'name': 'xe-0/0/0', 'description': '[xe-0/0/0] to dist-sw1 (member of ae11)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae11'}}}, {'name': 'xe-0/0/1', 'description': '[xe-0/0/1] to dist-sw1 (member of ae11)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae11'}}}, {'name': 'xe-0/0/2', 'description': '[xe-0/0/2] to dist-sw2 (member of ae12)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae12'}}}, {'name': 'xe-0/0/3', 'description': '[xe-0/0/3] to dist-sw2 (member of ae12)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae12'}}}, {'name': 'xe-0/0/4', 'description': '[xe-0/0/4] to campus-fw1 (member of ae15)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae15'}}}, {'name': 'xe-0/0/5', 'description': '[xe-0/0/5] to campus-fw1 (member of ae15)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae15'}}}, {'name': 'xe-0/0/6', 'description': '[xe-0/0/6] to campus-rt1 (member of ae16)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae16'}}}, {'name': 'xe-0/0/7', 'description': '[xe-0/0/7] to campus-rt1 (member of ae16)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae16'}}}, {'name': 'xe-0/0/8', 'description': '[xe-0/0/8] to dist-sw3 (member of ae13)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae13'}}}, {'name': 'xe-0/0/9', 'description': '[xe-0/0/9] to dist-sw3 (member of ae13)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae13'}}}, {'name': 'xe-0/0/10', 'description': '[xe-0/0/10] to dist-sw4 (member of ae14)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae14'}}}, {'name': 'xe-0/0/11', 'description': '[xe-0/0/11] to dist-sw4 (member of ae14)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae14'}}}, {'name': 'ae11', 'apply-groups': ['AE_MTU_JUMBO', 'AE_LACP_BOND'], 'description': '[xe-0/0/0-1] to dist-sw1', 'aggregated-ether-options': {'minimum-links': 1, 'lacp': {'active': [None]}}, 'unit': [{'name': 0, 'family': {'inet': {'address': [{'name': '172.16.1.0/31'}]}}}]}, {'name': 'ae12', 'apply-groups': ['AE_MTU_JUMBO', 'AE_LACP_BOND'], 'description': '[xe-0/0/2-3] to dist-sw2', 'aggregated-ether-options': {'minimum-links': 1, 'lacp': {'active': [None]}}, 'unit': [{'name': 0, 'family': {'inet': {'address': [{'name': '172.16.1.2/31'}]}}}]}, {'name': 'ae13', 'apply-groups': ['AE_MTU_JUMBO', 'AE_LACP_BOND'], 'description': '[xe-0/0/8-9] to dist-sw3', 'aggregated-ether-options': {'minimum-links': 1, 'lacp': {'active': [None]}}, 'unit': [{'name': 0, 'family': {'inet': {'address': [{'name': '172.16.1.4/31'}]}}}]}, {'name': 'ae14', 'apply-groups': ['AE_MTU_JUMBO', 'AE_LACP_BOND'], 'description': '[xe-0/0/10-11] to dist-sw4', 'aggregated-ether-options': {'minimum-links': 1, 'lacp': {'active': [None]}}, 'unit': [{'name': 0, 'family': {'inet': {'address': [{'name': '172.16.1.6/31'}]}}}]}, {'name': 'ae15', 'apply-groups': ['AE_MTU_JUMBO', 'AE_LACP_BOND'], 'description': '[xe-0/0/4-5] to campus-fw1', 'aggregated-ether-options': {'minimum-links': 1, 'lacp': {'active': [None]}}, 'unit': [{'name': 0, 'family': {'ethernet-switching': {'interface-mode': 'trunk', 'vlan': {'members': ['vlan_1', 'vlan_2', 'vlan_3']}}}}]}, {'name': 'ae16', 'apply-groups': ['AE_MTU_JUMBO', 'AE_LACP_BOND'], 'description': '[xe-0/0/6-7] to campus-rt1', 'aggregated-ether-options': {'minimum-links': 1, 'lacp': {'active': [None]}}, 'unit': [{'name': 0, 'family': {'inet': {'address': [{'name': '172.16.10.1/31'}]}}}]}, {'name': 'em0', 'unit': [{'name': 0, 'description': 'out of band interface', 'family': {'inet': {'address': [{'name': '192.168.43.201/24'}]}}}]}, {'name': 'em1', 'unit': [{'name': 0, 'family': {'inet': {'address': [{'name': '169.254.0.2/24'}]}}}]}, {'name': 'irb', 'apply-groups': ['IRB_OPTIONS'], 'unit': [{'name': 1, 'family': {'inet': {'address': [{'name': '172.20.1.251/24', 'virtual-gateway-address': '172.20.1.250'}]}, 'inet6': {'address': [{'name': '2001:db8::172:20:1:251/112', 'virtual-gateway-address': '2001:db8::172:20:1:250'}, {'name': 'fe80::172:20:1:251/112'}]}}}, {'name': 2, 'family': {'inet': {'address': [{'name': '172.20.2.251/24', 'virtual-gateway-address': '172.20.2.250'}]}, 'inet6': {'address': [{'name': '2001:db8::172:20:2:251/112', 'virtual-gateway-address': '2001:db8::172:20:2:250'}, {'name': 'fe80::172:20:2:251/112'}]}}}, {'name': 3, 'family': {'inet': {'address': [{'name': '172.20.3.251/24', 'virtual-gateway-address': '172.20.3.250'}]}, 'inet6': {'address': [{'name': '2001:db8::172:20:3:251/112', 'virtual-gateway-address': '2001:db8::172:20:3:250'}, {'name': 'fe80::172:20:3:251/112'}]}}}]}, {'name': 'lo0', 'unit': [{'name': 0, 'description': 'loopback', 'family': {'inet': {'address': [{'name': '192.168.0.1/32'}]}}}, {'name': 1, 'description': 'loopback', 'family': {'inet': {'address': [{'name': '192.168.1.1/32'}]}}}]}]}, 'snmp': {'interface': ['em0.0'], 'community': [{'name': '$home_snmp$', 'authorization': 'read-only', 'clients': [{'name': '10.255.127.0/24'}, {'name': '0.0.0.0/0', 'restrict': [None]}]}], 'trap-options': {'source-address': {'address': '192.168.43.201'}}, 'trap-group': [{'name': 'SNMP_TRAP', 'version': 'v2', 'categories': {'chassis': [None], 'routing': [None]}, 'targets': [{'name': '10.255.127.31'}]}, {'name': 'space', 'version': 'v2', 'targets': [{'name': '10.255.127.33'}]}]}, 'policy-options': {'policy-statement': [{'name': 'ecmp_policy', 'term': [{'name': '10', 'then': {'accept': [None]}}]}]}, 'routing-instances': {'instance': [{'name': 'EVPN_VRF_1', 'routing-options': {'router-id': '192.168.1.1', 'autonomous-system': {'as-number': '64500'}}, 'instance-type': 'vrf', 'interface': [{'name': 'irb.1'}, {'name': 'irb.2'}, {'name': 'irb.3'}, {'name': 'lo0.1'}], 'route-distinguisher': {'rd-type': '192.168.1.1:1'}, 'vrf-target': {'community': 'target:64500:1'}}, {'name': 'VIRTUAL_SWITCH_1', 'protocols': {'evpn': {'encapsulation': 'vxlan', 'extended-vni-list': ['all'], 'default-gateway': 'no-gateway-community'}}, 'description': 'VRF for virtual-switch', 'vtep-source-interface': {'interface-name': 'lo0.0'}, 'instance-type': 'virtual-switch', 'interface': [{'name': 'ae15.0'}], 'route-distinguisher': {'rd-type': '192.168.0.1:1'}, 'vrf-target': {'community': 'target:65100:1111', 'auto': [None]}, 'vlans': {'vlan': [{'name': 'vlan_1', 'vlan-id': 1, 'l3-interface': 'irb.1', 'vxlan': {'vni': 5001, 'ingress-node-replication': [None]}}, {'name': 'vlan_2', 'vlan-id': 2, 'l3-interface': 'irb.2', 'vxlan': {'vni': 5002, 'ingress-node-replication': [None]}}, {'name': 'vlan_3', 'vlan-id': 3, 'l3-interface': 'irb.3', 'vxlan': {'vni': 5003, 'ingress-node-replication': [None]}}]}}]}, 'routing-options': {'static': {'route': [{'name': '10.255.0.0/17', 'next-hop': ['192.168.43.1'], 'no-readvertise': [None]}, {'name': '10.6.6.0/24', 'next-hop': ['192.168.43.1'], 'no-readvertise': [None]}, {'name': '10.9.0.0/16', 'next-hop': ['192.168.43.1'], 'no-readvertise': [None]}]}, 'forwarding-table': {'export': ['ecmp_policy'], 'ecmp-fast-reroute': [None]}, 'router-id': '192.168.0.1', 'autonomous-system': {'as-number': '65100'}}, 'protocols': {'ospf': {'area': [{'name': '0.0.0.0', 'interface': [{'name': 'ae11.0'}, {'name': 'ae12.0'}, {'name': 'ae13.0'}, {'name': 'ae14.0'}, {'name': 'ae16.0'}, {'name': 'lo0.0', 'passive': [None]}]}]}, 'bgp': {'group': [{'name': 'EVPN_FABRIC', 'type': 'internal', 'local-address': '192.168.0.1', 'family': {'evpn': {'signaling': [None]}}, 'cluster': '0.0.0.1', 'multipath': [None], 'neighbor': [{'name': '192.168.0.11', 'description': 'dist-sw1'}, {'name': '192.168.0.12', 'description': 'dist-sw2'}, {'name': '192.168.0.13', 'description': 'dist-sw3'}, {'name': '192.168.0.14', 'description': 'dist-sw4'}], 'vpn-apply-export': [None]}]}, 'lldp': {'port-id-subtype': 'interface-name', 'port-description-type': 'interface-alias', 'interface': [{'name': 'all'}, {'name': 'em0', 'disable': [None]}]}}}}
{'multi-routing-engine-results': [{'multi-routing-engine-item': [{'re-name': [{'data': 'fpc0'}], 'software-information': [{'host-name': [{'data': 'core-sw1'}], 'product-model': [{'data': 'vqfx-10000'}], 'product-name': [{'data': 'vqfx-10000'}], 'junos-version': [{'data': '19.4R1.10'}], 'junos-edition': [{'data': 'limited'}], 'package-information': [{'name': [{'data': 'junos'}], 'comment': [{'data': 'JUNOS Base OS boot [19.4R1.10]'}]}, {'name': [{'data': 'jdocs'}], 'comment': [{'data': 'JUNOS Online Documentation [19.4R1.10]'}]}, {'name': [{'data': 'jcrypto'}], 'comment': [{'data': 'JUNOS Crypto Software Suite [19.4R1.10]'}]}, {'name': [{'data': 'jbase'}], 'comment': [{'data': 'JUNOS Base OS Software Suite [19.4R1.10]'}]}, {'name': [{'data': 'jpfe'}], 'comment': [{'data': 'JUNOS Packet Forwarding Engine Support (qfx-10-f) [19.4R1.10]'}]}, {'name': [{'data': 'jkernel'}], 'comment': [{'data': 'JUNOS Kernel Software Suite [19.4R1.10]'}]}, {'name': [{'data': 'jroute'}], 'comment': [{'data': 'JUNOS Routing Software Suite [19.4R1.10]'}]}, {'name': [{'data': 'jswitch'}], 'comment': [{'data': 'JUNOS Enterprise Software Suite [19.4R1.10]'}]}, {'name': [{'data': 'jsdn-i386'}], 'comment': [{'data': 'JUNOS SDN Software Suite [19.4R1.10]'}]}, {'name': [{'data': 'jsd'}], 'comment': [{'data': 'JUNOS jsd [i386-19.4R1.10-jet-1]'}]}, {'name': [{'data': 'jweb'}], 'comment': [{'data': 'JUNOS Web Management [19.4R1.10]'}]}, {'name': [{'data': 'py-base-i386'}], 'comment': [{'data': 'JUNOS py-base-i386 [19.4R1.10]'}]}, {'name': [{'data': 'py-base2-i386'}], 'comment': [{'data': 'JUNOS py-base2-i386 [19.4R1.10]'}]}, {'name': [{'data': 'py-extensions-i386'}], 'comment': [{'data': 'JUNOS py-extensions-i386 [19.4R1.10]'}]}, {'name': [{'data': 'py-extensions2-i386'}], 'comment': [{'data': 'JUNOS py-extensions2-i386 [19.4R1.10]'}]}]}]}]}]}
{'chassis-inventory': [{'chassis': [{'attributes': {'junos:style': 'inventory'}, 'name': [{'data': 'Chassis'}], 'serial-number': [{'data': '87114577881'}], 'description': [{'data': 'QFX3500'}]}]}]}
{'configuration': {'@': {'xmlns': 'http://xml.juniper.net/xnm/1.1/xnm', 'junos:changed-seconds': '1598542474', 'junos:changed-localtime': '2020-08-27 10:34:34 CDT'}, 'version': '20191212.201431_builder.r1074901', 'groups': [{'name': 'IRB_OPTIONS', 'interfaces': {'interface': [{'name': 'irb', 'unit': [{'name': '<*>', 'proxy-macip-advertisement': [None], 'virtual-gateway-accept-data': [None], 'family': {'inet': {'address': [{'name': '<*>', 'primary': [None], 'preferred': [None]}]}}, 'virtual-gateway-v4-mac': '00:5e:5e:5e:00:01'}]}]}}, {'name': 'AE_MTU_JUMBO', 'interfaces': {'interface': [{'name': '<*>', 'mtu': 9192}]}}, {'name': 'AE_LACP_BOND', 'interfaces': {'interface': [{'name': '<*>', 'aggregated-ether-options': {'lacp': {'active': [None], 'periodic': 'slow'}}}]}}], 'system': {'host-name': 'core-sw1', 'root-authentication': {'encrypted-password': '$6$eG4FXiQW$J4/a.5GZlXlrKcvJTpbaMl.qIelPqjR5lFk.POmxo5O3Vp5OdjHFFJ97PMqvABuZZOGXrdvSE6YF3f33wilgO.'}, 'login': {'user': [{'name': 'automation', 'uid': 3001, 'class': 'super-user', 'authentication': {'encrypted-password': '$6$po1LNlij$s7XhHlhUWX.3t3AMepFvfC5BLuxKManQmTbGHwQ8inei5If8aMiP8J4V8qPEu8L9VZkJbT.1Wm8h02d8nnb6e.'}}, {'name': 'cremsburg', 'uid': 3006, 'class': 'super-user', 'authentication': {'encrypted-password': '$6$JX8v3CWG$oLWOKFK0phWqtGrFx7HdeeVcgFRyQULVxgoTD4jMMGVNA87UUxTOYgewuWRwoosfwFqRTLO8zHQXkGWM0yxmT1'}}, {'name': 'cwallace', 'uid': 3004, 'class': 'super-user', 'authentication': {'encrypted-password': '$6$E3nzPlGE$g/SfhM2mAfY4PKusTalWKVXydNR3n8//MRhjwi5LuZ4Xc3C/BLD.f62IuxEAIrTZAP1oB8j3y6F2tM.Bux/ZK1'}}, {'name': 'jthompson', 'uid': 3005, 'class': 'super-user', 'authentication': {'encrypted-password': '$6$9ZDIN/o1$ctt1V9WYpG8LA2iKB7Wn8bSCx785vDBZrSEyJIOGbtyFdXujNsR7fpjKJWpS6m97IpGT0wmJmWdZOB11hI/vQ0'}}, {'name': 'nornir', 'uid': 3003, 'class': 'super-user', 'authentication': {'encrypted-password': '$6$O.kXS5OW$0HsqaFeAb1EXcHaLACw60bFgl/vA9SxxHHRcw1.BZdQwHygXQ0HvSdiKdgIUltO2OGXJWhTXhktZFAoJ2y85W1'}}, {'name': 'packetferret', 'uid': 3002, 'class': 'super-user', 'authentication': {'encrypted-password': '$6$.HKuZDyY$H2rjpnC8wAnzz71hn0WisOjjrg5Ap.Mpqui4/0CMj6G.b5VF6m4ZrsUMkG7stBc3Q8i.HPFleceoM6Kwa7D5c.'}}]}, 'services': {'ssh': {'root-login': 'allow'}, 'netconf': {'ssh': [None]}, 'rest': {'http': {'port': 8080}, 'enable-explorer': [None]}}, 'time-zone': 'America/Chicago', 'name-server': [{'name': '10.6.6.20'}, {'name': '10.6.6.21'}], 'syslog': {'user': [{'name': '*', 'contents': [{'name': 'any', 'emergency': [None]}]}], 'host': [{'name': '10.6.6.101', 'contents': [{'name': 'any', 'any': [None]}], 'port': 5514, 'source-address': '192.168.43.201', 'structured-data': [None]}], 'file': [{'name': 'messages', 'contents': [{'name': 'any', 'notice': [None]}, {'name': 'authorization', 'info': [None]}]}, {'name': 'interactive-commands', 'contents': [{'name': 'interactive-commands', 'any': [None]}]}, {'name': 'default-log-messages', 'contents': [{'name': 'any', 'info': [None]}], 'match': "(requested 'commit' operation)|(requested 'commit synchronize' operation)|(copying configuration to juniper.save)|(commit complete)|ifAdminStatus|(FRU power)|(FRU removal)|(FRU insertion)|(link UP)|transitioned|Transferred|transfer-file|(license add)|(license delete)|(package -X update)|(package -X delete)|(FRU Online)|(FRU Offline)|(plugged in)|(unplugged)|GRES", 'structured-data': [None]}]}}, 'chassis': {'aggregated-devices': {'ethernet': {'device-count': 64}}}, 'interfaces': {'interface': [{'name': 'xe-0/0/0', 'description': '[xe-0/0/0] to dist-sw1 (member of ae11)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae11'}}}, {'name': 'xe-0/0/1', 'description': '[xe-0/0/1] to dist-sw1 (member of ae11)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae11'}}}, {'name': 'xe-0/0/2', 'description': '[xe-0/0/2] to dist-sw2 (member of ae12)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae12'}}}, {'name': 'xe-0/0/3', 'description': '[xe-0/0/3] to dist-sw2 (member of ae12)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae12'}}}, {'name': 'xe-0/0/4', 'description': '[xe-0/0/4] to campus-fw1 (member of ae15)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae15'}}}, {'name': 'xe-0/0/5', 'description': '[xe-0/0/5] to campus-fw1 (member of ae15)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae15'}}}, {'name': 'xe-0/0/6', 'description': '[xe-0/0/6] to campus-rt1 (member of ae16)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae16'}}}, {'name': 'xe-0/0/7', 'description': '[xe-0/0/7] to campus-rt1 (member of ae16)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae16'}}}, {'name': 'xe-0/0/8', 'description': '[xe-0/0/8] to dist-sw3 (member of ae13)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae13'}}}, {'name': 'xe-0/0/9', 'description': '[xe-0/0/9] to dist-sw3 (member of ae13)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae13'}}}, {'name': 'xe-0/0/10', 'description': '[xe-0/0/10] to dist-sw4 (member of ae14)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae14'}}}, {'name': 'xe-0/0/11', 'description': '[xe-0/0/11] to dist-sw4 (member of ae14)', 'ether-options': {'ieee-802.3ad': {'bundle': 'ae14'}}}, {'name': 'ae11', 'apply-groups': ['AE_MTU_JUMBO', 'AE_LACP_BOND'], 'description': '[xe-0/0/0-1] to dist-sw1', 'aggregated-ether-options': {'minimum-links': 1, 'lacp': {'active': [None]}}, 'unit': [{'name': 0, 'family': {'inet': {'address': [{'name': '172.16.1.0/31'}]}}}]}, {'name': 'ae12', 'apply-groups': ['AE_MTU_JUMBO', 'AE_LACP_BOND'], 'description': '[xe-0/0/2-3] to dist-sw2', 'aggregated-ether-options': {'minimum-links': 1, 'lacp': {'active': [None]}}, 'unit': [{'name': 0, 'family': {'inet': {'address': [{'name': '172.16.1.2/31'}]}}}]}, {'name': 'ae13', 'apply-groups': ['AE_MTU_JUMBO', 'AE_LACP_BOND'], 'description': '[xe-0/0/8-9] to dist-sw3', 'aggregated-ether-options': {'minimum-links': 1, 'lacp': {'active': [None]}}, 'unit': [{'name': 0, 'family': {'inet': {'address': [{'name': '172.16.1.4/31'}]}}}]}, {'name': 'ae14', 'apply-groups': ['AE_MTU_JUMBO', 'AE_LACP_BOND'], 'description': '[xe-0/0/10-11] to dist-sw4', 'aggregated-ether-options': {'minimum-links': 1, 'lacp': {'active': [None]}}, 'unit': [{'name': 0, 'family': {'inet': {'address': [{'name': '172.16.1.6/31'}]}}}]}, {'name': 'ae15', 'apply-groups': ['AE_MTU_JUMBO', 'AE_LACP_BOND'], 'description': '[xe-0/0/4-5] to campus-fw1', 'aggregated-ether-options': {'minimum-links': 1, 'lacp': {'active': [None]}}, 'unit': [{'name': 0, 'family': {'ethernet-switching': {'interface-mode': 'trunk', 'vlan': {'members': ['vlan_1', 'vlan_2', 'vlan_3']}}}}]}, {'name': 'ae16', 'apply-groups': ['AE_MTU_JUMBO', 'AE_LACP_BOND'], 'description': '[xe-0/0/6-7] to campus-rt1', 'aggregated-ether-options': {'minimum-links': 1, 'lacp': {'active': [None]}}, 'unit': [{'name': 0, 'family': {'inet': {'address': [{'name': '172.16.10.1/31'}]}}}]}, {'name': 'em0', 'unit': [{'name': 0, 'description': 'out of band interface', 'family': {'inet': {'address': [{'name': '192.168.43.201/24'}]}}}]}, {'name': 'em1', 'unit': [{'name': 0, 'family': {'inet': {'address': [{'name': '169.254.0.2/24'}]}}}]}, {'name': 'irb', 'apply-groups': ['IRB_OPTIONS'], 'unit': [{'name': 1, 'family': {'inet': {'address': [{'name': '172.20.1.251/24', 'virtual-gateway-address': '172.20.1.250'}]}, 'inet6': {'address': [{'name': '2001:db8::172:20:1:251/112', 'virtual-gateway-address': '2001:db8::172:20:1:250'}, {'name': 'fe80::172:20:1:251/112'}]}}}, {'name': 2, 'family': {'inet': {'address': [{'name': '172.20.2.251/24', 'virtual-gateway-address': '172.20.2.250'}]}, 'inet6': {'address': [{'name': '2001:db8::172:20:2:251/112', 'virtual-gateway-address': '2001:db8::172:20:2:250'}, {'name': 'fe80::172:20:2:251/112'}]}}}, {'name': 3, 'family': {'inet': {'address': [{'name': '172.20.3.251/24', 'virtual-gateway-address': '172.20.3.250'}]}, 'inet6': {'address': [{'name': '2001:db8::172:20:3:251/112', 'virtual-gateway-address': '2001:db8::172:20:3:250'}, {'name': 'fe80::172:20:3:251/112'}]}}}]}, {'name': 'lo0', 'unit': [{'name': 0, 'description': 'loopback', 'family': {'inet': {'address': [{'name': '192.168.0.1/32'}]}}}, {'name': 1, 'description': 'loopback', 'family': {'inet': {'address': [{'name': '192.168.1.1/32'}]}}}]}]}, 'snmp': {'interface': ['em0.0'], 'community': [{'name': '$home_snmp$', 'authorization': 'read-only', 'clients': [{'name': '10.255.127.0/24'}, {'name': '0.0.0.0/0', 'restrict': [None]}]}], 'trap-options': {'source-address': {'address': '192.168.43.201'}}, 'trap-group': [{'name': 'SNMP_TRAP', 'version': 'v2', 'categories': {'chassis': [None], 'routing': [None]}, 'targets': [{'name': '10.255.127.31'}]}, {'name': 'space', 'version': 'v2', 'targets': [{'name': '10.255.127.33'}]}]}, 'policy-options': {'policy-statement': [{'name': 'ecmp_policy', 'term': [{'name': '10', 'then': {'accept': [None]}}]}]}, 'routing-instances': {'instance': [{'name': 'EVPN_VRF_1', 'routing-options': {'router-id': '192.168.1.1', 'autonomous-system': {'as-number': '64500'}}, 'instance-type': 'vrf', 'interface': [{'name': 'irb.1'}, {'name': 'irb.2'}, {'name': 'irb.3'}, {'name': 'lo0.1'}], 'route-distinguisher': {'rd-type': '192.168.1.1:1'}, 'vrf-target': {'community': 'target:64500:1'}}, {'name': 'VIRTUAL_SWITCH_1', 'protocols': {'evpn': {'encapsulation': 'vxlan', 'extended-vni-list': ['all'], 'default-gateway': 'no-gateway-community'}}, 'description': 'VRF for virtual-switch', 'vtep-source-interface': {'interface-name': 'lo0.0'}, 'instance-type': 'virtual-switch', 'interface': [{'name': 'ae15.0'}], 'route-distinguisher': {'rd-type': '192.168.0.1:1'}, 'vrf-target': {'community': 'target:65100:1111', 'auto': [None]}, 'vlans': {'vlan': [{'name': 'vlan_1', 'vlan-id': 1, 'l3-interface': 'irb.1', 'vxlan': {'vni': 5001, 'ingress-node-replication': [None]}}, {'name': 'vlan_2', 'vlan-id': 2, 'l3-interface': 'irb.2', 'vxlan': {'vni': 5002, 'ingress-node-replication': [None]}}, {'name': 'vlan_3', 'vlan-id': 3, 'l3-interface': 'irb.3', 'vxlan': {'vni': 5003, 'ingress-node-replication': [None]}}]}}]}, 'routing-options': {'static': {'route': [{'name': '10.255.0.0/17', 'next-hop': ['192.168.43.1'], 'no-readvertise': [None]}, {'name': '10.6.6.0/24', 'next-hop': ['192.168.43.1'], 'no-readvertise': [None]}, {'name': '10.9.0.0/16', 'next-hop': ['192.168.43.1'], 'no-readvertise': [None]}]}, 'forwarding-table': {'export': ['ecmp_policy'], 'ecmp-fast-reroute': [None]}, 'router-id': '192.168.0.1', 'autonomous-system': {'as-number': '65100'}}, 'protocols': {'ospf': {'area': [{'name': '0.0.0.0', 'interface': [{'name': 'ae11.0'}, {'name': 'ae12.0'}, {'name': 'ae13.0'}, {'name': 'ae14.0'}, {'name': 'ae16.0'}, {'name': 'lo0.0', 'passive': [None]}]}]}, 'bgp': {'group': [{'name': 'EVPN_FABRIC', 'type': 'internal', 'local-address': '192.168.0.1', 'family': {'evpn': {'signaling': [None]}}, 'cluster': '0.0.0.1', 'multipath': [None], 'neighbor': [{'name': '192.168.0.11', 'description': 'dist-sw1'}, {'name': '192.168.0.12', 'description': 'dist-sw2'}, {'name': '192.168.0.13', 'description': 'dist-sw3'}, {'name': '192.168.0.14', 'description': 'dist-sw4'}], 'vpn-apply-export': [None]}]}, 'lldp': {'port-id-subtype': 'interface-name', 'port-description-type': 'interface-alias', 'interface': [{'name': 'all'}, {'name': 'em0', 'disable': [None]}]}}}}

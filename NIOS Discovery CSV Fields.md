# NIOS Discovery CSV Fields

NIOS has multiple discovery mechanisms as part of the DDI solution. Data learnt by these discovery processes populates a set of discovery metadata fields built in to the solution.

Discovery sources include: Built-in network discovery using protocols such as ping, nmap and netbios, Virtual/cloud discovery, Network Insight and external sources such as NetMRI.

To facilitate the synchronisation of discovery data from external sources, such as NetMRI NIOS employs a discovery CSV file format.

A simple example of this file format with some basic discovery metadata is shown below::
	ip_address,last_discovered_timestamp,first_discovered_timestamp,netbios_name,os,discovered_name,discoverer
192.168.1.2,2015-05-15 06:35:41,2015-05-15 06:35:41,FRED,MacOS X,fred.local,AcmeDiscovery
192.168.1.3,2015-05-15 06:35:41,2015-05-15 06:35:41,FRED2,MacOS X,fred2.local,AcmeDiscovery


This can be imported through the API using the fileop API endpoint using the uploadinit and setdiscoverycsv functions. (See NIOS API documentation for details.)


At a high level the process where {{base_url}} = https://<gm>/wapi/<version> is:

POST {{base_url}}/fileop?_function=uploadinit

Capture 
	upload_url = results['url']
        upload_token = results['token']

Upload the file using the returned URL

You can then proceed to use the setdiscoverycsv function:

```
    # Initiate the actual import task.
    req_params = { 'token': upload_token,
                'mergedata': True,
                'network_view': 'default' }
                
    r = session.post(url + 'fileop?_function=setdiscoverycsv',
                    params=req_params)
```

NIOS support multiple metadata fields that are associated with discovery data. Discovery 
The discovery fields available are shown below:

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ UI Field Name                            ┃ CSV Field Name                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ AP Name                                  │ ap_name                                  │
│ Attached Device Address                  │ attached_device_address                  │
│ Attached Device Contact                  │ attached_device_contact                  │
│ Attached Device Description              │ attached_device_description              │
│ Attached Device Location                 │ attached_device_location                 │
│ Attached Device Model                    │ attached_device_model                    │
│ Attached Device Name                     │ attached_device_name                     │
│ Attached Device Port                     │ attached_device_port                     │
│ Attached Device Port Description         │ attached_device_port_description         │
│ Attached Device Port ID                  │ attached_device_port_id                  │
│ Attached Device Port Name                │ attached_device_port_name                │
│ Attached Device Type                     │ attached_device_type                     │
│ Attached Device Vendor                   │ attached_device_vendor                   │
│ Attached Virtual Port Configured Mode    │ attached_virtual_port_configured_mode    │
│ Attached Virtual Port Configured Speed   │ attached_virtual_port_configured_speed   │
│ Attached Virtual Port Link Status        │ attached_virtual_port_link_status        │
│ Attached Virtual Port MAC Address        │ attached_virtual_port_mac_address        │
│ Attached Virtual Port Mode               │ attached_virtual_port_mode               │
│ Attached Virtual Port Name               │ attached_virtual_port_name               │
│ Attached Virtual Port Speed              │ attached_virtual_port_speed              │
│ Attached Virtual Switch ID               │ attached_virtual_switch_id               │
│ Attached Virtual Switch IPv6 Enabled     │ attached_virtual_switch_ipv6_enabled     │
│ Attached Virtual Switch Name             │ attached_virtual_switch_name             │
│ Attached Virtual Switch Type             │ attached_virtual_switch_type             │
│ Attached Virtual Switch VTEP DHCP Server │ attached_virtual_switch_vtep_dhcp_server │
│ Attached Virtual Switch VTEP IP          │ attached_virtual_switch_vtep_ip          │
│ Attached Virtual Switch VTEP Multicast   │ attached_virtual_switch_vtep_multicast   │
│ Attached Virtual Switch VTEP Port Group  │ attached_virtual_switch_vtep_port_group  │
│ Attached Virtual Switch VTEP Type        │ attached_virtual_switch_vtep_type        │
│ Attached Virtual Switch VTEP VLAN        │ attached_virtual_switch_vtep_vlan        │
│ BGP AS                                   │ bgp_as                                   │
│ Bridge Domain                            │ bridge_domain                            │
│ Cisco ISE End Point Profile              │ cisco_ise_end_point_profile              │
│ Cisco ISE SSID                           │ cisco_ise_ssid                           │
│ Cisco ISE Security Group                 │ cisco_ise_security_group                 │
│ Cisco ISE Session State                  │ cisco_ise_session_state                  │
│ Device Contact                           │ device_contact                           │
│ Device Location                          │ device_location                          │
│ Device Management IP                     │ device_management_ip                     │
│ Device Model                             │ device_model                             │
│ Device Port Name                         │ device_port_name                         │
│ Device Port Type                         │ device_port_type                         │
│ Device Type(s)                           │ device_type(s)                           │
│ Device Vendor                            │ device_vendor                            │
│ Discovered MAC Address                   │ discovered_mac_address                   │
│ Discovered Name                          │ discovered_name                          │
│ Discoverer                               │ discoverer                               │
│ EPG                                      │ epg                                      │
│ First Discovered                         │ first_discovered                         │
│ Last Discovered                          │ last_discovered                          │
│ NetBIOS Name                             │ netbios_name                             │
│ Network Segment Available Ports          │ network_segment_available_ports          │
│ Network Segment ID                       │ network_segment_id                       │
│ Network Segment Name                     │ network_segment_name                     │
│ Network Segment Port Group               │ network_segment_port_group               │
│ Network Segment Type                     │ network_segment_type                     │
│ OS                                       │ os                                       │
│ Open Port(s)                             │ open_port(s)                             │
│ Physical Host CIDR Subnet                │ physical_host_cidr_subnet                │
│ Physical Host IP Address                 │ physical_host_ip_address                 │
│ Physical Host MAC Address                │ physical_host_mac_address                │
│ Physical Host Name                       │ physical_host_name                       │
│ Physical Host's NIC Names                │ physical_host's_nic_names                │
│ Port Duplex                              │ port_duplex                              │
│ Port Link                                │ port_link                                │
│ Port Speed                               │ port_speed                               │
│ Port Status                              │ port_status                              │
│ Port Type                                │ port_type                                │
│ SSID                                     │ ssid                                     │
│ Task Name                                │ task_name                                │
│ Tenant                                   │ tenant                                   │
│ VLAN Description                         │ vlan_description                         │
│ VLAN ID                                  │ vlan_id                                  │
│ VLAN Name                                │ vlan_name                                │
│ VRF Description                          │ vrf_description                          │
│ VRF Name                                 │ vrf_name                                 │
│ VRF RD                                   │ vrf_rd                                   │
│ Virtual Cluster                          │ virtual_cluster                          │
│ Virtual Datacenter                       │ virtual_datacenter                       │
│ Virtual Entity Name                      │ virtual_entity_name                      │
│ Virtual Entity Type                      │ virtual_entity_type                      │
│ Virtual Host                             │ virtual_host                             │
│ Virtual Host Adapter                     │ virtual_host_adapter                     │
│ Virtual Machine ID                       │ virtual_machine_id                       │
│ Virtual Machine Name                     │ virtual_machine_name                     │
│ Virtual Machine Port Group               │ virtual_machine_port_group               │
│ Virtual Machine Tenant ID                │ virtual_machine_tenant_id                │
│ Virtual Switch                           │ virtual_switch                           │
└──────────────────────────────────────────┴──────────────────────────────────────────┘
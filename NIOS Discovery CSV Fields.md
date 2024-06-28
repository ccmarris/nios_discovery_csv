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

NIOS support multiple metadata fields that are associated with discovery data. 


## Discovery Metadata

For a complete description of the metadata fields, please see the WAPI
documentation:

https://<GM>/wapidoc/additional/structs.html#discoverydata-discovered-data


An overview of the UI discovery fields and how they map to the API/CSV
are shown in the table below:

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ UI Field Name                            ┃ CSV Field Name                           ┃ Type         |
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩━━━━━━━━━━━━━━┩
│ AP Name                                  │ ap_name                                  │ String       |
│ Attached Device Address                  │ attached_device_address                  │ String       |
│ Attached Device Contact                  │ attached_device_contact                  │ String       |
│ Attached Device Description              │ attached_device_description              │ String       |
│ Attached Device Location                 │ attached_device_location                 │ String       |
│ Attached Device Model                    │ attached_device_model                    │ String       |
│ Attached Device Name                     │ attached_device_name                     │ String       |
│ Attached Device Port                     │ attached_device_port                     │ String       |
│ Attached Device Port Description         │ attached_device_port_description         │ String       |
│ Attached Device Port ID                  │ attached_device_port_id                  │ String       |
│ Attached Device Port Name                │ attached_device_port_name                │ String       |
│ Attached Device Type                     │ attached_device_type                     │ String       |
│ Attached Device Vendor                   │ attached_device_vendor                   │ String       |
│ Attached Virtual Port Configured Mode    │ attached_virtual_port_configured_mode    │ String       |
│ Attached Virtual Port Configured Speed   │ attached_virtual_port_configured_speed   │ String       |
│ Attached Virtual Port Link Status        │ attached_virtual_port_link_status        │ String       |
│ Attached Virtual Port MAC Address        │ attached_virtual_port_mac_address        │ String       |
│ Attached Virtual Port Mode               │ attached_virtual_port_mode               │ String       |
│ Attached Virtual Port Name               │ attached_virtual_port_name               │ String       |
│ Attached Virtual Port Speed              │ attached_virtual_port_speed              │ String       |
│ Attached Virtual Switch ID               │ attached_virtual_switch_id               │ String       |
│ Attached Virtual Switch IPv6 Enabled     │ attached_virtual_switch_ipv6_enabled     │ String       |
│ Attached Virtual Switch Name             │ attached_virtual_switch_name             │ String       |
│ Attached Virtual Switch Type             │ attached_virtual_switch_type             │ String       |
│ Attached Virtual Switch VTEP DHCP Server │ attached_virtual_switch_vtep_dhcp_server │ String       |
│ Attached Virtual Switch VTEP IP          │ attached_virtual_switch_vtep_ip          │ String       |
│ Attached Virtual Switch VTEP Multicast   │ attached_virtual_switch_vtep_multicast   │ String       |
│ Attached Virtual Switch VTEP Port Group  │ attached_virtual_switch_vtep_port_group  │ String       |
│ Attached Virtual Switch VTEP Type        │ attached_virtual_switch_vtep_type        │ String       |
│ Attached Virtual Switch VTEP VLAN        │ attached_virtual_switch_vtep_vlan        │ String       |
│ BGP AS                                   │ bgp_as                                   │ unsigned int |
│ Bridge Domain                            │ bridge_domain                            │ String       |
│ Cisco ISE End Point Profile              │ cisco_ise_end_point_profile              │ String       |
│ Cisco ISE SSID                           │ cisco_ise_ssid                           │ String       |
│ Cisco ISE Security Group                 │ cisco_ise_security_group                 │ String       |
│ Cisco ISE Session State                  │ cisco_ise_session_state                  │ String       |
│ Device Contact                           │ device_contact                           │ String       |
│ Device Location                          │ device_location                          │ String       |
│ Device Management IP                     │ device_management_ip                     │ String       |
│ Device Model                             │ device_model                             │ String       |
│ Device Port Name                         │ device_port_name                         │ String       |
│ Device Port Type                         │ device_port_type                         │ String       |
│ Device Type(s)                           │ device_type                              │ String       |
│ Device Vendor                            │ device_vendor                            │ String       |
│ Discovered MAC Address                   │ discovered_mac_address                   │ String       |
│ Discovered Name                          │ discovered_name                          │ String       |
│ Discoverer                               │ discoverer                               │ String       |
│ EPG                                      │ epg                                      │ String       |
│ First Discovered                         │ first_discovered                         │ Timestamp    |
│ Last Discovered                          │ last_discovered                          │ Timestamp    |
│ NetBIOS Name                             │ netbios_name                             │ String       |
│ Network Segment Available Ports          │ network_segment_available_ports          │ String       |
│ Network Segment ID                       │ network_segment_id                       │ String       |
│ Network Segment Name                     │ network_segment_name                     │ String       |
│ Network Segment Port Group               │ network_segment_port_group               │ String       |
│ Network Segment Type                     │ network_segment_type                     │ String       |
│ OS                                       │ os                                       │ String       |
│ Open Port(s)                             │ open_ports                               │ String       |
│ Physical Host CIDR Subnet                │ physical_host_cidr_subnet                │ String       |
│ Physical Host IP Address                 │ physical_host_ip_address                 │ String       |
│ Physical Host MAC Address                │ physical_host_mac_address                │ String       |
│ Physical Host Name                       │ physical_host_name                       │ String       |
│ Physical Host's NIC Names                │ physical_host's_nic_names                │ String       |
│ Port Duplex                              │ port_duplex                              │ String       |
│ Port Link                                │ port_link                                │ String       |
│ Port Speed                               │ port_speed                               │ String       |
│ Port Status                              │ port_status                              │ String       |
│ Port Type                                │ port_type                                │ String       |
│ SSID                                     │ ssid                                     │ String       |
│ Task Name                                │ task_name                                │ String       |
│ Tenant                                   │ tenant                                   │ String       |
│ VLAN Description                         │ vlan_description                         │ String       |
│ VLAN ID                                  │ vlan_id                                  │ Unsigned Int |
│ VLAN Name                                │ vlan_name                                │ String       |
│ VRF Description                          │ vrf_description                          │ String       |
│ VRF Name                                 │ vrf_name                                 │ String       |
│ VRF RD                                   │ vrf_rd                                   │ String       |
│ Virtual Cluster                          │ virtual_cluster                          │ String       |
│ Virtual Datacenter                       │ virtual_datacenter                       │ String       |
│ Virtual Entity Name                      │ virtual_entity_name                      │ String       |
│ Virtual Entity Type                      │ virtual_entity_type                      │ String       |
│ Virtual Host                             │ virtual_host                             │ String       |
│ Virtual Host Adapter                     │ virtual_host_adapter                     │ String       |
│ Virtual Machine ID                       │ virtual_machine_id                       │ String       |
│ Virtual Machine Name                     │ virtual_machine_name                     │ String       |
│ Virtual Machine Port Group               │ virtual_machine_port_group               │ String       |
│ Virtual Machine Tenant ID                │ virtual_machine_tenant_id                │ String       |
│ Virtual Switch                           │ virtual_switch                           │ String       |
└──────────────────────────────────────────┴──────────────────────────────────────────┘──────────────┘
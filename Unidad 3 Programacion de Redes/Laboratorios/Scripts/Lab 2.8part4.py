#Bryan Adrian Reyes Ibarra
#03 de diciembre del 2023
#Lab 2.8 part 4 loopback

from ncclient import manager
import xml.dom.minidom

m = manager.connect(
        host="10.10.20.48",
        port=830,
        username="developer",
        password="C1sco12345",
        hostkey_verify=False
)

netconf_data = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>111</name>
    <description>TEST1</description>
    <ip>
     <address>
      <primary>
       <address>100.100.100.100</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


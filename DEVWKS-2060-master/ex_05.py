"""
ex-05.py

Purpose:
    UCS Manager VLAN creation example
Author:
    John McDonough (jomcdono@cisco.com) github: (@movinalot)
    Cisco Systems, Inc.
"""

from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

# Create a Login Handle and Login
HANDLE = UcsHandle("13.58.22.56", "admin", "password")
HANDLE.login()

# Query the FabricLanCloud, under which VLAN Objects are inserted
FABRIC_LAN_CLOUD = HANDLE.query_classid("FabricLanCloud")

# Instantiate a VLAN Object, minimally "id" and "name" are required
VLAN = FabricVlan(
    parent_mo_or_dn=FABRIC_LAN_CLOUD[0],
    name="vlan100",
    id="100"
    )

# Add the instantiated VLAN Object to the HANDLE
HANDLE.add_mo(VLAN, modify_present=True)

# Commit the HANDLE to add the VLAN to UCS Manager
HANDLE.commit()

# Logout
HANDLE.logout()

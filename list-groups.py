#!/usr/bin/env python
"""
DESCRIPTION:
    Ansible module to list groups and number of hosts in each group in the inventory.
    The script will use the default inventory in ansible.cfg file, If you didn't specify inventory using "-a" option.

SYNTAX:
    ansible localhost -m list-groups [-a "inventory_file_path"]

VERSION:
    v0.3 - November 2015.

BY:
    Ahmed M. AbouZaid (http://tech.aabouzaid.com/) - Under GPL v2.0 or later.

"""

import os
import re
import sys
import json

# Module arguments file (this how ansible passes the arguments to its module).
module_arguments_file = sys.argv[1]

# Get groups from inventory file and add it to array. 
module_arguments = open(module_arguments_file).readlines()

# Set inventory path, if you didn't provied it with "-a" option,
# it will get the default inventory in ansible.cfg file.
try:
  hosts_file = os.path.expanduser(module_arguments[0])
except IndexError:
  import ConfigParser
  config = ConfigParser.ConfigParser()
  config.read("/etc/ansible/ansible.cfg")
  hosts_file = config.get('defaults', 'inventory')

# Read hosts list from inventory file.
hosts_list = open(hosts_file).readlines()

# Dictionary with Default value for hosts without groups.
group = 'Without group'
groups_list = { group: 0 }

# Loop over inventory file.
for line in hosts_list:
 
 # Skip comments & empty lines.
 line = line.strip()
 if not line or line.startswith('#'):
    continue
 
 # Add group to groups_list dictionary.
 if line.startswith('['):
    group = re.sub(r'[\[\]]', '', line)
    groups_list[group] = 0

 # Count hosts in specific group.
 else:
    groups_list[group] += 1
  
# Print output in JSON format.
print '{"Inventory Groups": ' + json.dumps(groups_list) + '}'

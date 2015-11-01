#! /bin/python
# Ansible module to list groups in inventory (Python version)
# You can print output like "pretty-print" outside Ansible by using:
#./listgroups /path/to/ansible.cfg | python -m json.tool 
 
import sys
import re
import json
  
#get hosts inventory from ansible.cfg file.
ansible_conf_file = open(sys.argv[1]).read()
hosts_file = re.findall('hostfile\s*=\s*(.*)', ansible_conf_file)[0]
  
#Get groups from inventory file and add it to array. 
cat_hosts_file = open(hosts_file).readlines()
group = 'Default' # for hosts without a group
groups_list = {group: 0}
for line in cat_hosts_file:
 
 # Skip comments & empty lines
 line = line.strip()
 if not line or line.startswith('#'):
  continue
 
 if line.startswith('['): # group
  group = re.sub(r'[\[\]]', '', line)
  groups_list[group] = 0
 else: # host
  groups_list[group] += 1
  
#Print output in json format.
print '{"Inventory Groups": ' + json.dumps(groups_list) + '}'

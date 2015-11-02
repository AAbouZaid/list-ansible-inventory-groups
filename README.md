list-ansible-inventory-groups
=========================================

Description.
--------------
Ansible module to list groups and number of hosts in each group in the inventory.

For more information you can check this post:<br />
http://tech.aabouzaid.com/2015/06/ansible-module-to-list-groups-in-inventory-python.html

I got some help from "[Mohammad Tayseer](https://github.com/mtayseer)" about how to make this script "More Pythonic".


Why?
--------------
I've been started using Ansible since v1.7, and I wanted to list groups in inventory file, but not all hosts as in option "--list-hosts", also I wanted to display number of group members.

After small search, I found the "--list-hosts" was able to list groups as well hosts, but reported as a bug because it's called "--list-hosts" not "--list-groups" (and this is actually logical :D), so I made a Ansible module to list groups and number of hosts in each group.


Installation.
--------------
Copy the script to Ansible modules path (make sure it's enabled in your ansible.cfg), and remember to give it execution premesstion.
By default it is:
```
/usr/share/my_modules/
```

Then:
```
chmod +x /usr/share/my_modules/list-groups.py
```


Output example.
--------------
> ansible localhost -m list-groups -a "~/PATH/TO/INVENTORY/FILE"

```
localhost | success >> {
    "Inventory Groups": {
        "Without group": 2,
        "Group1": 5,
        "Group2": 3,
        "Group3": 7
    }
}
```


Version.
--------------
v0.3 - November 2015.


By.
--------------
Ahmed M. AbouZaid [http://tech.aabouzaid.com/](http://tech.aabouzaid.com/) - Under GPL v2.0 or later.


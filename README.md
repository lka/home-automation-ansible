# home-automation-ansible
ansible play books for home automation

installation:

```
md home-automation-ansible
cd home-automation-ansible
#   ---> clone this repository
git clone https://github.com/lka/home-automation-ansible.git
#  ---> create your secrets:
echo "some chars as you want for encryption" > .vault_password_file
cp group_vars/all/secrets.yml.example group_vars/all/secrets.yml
ansible-vault encrypt group_vars/all/secrets.yml

# for each shelly you can create it's own defaults see examples in host_vars/
# but keep in mind to copy all settings from the default. Currently it's not possible
# to overwrite one item.

# to apply all the settings to one shelly:
ansible-playbook -l shellyxx.your.domain shelly.yml
```

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

Git hooks:

1. Set the repository hook path once per clone:

```bash
git config core.hooksPath .githooks
```

2. Der Commit-Hook prüft automatisch, dass `group_vars/all/secrets.yml` nur committet wird, wenn es ansible-vault-verschlüsselt ist.

3. Das Skript liegt im Repository unter `.githooks/pre-commit`.

4. Wenn `group_vars/all/secrets.yml` bereits im Index war, entferne es aus dem Tracking mit:

```bash
git rm --cached group_vars/all/secrets.yml
```

5. Danach committen:

```bash
git add .gitignore README.md .githooks/pre-commit
git commit -m "Add vault protection hook and document hook setup"
```

6. Bei einem neuen Clone müssen Entwickler nur einmal folgende Zeile ausführen:

```bash
git config core.hooksPath .githooks
```

7. Der Hook schützt nur die gestagte Datei. Nicht-tracked Dateien werden weiterhin lokal behalten und nicht committet.

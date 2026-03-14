# nxrseCrypt

**⚖️ License:** GNU General Public License v2.0

**🚀 Version:** Beta


## 📋 Overview

**This software is still in Beta! And is not intended for use, (yet)**

`nxrseCrypt` is a lightweight CLI text encryption/decryption tool, coded in python3.  
It uses mapping files stored in `~/nxrsecrypt/data/encryption_mappings` to convert characters into chunks of random chracters. Only users with the correct corresponding mapping file can decrypt the text.

![nxrseCrypt in action](images/use_case_screenshot.jpg)

nxrseCrypt is my first major project and GitHub repository, created primarily to improve my programming, Git, and documentation skills.
While it was originally built for private communication, it is not intended for production use at this time.

**I welcome criticism, and forks. if this inspires anyone to build an improved open-source version, i would love to see that.**

Only tested on Linux, \
Let me know if it's compatible with windows and/or macos

## ✨ Features

- 🔐 Encrypt text using a mapping file.
- 🔓 Decrypt text with the corresponding mapping.
- 🗺️ Support for multiple mapping tables.
- ⚙️ Editable config file.
- ⚠️ Error messages for unsupported characters, invalid encrypted input, etc.
- 💬 CLI feedback with success, error, and info messages.

## 🎯 Use Cases

**Privately messaging others**\
Create an encryption map for a person or group, securely share it with them, and communicate using encrypted text.

**Encrypting documents on external storage**\
If you store sensitive files (notes, passwords, etc.) on a USB drive or other external device, anyone who gets access could read them. Encrypt the text with nxrseCrypt so it cannot be viewed without the corresponding encryption map.

### 🔐 Extra Security Tip

Consider storing several decoy encryption mappings alongside your real ones, and avoid naming important mappings after their actual purpose.

For example, keep 20+ mappings with generic or misleading names. If someone gains access to your system, it becomes much harder for them to identify which mapping is actually used for decrypting sensitive data.


## 📥 Installation

### 1. 🔗 Clone the repository:

```fish
git clone https://github.com/nxrs3/nxrsecrypt
```

### 2. Installing dependencies: the 'rich' Python module

#### 🐧 Linux

```bash
python3 -m venv ~/nxrsecrypt-venv
source ~/nxrsecrypt-venv/bin/activate
pip install rich
deactivate
```

#### 🪟 Windows

```powershell
python -m venv $HOME\nxrsecrypt-venv
$HOME\nxrsecrypt-venv\Scripts\Activate.ps1
pip install rich
deactivate
```

### 3. ▶️ Create a command to easily run nxrsecrypt:

#### 🐧 Linux

##### using bash:

```bash
echo 'nxrsecrypt() { source ~/nxrsecrypt-venv/bin/activate && python3 ~/nxrsecrypt/main.py; }' >> ~/.bashrc
source ~/.bashrc
```

##### using zsh:

```zsh
echo 'nxrsecrypt() { source ~/nxrsecrypt-venv/bin/activate && python3 ~/nxrsecrypt/main.py; }' >> ~/.zshrc
source ~/.zshrc
```

##### using fish:

```fish
function nxrsecrypt
    source ~/nxrsecrypt-venv/bin/activate.fish
    python3 ~/nxrsecrypt/main.py
end
funcsave nxrsecrypt
```

#### 🪟 Windows (PowerShell)

```
function nxrsecrypt {
    & $HOME\nxrsecrypt-venv\Scripts\Activate.ps1
    python $HOME\nxrsecrypt\main.py
}
Set-Alias nxrsecrypt nxrsecrypt
```

## 🛠️ Usage & commands

### ▶️ Run nxrsecrypt
```
nxrsecrypt
```

### 🛠️ nxrseCrypt commands

commands are split by ' // ' so for instance, in the command 'a // x // y // z':
'a' is the command, 'x' is argument 1, 'y' is argument 2, 'z' is argument 3

#### 📌 Basic commands:

Show command overview:
```
lc
```
Exit nxrsecrypt:
```
exit
```
Clear history:
```
clear
```
Restart nxrsecrypt:
```
restart
```
Update nxrsecrypt:
```
update
```

#### 🗺️ Creating and managing encryption maps:

Listing encryption maps:
```
list-em
```
Deleting an encryption map:
```
del-em // <name of mapping>
```
Generate a map:
```
gen-em // <name> // <chunk length/strength (3-10)> // <character list (anything other than default is not necessary.)>
```
displaying a map:
```
get-em // <name of mapping>
```

#### 📄 Managing encryption mapping character lists, if anything other than the default list is needed:

Listing character lists:
```
list-cl
```
Deleting a character list:
```
del-em // <name of character list>
```
Creating a list:
```
create-cl // <name> // <characters>
```
Displaying a character list:
```
get-cl // <name of list>
```

#### 🔐 Encryption:

Encrypting text:
```
encrypt // <encryption mapping> // <text>
```
Decrypting encrypted text:
```
decrypt // <encryption mapping> // <text>
```

#### 🔄 Reinitialization:
If you wish to reset the state of encryption mappings, character lists, config file,
and other general data, run:
```
reset
```

### ⚙️ Configuration

#### 🔧 Manual configuration

Edit the user config file located ~/nxrsecrypt/config.

To add what you modified to the actual config:
```
load-config
```
and
```
restart
```
\
To reset the config:
```
reset-config
```
and
```
restart
```

#### </> Cli configuration (NEW)

View the config
```
get-config
```

Change a variable in the config:
```
set-config // <variable> // <new value>
```
then restart:
```
restart
```

#### ⚠️ Fixing Config Errors

If a misconfiguration causes an error in modules/config.py when running nxrsecrypt, reset the config by entering this in your terminal:
```
python3 ~/nxrsecrypt/configless_config_reset.py
```

\
\
© 2026 nxrs3 - GNU GPL v2.0

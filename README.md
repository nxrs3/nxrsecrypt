# nxrseCrypt

**Version:** Beta


## Overview

`nxrseCrypt` is a lightweight CLI encryption/decryption tool, coded in python3.  
It uses mapping files stored in `data/encryption_mappings` to convert characters into chunks of random chracters. Only users with the correct corresponding mapping file can decrypt the text.

This is my first big project, and is not a professional, i made this for fun to communicate privatly with my friends.
Feel free to criticize.


## ✨ Features

- 🔐 Encrypt text using a mapping file.
- 🔓 Decrypt text with the corresponding mapping.
- 🗺️ Support for multiple mapping tables.
- </> Commands to manage and generate mappings.
- ⚙️ Editable config file.
- ⚠️ Error messages for unsupported characters, invalid encrypted input, etc.
- 💬 CLI feedback with success, error, and info messages.


## 📥 Installation

1. 🔗 Clone the repository:

```
git clone https://github.com/nxrs3/nxrsecrypt
```

3. 🎨 Install the 'rich' python module:

using pip:

```
pip install rich
```

using pacman:

```
sudo pacman -S python-rich
```

using apt:

```
apt install python3-rich
```

2. </> Create a command to easily run nxrsecrypt:

using bash:

```
echo 'mycmd() { python3 ~/nxrsecrypt/main.py; }' >> ~/.bashrc   # Bash  
source ~/.bashrc
```

using zsh:

```
echo 'nxrsecrypt() { python3 ~/nxrsecrypt/main.py; }' >> ~/.zshrc    # Zsh  
source ~/.zshrc
```

using fish:

```
function nxrsecrypt  
    python3 ~/nxrsecrypt/main.py  
end  
funcsave nxrsecrypt
```


## 🛠️ Usage

i'll get to this later

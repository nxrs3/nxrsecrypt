# nxrseCrypt

**Version:** v-alpha


## Overview

`nxrseCrypt` is a lightweight CLI encryption/decryption tool.  
It uses mapping files stored in `data/encryption_mappings` to convert characters into tokens. Only users with the correct mapping file can decrypt the text.

This is my first big project, and is not a professional, i made this for fun to communicate privatly with my friends.


## Features

- Encrypt text using a mapping file.
- Decrypt text with the corresponding mapping.
- Support for multiple mapping tables.
- Clear error messages for unsupported characters or invalid encrypted input.
- CLI feedback with success, error, and process messages.


## Installation

1. Clone the repository:

```
git clone <your-repo-url>
```


2. Create a command to easily run nxrsecrypt:

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


3. installing the 'rich' python module:

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

#!/usr/bin/python3

# to take config changes into effect enter the command 'load-config'
# to reset to the default config enter the command 'reset-config'
# !! config runs on python !!

import os
from getpass import getuser

# directory & file locations | only edit this if your nxrsecrypt dir is actually any other place than ~/
home = os.path.expanduser("~")
location = os.path.join(home, "nxrsecrypt")
main_py_location = os.path.join(location, "main.py")
data_location = os.path.join(location, "data")
em_location = os.path.join(data_location, "encryption_mappings")
char_list_location = os.path.join(em_location, "character_lists")
example_em_location = os.path.join(data_location, "example_em")
default_cl_location = os.path.join(data_location, "default_cl")
default_config_location = os.path.join(data_location, "default_config")
config_location = os.path.join(location, "config")
config_module_location = os.path.join(location, "modules", "config.py")

# program information | editing correctly wont break anything, edit if you want
version = "beta"

# other information | editing correctly wont break anything, edit if you want
user = getuser()

# customization | feel free to edit, as long as you know rich's color system
error_color = "bold red"
success_color = "bold green"
info_color = "italic blue"
headline_color = "bold cyan"
result_color = "bold blue"
command_prompt_color = "cyan"
welcome_message = True
headline_text = f"--- nxrseCrypt - v-{version} - MIT License | (c) 2026 nxrs3 ---"
command_prompt = f"{user} - nxrsecrypt"

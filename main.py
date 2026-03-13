#!/usr/bin/python3
from modules import cli_system, command_functions
from modules.config import *
from rich import print
import os

def clear():
    cli_system.clear_history(headline_text)

def welcome_user():
    new_user_path = os.path.join(data_location, "new_user")
    new_user = os.path.exists(new_user_path)
    if new_user:
        with open(os.path.join(data_location, "copyright_message"), "r") as f:
            print(f.read())
        print(f"  welcome to nxrsecrypt {user}, the README.md contains the documentation you need")
        os.remove(new_user_path)
    else:
        print(f"  welcome back, {user}")
    print("  type 'lc' to view commands")

# -----------------------------
# Command map
# -----------------------------
commands = {
    "lc": command_functions.show_commands,
    "exit": command_functions.exit_nxrsecrypt,
    "restart": command_functions.restart_nxrsecrypt,
    "clear": command_functions.clear_terminal,
    "info": command_functions.show_info,
    "list-em": command_functions.list_em,
    "get-em": command_functions.get_em,
    "encrypt": command_functions.encrypt,
    "decrypt": command_functions.decrypt,
    "gen-em": command_functions.generate_em,
    "del-em": command_functions.delete_em,
    "list-cl": command_functions.list_cl,
    "create-cl": command_functions.create_cl,
    "del-cl": command_functions.delete_cl,
    "get-cl": command_functions.get_cl,
    "load-config": command_functions.load_config,
    "reset-config": command_functions.reset_config,
    "get-config": command_functions.get_config,
    "set-config": command_functions.set_config,
    "reset": command_functions.reset,
    "update": command_functions.update,
}

# -----------------------------
# Main loop
# -----------------------------
def main():
    clear()
    if welcome_message:
        welcome_user()
    while True:
        args = cli_system.prompt(command_prompt, " // ")
        cmd = args[0]
        if cmd in commands:
            commands[cmd](args)
        elif cmd == "" or cmd is None:
            continue
        else:
            cli_system.error(f"'{cmd}' is not a recognised command")

if __name__ == "__main__":
    main()

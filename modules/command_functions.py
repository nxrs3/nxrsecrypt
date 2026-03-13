#!/usr/bin/python3
from . import cli_system, encryption, map_generator, config_mgmt
from .config import *
from rich import print
import os
import shutil
import sys
import subprocess

def clear():
    cli_system.clear_history(headline_text)

# ---------------------------------------------

def show_commands(args):
    cli_system.display_command_overview(os.path.join(data_location, "command_overview"))

def exit_nxrsecrypt(args):
    os.system("cls" if os.name == "nt" else "clear")
    sys.exit()

def restart_nxrsecrypt(args):
    cli_system.reload(main_py_location)

def clear_terminal(args):
    clear()

def show_info(args):
    print()
    print("   version:", version)
    print("   license:", License)
    print("   contact me at:", "nxrs3@proton.me")
    print("   description:", description)

def list_em(args):
    files = [f for f in os.listdir(em_location) if os.path.isfile(os.path.join(em_location, f))]
    if files:
        print("   ", end="")
        print(str(files).strip("[]"))
    else:
        print("   no encryption mappings")

def get_em(args):
    arg1 = args[1]
    if arg1 is not None:
        path = os.path.join(em_location, arg1)
        if os.path.exists(path):
            with open(path, "r") as f:
                print(f.read())
        else:
            cli_system.error(f"encryption mapping '{arg1}' does not exist")
    else:
        cli_system.error("you did not specify an encryption mapping")

def encrypt(args):
    arg1, arg2 = args[1], args[2]
    if arg1 is None:
        cli_system.error("you did not specify a mapping")
        return
    if arg2 is None:
        cli_system.error("you did not include text to encrypt")
        return

    mapping_path = os.path.join(em_location, arg1)
    if not os.path.exists(mapping_path):
        cli_system.error(f"encryption mapping '{arg1}' does not exist")
        return

    cli_system.info(f"encrypting '{arg2}' using '{arg1}' mapping")
    mapping = encryption.load_mapping(mapping_path)
    unsupported = sorted(set(ch for ch in arg2 if ch not in mapping))
    if unsupported:
        cli_system.error(f"text contains characters not supported by mapping: {', '.join(unsupported)}")
        return

    encrypted_text = encryption.encrypt(arg2, mapping)
    cli_system.success("text encrypted")
    print(f"   [{result_color}]encrypted text:[/{result_color}]", encrypted_text)

def decrypt(args):
    arg1, arg2 = args[1], args[2]
    if arg1 is None:
        cli_system.error("you did not specify a mapping")
        return
    if arg2 is None:
        cli_system.error("you did not include text to decrypt")
        return

    mapping_path = os.path.join(em_location, arg1)
    if not os.path.exists(mapping_path):
        cli_system.error(f"encryption mapping '{arg1}' does not exist")
        return

    cli_system.info(f"decrypting '{arg2}' using '{arg1}' mapping")
    mapping = encryption.load_mapping(mapping_path)
    decrypted_text = encryption.decrypt(arg2, mapping)
    if decrypted_text:
        cli_system.success("text decrypted")
        print(f"   [{result_color}]decrypted text:[/{result_color}]", decrypted_text)

def generate_em(args):
    arg1, arg2, arg3 = args[1], args[2], args[3]
    if arg1 is None:
        cli_system.error("'gen-em' command requires mapping name")
        return
    if arg2 is None:
        cli_system.error("'gen-em' command requires chunk length")
        return

    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789_"
    if any(c not in allowed_chars for c in arg2):
        cli_system.error(f"argument 2: '{arg2}', can only contain integers")
        return

    if arg3 is None:
        arg3 = "n/a"
    map_generator.generate_map(arg1, int(arg2), arg3)

def delete_em(args):
    arg1 = args[1]
    if arg1 is None:
        cli_system.error("encryption map is not specified")
        return

    path = os.path.join(em_location, arg1)
    if os.path.exists(path):
        os.remove(path)
        cli_system.success(f"deleted encryption mapping '{arg1}'")
    else:
        cli_system.error(f"encryption map '{arg1}' does not exist")

def list_cl(args):
    files = [f for f in os.listdir(char_list_location) if os.path.isfile(os.path.join(char_list_location, f))]
    if files:
        print("   ", end="")
        print(str(files).strip("[]"))
    else:
        print("   no mapping character lists")

def create_cl(args):
    arg1, arg2 = args[1], args[2]
    if arg1 is None:
        cli_system.error("'create-cl' command requires character list name")
        return
    if arg2 is None:
        cli_system.error("'create-cl' command requires character list characters")
        return

    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789_"
    if any(c not in allowed_chars for c in arg1):
        cli_system.error(f"name '{arg1}' contains invalid characters")
        print("    allowed characters are: ", end="")
        print(", ".join(allowed_chars))
        return

    path = os.path.join(char_list_location, arg1)
    with open(path, "w") as f:
        f.write(arg2)
    cli_system.success(f"wrote '{arg2}' to the new character list '{arg1}'")

def delete_cl(args):
    arg1 = args[1]
    if arg1 is None:
        cli_system.error("character list is not specified")
        return
    path = os.path.join(char_list_location, arg1)
    if not os.path.exists(path):
        cli_system.error(f"character list '{arg1}' does not exist")
        return
    if arg1 == "default":
        cli_system.error("cannot delete default character list")
        return
    os.remove(path)
    cli_system.success(f"deleted encryption mapping character list '{arg1}'")

def get_cl(args):
    arg1 = args[1]
    if arg1 is None:
        cli_system.error("you did not specify a character list")
        return
    path = os.path.join(char_list_location, arg1)
    if os.path.exists(path):
        with open(path, "r") as f:
            print("   ", end="")
            print(f.read())
    else:
        cli_system.error(f"encryption mapping character list '{arg1}' does not exist")

def load_config(args):
    cli_system.load_config(config_location, config_module_location)
    cli_system.success("loaded config")

def reset_config(args):
    cli_system.info("resetting config file")
    with open(default_config_location, "r") as f:
        default_config = f.read()
    with open(config_location, "w") as f:
        f.write(default_config)
    cli_system.load_config(config_location, config_module_location)
    cli_system.success("reset config")

def get_config(args):
    with open(config_module_location, "r") as f:
        config = f.read()
    print()
    print(config)

def set_config(args):
    arg1, arg2 = args[1], args[2]
    if arg1 is None:
        cli_system.error("you did not specify a config variable")
        return
    if arg2 is None:
        cli_system.error("you did not specify a value")
        return
    config_mgmt.replace_value(config_location, arg1, arg2)

def reset(args):
    reset_confirmation = input("   are you sure? (y/n): ")
    if reset_confirmation == "y":
        new_user_path = os.path.join(data_location, "new_user")
        with open(new_user_path, "w") as f:
            cli_system.info("regenerated 'new_user' file")
        cli_system.info("deleting 'encryption_mappings' folder and creating a new one")
        shutil.rmtree(em_location, ignore_errors=True)
        os.makedirs(os.path.join(em_location, "character_lists"), exist_ok=True)
        cli_system.info("regenerating 'example' encryption mapping")
        with open(example_em_location, "r") as f:
            example_em = f.read()
        with open(os.path.join(em_location, "example"), "w") as f:
            f.write(example_em)
        cli_system.info("regenerating 'default' encryption mapping character list")
        with open(default_cl_location, "r") as f:
            default_cl = f.read()
        with open(os.path.join(char_list_location, "default"), "w") as f:
            f.write(default_cl)
        cli_system.info("resetting config file")
        with open(default_config_location, "r") as f:
            default_config = f.read()
        with open(config_location, "w") as f:
            f.write(default_config)
        cli_system.load_config(config_location, config_module_location)
        cli_system.success("reset nxrsecrypt")
    else:
        cli_system.info("reset aborted")

def update(args):
    cli_system.info("pulling latest changes")
    result = subprocess.run(
        ["git", "pull"],
        cwd=location,
        capture_output=True,
        text=True
    )
    for line in result.stdout.splitlines():
        print("   " + line)
    for line in result.stderr.splitlines():
        print("   " + line)

def reinstall(args):
    reset_confirmation = input("   are you sure? (y/n): ")
    if reset_confirmation == "y":
        cli_system.info("deleting nxrsecrypt directory")
        shutil.rmtree(location)
        result = subprocess.run(
            ["git", "clone", "https://github.com/nxrs3/nxrsecrypt"],
            cwd=home,
            capture_output=True,
            text=True
        )
        for line in result.stdout.splitlines():
            print("   " + line)
        for line in result.stderr.splitlines():
            print("   " + line)
        cli_system.info("restarting")
        cli_system.reload(main_py_location)
    else:
        cli_system.info("reinstall aborted")

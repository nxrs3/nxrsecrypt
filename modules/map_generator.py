#!/usr/bin/python3
import random
import string
import os
from .config import *
from . import cli_system

def generate_map(name: str, length: int, char_list: str) -> None:
    """
    Generate a character-to-chunk mapping and save it to a file.

    Parameters:
        name (str): filename to save the mapping in encryption_mappings/
        length (int): chunk length (2-6)
        char_list (str): name of character list to use

    Returns:
        None
    """
    
    if not char_list or char_list == "n/a":
        char_list = "default"

    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789_"
    if any(c not in allowed_chars for c in name):
        cli_system.error(f"name '{name}' contains invalid characters")
        print("    allowed characters are: ", ", ".join(allowed_chars))
        return

    if not (3 <= length <= 10):
        cli_system.error("chunk length must be between 3 and 10")
        return
    
    # Load characters from char list
    char_list_path = os.path.join(char_list_location, char_list)
    if not os.path.exists(char_list_path):
        cli_system.info(f"character list '{char_list}' does not exist. using 'default' character list")
        char_list_path = os.path.join(char_list_location, "default")
    else:
        cli_system.info(f"generating map using '{char_list}' character list")

    with open(char_list_path, "r") as f:
        chars = list(f.read().replace("\n", ""))

    # Characters to use for chunks
    chunk_chars = string.ascii_letters + string.digits + "!@#$&*-_=;:,./?~"

    mapping = {}
    used_chunks = set()

    for ch in chars:
        while True:
            chunk = ''.join(random.choices(chunk_chars, k=length))
            if chunk not in used_chunks:
                mapping[ch] = chunk
                used_chunks.add(chunk)
                break

    # Save mapping to file
    file_path = os.path.join(em_location, name)
    with open(file_path, "w") as f:
        for k in chars:
            f.write(f"{k} = {mapping[k]}\n")

    cli_system.success(f"mapping saved to {file_path}")


def make_char_list(name: str, chars: str):
    """
    Save a new character list to the character lists directory.
    """
    if not name or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789_" for c in name):
        cli_system.error(f"invalid character list name '{name}'")
        return

    path = os.path.join(char_list_location, name)
    with open(path, "w") as f:
        f.write(chars)
    cli_system.success(f"character list '{name}' saved")

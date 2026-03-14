#!/usr/bin/python3
from .config import *
import os
import subprocess
from rich import print
from typing import Optional, Tuple

def clear_history(text: str):
    """Clears the terminal and prints a headline message."""
    os.system("cls" if os.name == "nt" else "clear")
    print(f"[{headline_color}] {text} [/{headline_color}]")
    print()

def reload(path: str):
    """Reloads the given Python script and exits the current process."""
    subprocess.run("python3 " + path, shell=True)
    exit()

def error(message: str):
    """Prints an error message in the configured error color."""
    print(f"   [{error_color}]Error:[/{error_color}] {message}")

def success(message: str):
    """Prints a success message in the configured success color."""
    print(f"   [{success_color}]Success![/{success_color}] {message}")

def info(message: str):
    """Prints an info message in the configured info color."""
    print(f"   [{info_color}]info: [/{info_color}]{message}...")

def load_config(config: str, config_module: str):
    """Copies the user config file to the config module."""
    info("copying user config file to config module")
    with open(config, "r") as f:
        config_contents = f.read()
    with open(config_module, "w") as f:
        f.write(config_contents)
    success("config saved, restart to take the new config into effect")

def display_command_overview(command_overview_path: str):
    """Displays the contents of a command overview file."""
    with open(command_overview_path) as f:
        commands = f.read()
        print(commands)

def prompt(prompt: str, splitter: str) -> Tuple[Optional[str], ...]:
    """
    Prompts the user for input, splits it using the given splitter,
    fills up to 8 arguments with None if not provided, and returns as a tuple.

    Example:
        >>> command("Enter args", " // ")
        ('arg1', 'arg2', None, None, None, None, None, None)
    """
    MAX_ARGS = 8
    print(f"[{command_prompt_color}]  {prompt} > [/{command_prompt_color}]", end="")
    raw_args = input().split(splitter)
    args = [(arg if arg != "" else None) for arg in raw_args][:MAX_ARGS]
    args += [None] * (MAX_ARGS - len(args))
    return tuple(args)

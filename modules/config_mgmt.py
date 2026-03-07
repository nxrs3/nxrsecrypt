from modules import cli_system

def replace_value(file_path, config_variable, new_value):
    with open(file_path, "r") as f:
        lines = f.readlines()

    found = False

    for i, line in enumerate(lines):
        name, sep, value = line.partition("=")
        if name.strip() == config_variable:
            lines[i] = f"{name.strip()} = {new_value}\n"
            found = True
            break

    if not found:
        cli_system.error(f"{config_variable} not found in file")
        return

    with open(file_path, "w") as f:
        f.writelines(lines)
    cli_system.success(f"set variable '{config_variable} to '{new_value}'")

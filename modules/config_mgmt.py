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

def emergency_config_reset(default_conf_path, config_module_path, user_config_path):
    cli_system.error("error in config, resetting to default config")

    with open(default_conf_path, "r") as f:
        default_config = f.read()

    with open(config_module_path, "w") as f:
        f.write(default_config)
    with open(user_config_path, "w") as f:
        f.write(default_config)

import os
import subprocess

location = os.path.join(os.path.expanduser("~"), "nxrsecrypt")
default_config_location = os.path.join(location, "data", "default_config")
config_location = os.path.join(location, "config")
config_module_location = os.path.join(location, "modules", "config.py")

with open(default_config_location, "r") as f:
    default_config = f.read()
with open(config_location, "w") as f:
    f.write(default_config)
with open(config_module_location, "w") as f:
    f.write(default_config)
    
subprocess.run("python3 " + os.path.join(location, "main.py"), shell=True)
exit()

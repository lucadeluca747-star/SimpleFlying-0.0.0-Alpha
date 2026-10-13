import os
import pyfiglet
RED = "\033[31m"
RESET = "\033[0m"
GREEN = "\033[32m"
print(GREEN + pyfiglet.figlet_format("Simple\nFlying", font="ansi_shadow") + RESET)


print(RED + "this is the setup.py file, to load the actual game it will take around 30 seconds" + RESET)
path = os.path.abspath("main.py")
os.system("pip install ursina")
os.system(f'python "{path}"')

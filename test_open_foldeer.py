import os
import subprocess, io

path = "C:\\Users\\rajat\\Downloads"


subprocess.Popen(f'explorer {os.path.realpath(path)}')
# C:\Users\rajat\OneDrive\Documents --Document
# C:\Users\rajat\Downloads

try:

    External_HardDrive = "F:\\Movies\\HollyWood"
    subprocess.Popen(f'explorer {os.path.realpath(External_HardDrive)}')
except Exception as e:
    print(e)
    # speak('Say that Again ...')
    print('Hard-drive not connected')



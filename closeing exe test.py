import os

EdgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
# p = os.startfile(EdgePath)


import subprocess

p = subprocess.Popen(EdgePath)
p.terminate()

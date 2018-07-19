import subprocess
import os

appname=""
path="/usr/bin/"
output = str(os.popen('wmctrl -l -x').read())
window_list = os.popen('xdotool search --onlyvisible --name '+appname).read()
#This cycles between windows of one app continously
if appname in str(output): 
    print(window_list)
    for item in window_list.split("\n"):
        if os.popen('xdotool getactivewindow').read() != item:

            os.popen('xdotool windowactivate '+item.strip())
            break
#Starts the app
else: 
    subprocess.Popen([path+appname])
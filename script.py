import os
import subprocess
import sys
import re

#[W[%][xH[%]]][{+-}X[%]{+-}Y[%]] | [X[%]:Y[%]]

re_geo = ".*[0-9]+.*"

saw_directory = os.path.dirname(os.path.realpath(__file__))
print(sys.executable)
print(os.path.realpath(__file__))
print("SAW directory: " + saw_directory)

url = sys.argv[1]
# find screens and their dims
# I use directly xrandr so that no unconvenient python dependencies are needed
screens = []
stream = os.popen('xrandr | grep " connected"')
output = stream.read()
for str_screen in output.split("\n"):
    if len(str_screen) == 0:
        continue
    else:
        splitted = str_screen.split()
        name = splitted[0]
        for m in splitted[1:]:
            if re.match(re_geo, m):
                dims = m
                break
        screens.append([name, dims])
print("Found screens: ", screens)



def make_cmd(dims):
    return "." + saw_directory + "/xwinwrap/xwinwrap -g "+dims+" -ni -s -nf -b -un -ov -fdt -argb -- mpv --no-osc --no-osd-bar --quiet --screen=0 --geometry="+dims+" -wid WID --loop " + url

zombies=[]
for name, dims in screens:
    cmd = make_cmd(dims)
    print(cmd)
    zom = subprocess.Popen(["sh", saw_directory + "/single_screen.sh", dims, url])
    zombies.append(zom)
    
for death in zombies:
    death.wait()

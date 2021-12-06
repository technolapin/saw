import os
import subprocess
import sys

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
        dims = splitted[2]
        screens.append([name, dims])
print(screens)



def make_cmd(dims):
    return "./xwinwrap -g "+dims+" -ni -s -nf -b -un -ov -fdt -argb -- mpv --mute=yes --no-audio --no-osc --no-osd-bar --quiet --screen=0 --geometry="+dims+" -wid WID --loop " + url

zombies=[]
for name, dims in screens:
    cmd = make_cmd(dims)
    print(cmd)
    zom = subprocess.Popen(["sh", "single_screen.sh", dims, url])
    zombies.append(zom)
    
for death in zombies:
    death.wait()

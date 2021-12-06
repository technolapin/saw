#usage: ./single_screen.sh wxh+x+y <filename>
./xwinwrap/xwinwrap -g $1 -ni -s -nf -b -un -ov -fdt -argb -- mpv --mute=yes --no-audio --no-osc --no-osd-bar --quiet --screen=0 --geometry=$1 -wid WID --loop $2

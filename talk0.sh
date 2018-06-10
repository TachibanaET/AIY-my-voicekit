#! /bin/bash
echo $@
/home/pi/Downloads/aquestalkpi/AquesTalkPi $@ | aplay

#! /bin/bash

#This is a script to set the resolution of a linux virtual machine to  1920x1080p at 60hz.
#It is specfically for a linux virtual machine running with virtual box.
xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
xrandr --addmode Virtual1 1920x1080_60.00
xrandr --output Virtual1 --mode "1920x1080_60.00"

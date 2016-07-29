#!/bin/bash
#if synclient -l | grep "TouchpadOff .*=.*0" ; then
    #synclient TouchpadOff=1 ;
#else
    #synclient TouchpadOff=0 ;
#fi
if xinput list-props 13 | grep "Device Enabled (136):.*1" >/dev/null
then
  xinput disable 13
  notify-send -u low -i mouse "Trackpad disabled"
else
  xinput enable 13
  notify-send -u low -i mouse "Trackpad enabled"
fi

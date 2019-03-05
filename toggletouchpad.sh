#!/bin/bash
#if synclient -l | grep "TouchpadOff .*=.*0" ; then
    #synclient TouchpadOff=1 ;
#else
    #synclient TouchpadOff=0 ;
#fi
id="$(xinput | grep "Synaptics"| grep -oP 'id=([0-9]*)' | sed 's/id=//')"
if xinput list-props $id | grep "Device Enabled (153):.*1" >/dev/null
then
  xinput disable $id
  notify-send -u low -i mouse "Trackpad disabled"
else
  xinput enable $id
  notify-send -u low -i mouse "Trackpad enabled"
fi

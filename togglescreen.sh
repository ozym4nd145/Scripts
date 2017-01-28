#!/bin/bash
#if synclient -l | grep "TouchpadOff .*=.*0" ; then
    #synclient TouchpadOff=1 ;
#else
    #synclient TouchpadOff=0 ;
#fi
id="$(xinput | grep "Touchscreen"| grep -oP 'id=([0-9]*)' | sed 's/id=//')"
if xinput list-props $id | grep "Device Enabled (136):.*1" >/dev/null
then
  xinput disable $id
  notify-send -u low -i mouse "Touchscreen disabled"
else
  xinput enable $id
  notify-send -u low -i mouse "Touchscreen enabled"
fi

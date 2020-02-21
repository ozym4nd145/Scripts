#!/bin/bash
## Taken from: https://www.reddit.com/r/i3wm/comments/badmnu/start_a_new_terminal_in_the_same_directory/
filter="(bash|vi|mc)"
winpid=$(xprop -id $(xdotool getactivewindow) _NET_WM_PID|awk '{print $3}')
if [ -n "$winpid" ]; then
    lpid=$(pstree -aApT ${winpid}|grep -E  "\\-${filter},[0-9]+" -o|tail -n1|awk -F, '{print $2}')
    if [ -n "${lpid}" ]; then
        cd $(readlink /proc/${lpid}/cwd)
    fi
fi
xterm &

#!/usr/bin/env bash
set -e

tmp_dir=/tmp/scrot
save_dir=/home/$USER/Screenshots
save_arg=$1
option=$2

mkdir -p $tmp_dir
mkdir -p $save_dir

cd $tmp_dir
case "$save_arg" in
	--save|-s)
		scrot $option -e "mv \$f $save_dir/ && xclip -selection clipboard -t image/png -i $save_dir/\$n"
		;;
	--nosave|-n)
		scrot $option -e "xclip -selection clipboard -t image/png -i \$f"
		;;
	*)
		exit 2
		;;
esac
sleep 1
notify-send "Screenshot done"

exit 0

#!/bin/bash

SEPARATOR1="\n######################################################################"
SEPARATOR2="----------------------------------------------------------------------"
NAME="notes.txt"
SAVEPATH="$HOME/$NAME"
SAVEPATHTMP="/tmp/$NAME.tmp"
rm -f $SAVEPATHTMP
vim $SAVEPATHTMP
tm=$(date)
echo -e $SEPARATOR1 >> $SAVEPATH
echo $tm >> $SAVEPATH
echo -e $SEPARATOR2 >> $SAVEPATH
cat $SAVEPATHTMP >> $SAVEPATH
rm -f $SAVEPATHTMP

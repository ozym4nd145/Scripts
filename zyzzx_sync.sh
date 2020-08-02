#!/bin/bash
set -o nounset # no undeclared variable use
set -e # fail on non zero return

echo "-----------------------------------------------------"
echo "$(date)"
echo "-----------------------------------------------------"

DEST="hippocampus:/volume1/data/zyzzx/backup"
COMMAND="rsync -rluptzvP --delete --exclude '__pycache__' --exclude '*.pyc' --exclude '.git' --exclude '*.o' --exclude 'node_modules' --ignore-missing-args --max-size='100M' --filter=':- .gitignore'"

crontab -l > "${HOME}"/.crontab.bak
declare -a dotPaths=(".bashrc" ".vimrc" ".tmux.conf" ".config" ".gitconfig" ".dircolors" ".dmenurc" ".dmrc" ".fzf" ".i3" ".urxvt" ".wpmrc" ".wpm.csv" ".Xauthority" ".xinitrc" ".Xresources" ".gnupg" ".bash_eternal_history" ".bash_history" ".profile" ".ssh" ".vim" ".crontab.bak" ".emacs.d" ".doom.d")
declare -a homePaths=("bin" "man" "colorschemes" "notes.txt" "Tower" "org" "secret")
declare -a otherPaths=("/data")

fullDotPaths=("${dotPaths[@]/#/${HOME}/}")
fullHomePaths=("${homePaths[@]/#/${HOME}/}")

eval ${COMMAND} "${fullDotPaths[@]}" "${DEST}/dotFiles/"
eval ${COMMAND} "${fullHomePaths[@]}" "${DEST}/homeFiles/"
eval ${COMMAND} "${otherPaths[@]}" "${DEST}/otherFiles/"

echo -e "-----------------------------------------------------\n"

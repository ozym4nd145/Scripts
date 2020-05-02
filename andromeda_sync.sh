#!/bin/bash
set -o nounset # no undeclared variable use
set -e # fail on non zero return

echo "-----------------------------------------------------"
echo "$(date)"
echo "-----------------------------------------------------"

DEST="/data/andromeda"
COMMAND="rsync -rluptzzvP --delete --exclude '__pycache__' --exclude '*.pyc' --exclude '.git' --exclude '*.o' --exclude 'node_modules' --ignore-missing-args --max-size='100M' --filter=':- .gitignore'"

crontab -l > "${HOME}"/.crontab.bak
declare -a dotPaths=(".bashrc" ".vimrc" ".tmux.conf" ".config" ".gitconfig" ".dircolors" ".fzf" ".fzf.bash" ".gnupg" ".bash_eternal_history" ".bash_history" ".profile" ".ssh" ".vim" ".crontab.bak")
declare -a homePaths=("bin" "man" "logs" "secrets" "docker-services")
declare -a otherPaths=()

fullDotPaths=("${dotPaths[@]/#/${HOME}/}")
fullHomePaths=("${homePaths[@]/#/${HOME}/}")

eval ${COMMAND} "${fullDotPaths[@]}" "${DEST}/dotFiles/"
eval ${COMMAND} "${fullHomePaths[@]}" "${DEST}/homeFiles/"
eval ${COMMAND} "${otherPaths[@]}" "${DEST}/otherFiles/"

echo -e "-----------------------------------------------------\n"

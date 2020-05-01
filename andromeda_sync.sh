#!/bin/bash
set -o nounset # no undeclared variable use
set -e # fail on non zero return

DEST="/data/andromeda"
COMMAND="rsync -avz"

crontab -l > "${HOME}"/.crontab.bak
declare -a dotPaths=(".bashrc" ".vimrc" ".tmux.conf" ".config" ".gitconfig" ".dircolors" ".fzf" ".fzf.bash" ".gnupg" ".bash_eternal_history" ".bash_history" ".profile" ".ssh" ".vim" ".crontab.bak")
declare -a homePaths=("bin" "man" "letsencrypt")
declare -a otherPaths=()

for p in "${dotPaths[@]}"; do
  eval ${COMMAND} ${HOME}/${p} ${DEST}/dotFiles/
done
for p in "${homePaths[@]}"; do
  eval ${COMMAND} ${HOME}/${p} ${DEST}/homeFiles/
done
for p in "${otherPaths[@]}"; do
  eval ${COMMAND} ${p} ${DEST}/otherFiles/
done

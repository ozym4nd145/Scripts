#!/bin/bash
set -o nounset # no undeclared variable use
set -e # fail on non zero return

echo "-----------------------------------------------------"
echo "$(date)"
echo "-----------------------------------------------------"

export PATH=${PATH}:${HOME}/bin

declare -a DIRS=("/data/andromeda" "/data/opal" "/data/bismuth" "/data/zyzzx")
for d in "${DIRS[@]}"; do
  pushd ${d}
  echo "Backing up ${d}"
  duplicacy backup -storage google -threads 2 -stats
  duplicacy backup -storage oz-google-dummy -threads 2 -stats
  duplicacy copy -from google -to oz-google -threads 2
  popd
  echo "Backing done for ${d}"
done

echo -e "-----------------------------------------------------\n"

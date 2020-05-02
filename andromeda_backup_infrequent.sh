#!/bin/bash
set -o nounset # no undeclared variable use
set -e # fail on non zero return

echo "-----------------------------------------------------"
echo "$(date)"
echo "-----------------------------------------------------"

export PATH=${PATH}:${HOME}/bin

declare -a DIRS=("/data/share")
for d in "${DIRS[@]}"; do
  pushd ${d}
  echo "Backing up ${d}"
  duplicacy backup -storage google -threads 2 -stats
  popd
  echo "Backing done for ${d}"
done

echo -e "-----------------------------------------------------\n"

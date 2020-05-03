#!/bin/bash
set -o nounset # no undeclared variable use
set -e # fail on non zero return

echo "-----------------------------------------------------"
echo "$(date)"
echo "-----------------------------------------------------"

export PATH=${PATH}:${HOME}/bin
THREADS=30

declare -a DIRS=("/data/share")
echo "### Backup Start ###"
for d in "${DIRS[@]}"; do
  pushd ${d}
  echo "Backing up ${d}"
  duplicacy backup -storage google -threads "${THREADS}" -stats
  popd
  echo "Backing done for ${d}"
done
echo "### Backup End ###"

echo "### Check Start ###"
pushd "${DIRS[0]}"
duplicacy -log check -storage google -all -threads "${THREADS}" -fossils -resurrect
popd
echo "### Check End ###"

echo -e "-----------------------------------------------------\n"

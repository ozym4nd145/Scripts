#!/bin/bash
set -o nounset # no undeclared variable use
set -e # fail on non zero return

echo "-----------------------------------------------------"
echo "$(date)"
echo "-----------------------------------------------------"

export PATH=${PATH}:${HOME}/bin
DIR="/data/andromeda"
THREADS=30

if [ $(pgrep -x duplicacy) -eq 0 ]; then
  echo "Another instance of duplicacy is running!"
  exit 1
else
  echo "No other instance is running okay to prune"
fi

echo "### Prune Start ###"
pushd "${DIR}"
duplicacy prune -storage google -keep 0:1080 -keep 120:360 -keep 30:180 -keep 7:30 -keep 1:7 -all -threads "${THREADS}"
duplicacy prune -storage backblaze -keep 0:1080 -keep 120:360 -keep 30:180 -keep 7:30 -keep 1:7 -all -threads "${THREADS}"
popd
echo "### Pruning End ###"

echo -e "-----------------------------------------------------\n"

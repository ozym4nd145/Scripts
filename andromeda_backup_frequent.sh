#!/bin/bash
set -o nounset # no undeclared variable use
set -e # fail on non zero return
export PATH=${PATH}:${HOME}/bin

LOG_DIR="${HOME}"/logs/backup/frequent
LOG_FILE="${LOG_DIR}"/$(date +"%Y%m%d-%H%M%S").log
mkdir -p ${LOG_DIR}

declare -a DIRS=("/data/andromeda" "/data/opal" "/data/bismuth" "/data/zyzzx")
for d in "${DIRS[@]}"; do
  pushd ${d}
  echo "Backing up ${d}" >> ${LOG_FILE} 2>&1
  duplicacy backup -storage google -threads 2 -stats >> ${LOG_FILE} 2>&1
  duplicacy backup -storage oz-google-dummy -threads 2 -stats >> ${LOG_FILE} 2>&1
  duplicacy copy -from google -to oz-google -threads 2 >> ${LOG_FILE} 2>&1
  popd
  echo "Backing done for ${d}" >> ${LOG_FILE} 2>&1
done

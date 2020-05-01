#!/bin/bash
set -o nounset # no undeclared variable use
set -e # fail on non zero return
export PATH=${PATH}:${HOME}/bin

LOG_DIR="${HOME}"/logs/backup/infrequent
LOG_FILE="${LOG_DIR}"/$(date +"%Y%m%d-%H%M%S").log
mkdir -p ${LOG_DIR}

declare -a DIRS=("/data/share")
for d in "${DIRS[@]}"; do
  pushd ${d}
  echo "Backing up ${d}" >> ${LOG_FILE} 2>&1
  duplicacy backup -storage google -threads 2 -stats >> ${LOG_FILE} 2>&1
  popd
  echo "Backing done for ${d}" >> ${LOG_FILE} 2>&1
done

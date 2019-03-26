#!/bin/bash
set -e

# Log Location on Server.
LOG_LOCATION=${HOME}/logs
exec > >(tee -ai $LOG_LOCATION/syncKeePass.log)
exec 2>&1

SEPARATOR1="\n######################################################################"
SEPARATOR2="----------------------------------------------------------------------"


LOCALDB_PATH="${HOME}/500GB/KeePassDB/"
REMOTEDB_PATH="${HOME}/500GB/DriveSync/KeePassDB/"
REMOTE_URL="GDrive-suyash1212:/KeePassDB/"

DB_NAME="DB.kdbx"
TIME=`/bin/date +%Y-%m-%d-%H-%M-%S`

# print separators
echo -e $SEPARATOR1
echo $(date)
echo -e $SEPARATOR2

# Get remote data
rclone sync -v ${REMOTE_URL} ${REMOTEDB_PATH}

# Backup local db
cp ${LOCALDB_PATH}${DB_NAME} ${LOCALDB_PATH}${TIME}-${DB_NAME}

# Merge local and remote db
# Read Password
echo -n Password:
read -s password
echo ${password} | keepassxc-cli merge -s ${LOCALDB_PATH}${DB_NAME} ${REMOTEDB_PATH}${DB_NAME}

# Backup remote db
cp ${REMOTEDB_PATH}${DB_NAME} ${REMOTEDB_PATH}${TIME}-${DB_NAME}

# copy merged db to remote
cp ${LOCALDB_PATH}${DB_NAME} ${REMOTEDB_PATH}${DB_NAME}

# Get remote data
rclone sync -v ${REMOTEDB_PATH} ${REMOTE_URL}

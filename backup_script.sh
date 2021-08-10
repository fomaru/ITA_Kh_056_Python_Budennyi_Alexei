#!/usr/bin/env bash

help_message="Source directory and destination for archive and log file required"

LOGFILE="/home/alex/backups/rsync-backup-log-$(date +"%Y-%m-%d").log"
source=$1
destination=$2

rsync --delete --info=COPY2,DEL2,NAME2,BACKUP2,REMOVE2,SKIP2 -a $source $destination > $LOGFILE

# while read line; do
#   a=$(awk '{print $2}' $line)
#   echo $a
#   if [ -z $(awk '{print $2}' $line)]
#   then
#       echo $line
#   fi
# done > $LOGFILE

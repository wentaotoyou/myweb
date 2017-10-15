#!/usr/bin/env bash

SHELL_NAME="update_web"
#SHELL_DIR="/data/updates/scripts/rundeck/web"
SHELL_LOG="${SHELL_DIR}/${SHELL_NAME}.log"
#LOCK_FILE="/tmp/${SHELL_NAME}.lock"

#Write Log
function logger(){
    LOG_INFO=$1
    echo -e "$(date "+%Y%m%d %H:%M:%S"): ${LOG_INFO}"
    echo -e "$(date "+%Y%m%d %H:%M:%S"): ${LOG_INFO}" >> ${SHELL_LOG}
}

 Shell Usage
function shell_usage(){
    echo $"Usage: $0 eshop-app /data/project/web/eshop-server/eshop-app/target/eshop-app /data"
}

if [ $# -ne 3 ]; then
    shell_usage
    exit 1
fi

app=$1
src_dir=$2
filelist=$3

for file in $filelist
do
#    cp -rp --parent $file $src_dir/$file pkgs_dir/$app/
    echo $file
done
#rsync -avzp pkgs_dir/$app 192.168.1.222:/data/web/$app
#if [ isreboot = 0 ];then
#    ssh 192.168.1.222 tomcat reboot $app
#fi
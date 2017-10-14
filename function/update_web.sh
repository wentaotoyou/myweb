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

# Shell Usage
#function shell_usage(){
#    echo $"Usage: $0 eshop-app /data/project/web/eshop-server/eshop-app/target/eshop-app "
#}
#
#if [ $# -ne 2 ]; then
#    shell_usage
#    exit 1
#fi

APP=$1
src_dir=$2
filelist=$3

for file in $filelist
do
#    cp -rp --parent $file $src_dir/$file pkgs_dir/$APP/
    echo $file
done
#if [ -z "$APP" -o ! -z "$src_dir" ];then
#    echo "Null parameter or $APP configuration files does not exist"
#    exit 1
#fi

#if [ -z "$src_dir" -0 -d "$src_dir" ];then
#    echo "Null parameter or $src_dir does not exist"
#fi

#rsync -avzp pkgs_dir/$APP 192.168.1.222:/data/web/$APP
#if [ isreboot = 0 ];then
#    ssh 192.168.1.222 tomcat reboot $APP
#fi
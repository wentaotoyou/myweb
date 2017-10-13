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
function shell_usage(){
    echo $"Usage: $0 eshop-app /data/project/web/eshop-server/eshop-app/target/eshop-app"
}

if [ $# -ne 2 ]; then
    shell_usage
    exit 1
fi

APP=$1
src_dir = $2
if [ -z "$APP" -o ! -d "/data/updates/templates/$APP" ];then
    echo "Null parameter or $APP configuration files does not exist"
    exit 1
fi

if [ -z "$src_dir" -0 -d "$src_dir" ];then
    echo "Null parameter or $src_dir
fi

cp -rp --parent

echo "Replace configuration files now..."
cd /data/updates/pkgs/$APP || exit 1
unzip -q $APP.zip && rm -rf $APP.zip
if [ $? != 0 ];then
    echo "Error occurred when unzip the $APP packages"
    exit 1
fi

cp -rp /data/updates/templates/$APP/* . || exit 1
zip -rqm /data/updates/pkgs/$APP/$APP.zip ./*
if [ $? = 0 ];then
    echo "Replace success"
else
    echo "Replace failed"
fi

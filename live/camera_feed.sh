#! /bin/bash

local_or_remote=$1
local_machine=$2
remote_machine_config=$3
port=$4

pi_name="pi"

command="/opt/vc/bin/raspivid -t 0 -w 600 -h 600 -hf -fps 20 -o - | nc $local_machine $port"

# Need to run in separate proc
function nc_listen_pycam() {
    nc -l $port | mplayer -fps 20 -demuxer h264es -
}

function run_over_ssh() {
    ssh $remote_machine_config -t $command
}

function nope() {
    echo "Invalid usage - use ./camera_feed local|remote local_machine remote_machine port"
    echo $1
    exit
}

if [ "$local_or_remote" == "" ]
then
    nope "Need local|remote"
fi



if [ "$local_or_remote" = "local" ]
then
    port=$2
    if [ "$port" == "" ]
    then
        nope "Need port"
    fi
    nc_listen_pycam
    exit
fi

if [ "$local_or_remote" = "remote" ]
then
    if [ "$local_machine" == "" ]
    then
        nope "Need local machine"
    elif [ "$remote_machine_config" == "" ]
    then
        nope "Need remote machine"
    fi
    run_over_ssh
else
    nope "Invalid local|remote"
fi
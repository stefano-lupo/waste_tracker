#! /bin/bash

pi_ip="192.168.1.6"
pi_dir="/home/pi/waste_tracker"
scp -r . pi@$pi_ip:$pi_dir
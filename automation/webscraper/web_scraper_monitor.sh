#!/bin/bash

function main
{
	echo "`date +"%Y-%m-%d %H:%M:%S"` ====================="
	echo "`date +"%Y-%m-%d %H:%M:%S"` ==== Adding to master" 
	echo "`date +"%Y-%m-%d %H:%M:%S"` ====================="
	git pull origin master >> /opt/monitor.log 2>&1 
	check_err="$?"
	if [ $check_err -ne "0" ]
	then
		echo "`date +"%Y-%m-%d %H:%M:%S"` ====================="
		echo "`date +"%Y-%m-%d %H:%M:%S"` ==== Failed Update" 
		echo "`date +"%Y-%m-%d %H:%M:%S"` ====================="
		exit 1
	else 
		echo "`date +"%Y-%m-%d %H:%M:%S"` ====================="
		echo "`date +"%Y-%m-%d %H:%M:%S"` ==== Succeeded Update" 
		echo "`date +"%Y-%m-%d %H:%M:%S"` ====================="
		return 0
	fi	
}

main 
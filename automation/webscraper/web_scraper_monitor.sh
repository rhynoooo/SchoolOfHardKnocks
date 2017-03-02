#!/bin/bash

function main
{
	echo "`date +"%Y-%m-%d %H:%M:%S"` ==== Adding to master" 
	git pull origin master 
	check_err="$?"
	if [ $check_err -ne "0" ]
	then
		echo "`date +"%Y-%m-%d %H:%M:%S"` ==== error occurred, exiting"
		exit 1
	else 
		echo "`date +"%Y-%m-%d %H:%M:%S"` ==== succeeded in updating..."
		return 0
	fi	
}

main 
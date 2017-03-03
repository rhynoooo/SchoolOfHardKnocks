#!/bin/bash

function main
{
	echo "`date +"%Y-%m-%d %H:%M:%S"` ====================="
	echo "`date +"%Y-%m-%d %H:%M:%S"` ==== Adding to master" 
	echo "`date +"%Y-%m-%d %H:%M:%S"` ====================="
	cd /opt/webscraper/automation/webscraper >> /opt/monitor.log 2>&1 
	git pull origin master >> /opt/monitor.log 2>&1 
	check_err="$?"
	if [ $check_err -ne "0" ]
	then
		echo "`date +"%Y-%m-%d %H:%M:%S"` ====================="
		echo "`date +"%Y-%m-%d %H:%M:%S"` ==== Failed Update" 
		echo "`date +"%Y-%m-%d %H:%M:%S"` 
		aws sns publish --topic-arn arn:aws:sns:us-east-1:384526644452:Fuck --region us-east-1 --subject "Code deployed failed." --message "Please check code deployment"">> /opt/monitor.log 2>&1
		exit 1
	else 
		echo "`date +"%Y-%m-%d %H:%M:%S"` ====================="
		echo "`date +"%Y-%m-%d %H:%M:%S"` ==== Succeeded Update" 
		echo "`date +"%Y-%m-%d %H:%M:%S"` ====================="
		return 0
	fi	
}

main 
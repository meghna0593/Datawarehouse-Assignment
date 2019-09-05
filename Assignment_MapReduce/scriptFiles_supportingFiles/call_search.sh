#!/bin/bash

case $1 in
	'start') #start the search service
		while [ True ]
		do
			`twurl "/1.1/search/tweets.json?q=halifax&result_type=mixed" >> halifax_raw_search.json`
	        	sleep 2h
		done
		;;
	'stop') #stop the search service
		kill -9 $(ps -ef | grep -w '[c]all_search.sh' | awk '{print $2}') 
		;;
	*)
		echo "Please enter start/stop"
		;;
esac	

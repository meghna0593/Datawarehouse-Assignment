#!/bin/bash

case $1 in
	'start') #start the stream service
		while [ True ]
		do
			`python get_tweets_search.py >> halifax_raw_stream.json`
		done
		;;
	'stop') #stop the stream service
		kill -9 $(ps -ef | grep -w '[c]all_stream.sh' | awk '{print $2}') 
		;;
	*)
		echo "Please enter start/stop"
		;;
esac	

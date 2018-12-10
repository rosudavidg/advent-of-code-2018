#!/bin/bash

INPUT_FILE="input.txt"
BAD_MESSAGE="Usage: ./run [1 | 2]"

run() {
	echo "[Running part" $1"...]"
	python3.6 part-$1.py < $INPUT_FILE	
	echo "[Done]"
}

if [ $# -eq 1 ] ; then
	if [ $1 -eq 1 ] ; then
		run 1
	elif [ $1 -eq 2 ] ; then
		run 2
	else
		echo $BAD_MESSAGE
	fi
elif [ $# -gt 1 ] ; then
	echo $BAD_MESSAGE
else
	run 1
	run 2
fi

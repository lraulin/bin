#!/bin/bash

option = $1

if [ $option = '-on' ]
then

    echo "Stopping Crashplan..."
    sudo service crashplan stop
    echo "Crashplan deactivated."

    echo "Stopping other applications..."
    sudo killall dropbox
    sudo killall qtorrent
    sudo killall transmission
    sudo killall transmission-gtk
    sudo killall ktorrent
    sudo killall *torrent*
    echo "Done."

    echo "Hotspot mode engaged."
    
elif [ $option = '-off' ]
then
    echo "Starting Crashplan service..."
    sudo service crashplan start
    echo "Done."
    echo "Hotspot mode disengaged."
    echo "System normal."
    
else
    "Option required: -on or -off."
fi

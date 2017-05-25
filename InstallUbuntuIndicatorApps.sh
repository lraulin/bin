#!/bin/bash
# Install indicator applets in Ubuntu 14.04

echo "Adding PPAs..."
sudo add-apt-repository ppa:atareao/atareao
#For Synapse search tool...unnecessary if you like using the Unity dash.
#sudo add-apt-repository ppa:elementary-os/daily
#sudo add-apt-repository ppa:elementary-os/unstable-upstream
sudo add-apt-repository ppa:jconti/recent-notifications
sudo add-apt-repository ppa:tsbarnes/indicator-keylock

echo "Updating package lists..."
update

echo "Installing apps..."
sudo apt-get install my-weather-indicator -y
sudo apt-get install indicator-cpufreq -y
sudo apt-get install indicator-multiload -y
#For Synapse search tool...unnecessary if you like using the Unity dash.
#sudo apt-get install indicator-synapse -y
sudo apt-get install indicator-notifications -y
sudo apt-get install diodon diodon-plugins -y
sudo apt-get install indicator-keylock -y
sudo apt-get install touchpad-indicator -y

echo "Done!"

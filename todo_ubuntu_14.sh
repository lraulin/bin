#!/bin/sh
#http://www.webupd8.org/2014/04/10-things-to-do-after-installing-ubuntu.html


#sudo add-apt-repository ppa:nilarimogard/webupd8
sudo add-apt-repository ppa:atareao/atareao
sudo add-apt-repository ppa:peterlevi/ppa
sudo add-apt-repository ppa:mc3man/trusty-media
#sudo add-apt-repository ppa:linrunner/tlp

sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade

#sudo apt-get install pidgin-indicator
sudo apt-get install calendar-indicator
sudo apt-get install my-weather-indicator
sudo apt-get install variety
sudo apt-get install indicator-cpufreq
sudo apt-get install unity-tweak-tool
sudo apt-get install compizconfig-settings-manager
sudo apt-get install libreoffice-style-sifr
#sudo apt-get install tlp tlp-rdw
#sudo tlp start

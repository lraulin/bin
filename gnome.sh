#!/bin/bash

sudo apt-get update
sudo apt-get dist-upgrade -y
sudo apt-get install gnome-shell
sudo add-apt-repository ppa:gnome3-team/gnome3-staging -y
sudo apt-get dist-upgrade -y
sudo apt-get install epiphany-browser gnome-maps polari -y

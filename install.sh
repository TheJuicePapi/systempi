#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

# Install required packages (adjust based on your needs)
apt-get update
apt-get install -y python3 python3-pip

# Install Python dependencies
pip3 install psutil

# Create symbolic link for systempi.py
ln -s "$(pwd)/systempi.py" /usr/local/bin/systempi

clear

echo "Installation complete and shortcut created! Launch a new terminal and you'll be able to run 'systempi' from any directory!"

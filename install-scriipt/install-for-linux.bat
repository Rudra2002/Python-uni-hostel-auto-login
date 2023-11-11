#!/bin/bash

# Task 1: Install Chromium Browser
echo "Installing Chromium Browser..."
sudo apt install -y chromium-browser

# Task 2: Install Chromium Chromedriver
echo "Installing Chromium Chromedriver..."
sudo apt install -y chromium-chromedriver

# Task 3: Copy login.py to ~/.local/bin
echo "Copying login.py to ~/.local/bin..."
cp ../source/login.py ~/.local/bin

echo "Script completed successfully."

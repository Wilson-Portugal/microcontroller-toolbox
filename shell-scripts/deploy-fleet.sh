#!/bin/bash
# shell-scripts/deploy-fleet.sh
# Automates pushing toolbox scripts from Guarda to local microcontrollers

TARGET_IP=$1
TARGET_TYPE=$2  # e.g., 'rp2040' or 'esp32'

if [ -z "$TARGET_IP" ]; then
    echo "Usage: ./deploy-fleet.sh <device-ip-or-hostname> [device-type]"
    echo "Example: ./deploy-fleet.sh 192.168.1.50 esp32"
    exit 1
fi

echo "=================================================="
echo "Deploying Microcontroller Toolbox to $TARGET_IP"
echo "=================================================="

# Check if mpremote or ampy is installed for flashing microcontrollers over network/serial
# Or if this is copying a script to another Pi server via SCP
if [ "$TARGET_TYPE" == "server" ]; then
    echo "Copying toolbox to remote linux server..."
    scp -r /home/coelho/microcontroller-toolbox/coelho@$TARGET_IP:/home/coelho/
else
    echo "Preparing to flash MicroPython board at $TARGET_IP..."
    # Note: You can incorporate your specific ampy/mpremote network commands here
fi

echo "Deployment cycle finished for $TARGET_IP."

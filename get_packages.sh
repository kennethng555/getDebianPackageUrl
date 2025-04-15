#!/bin/bash

set -e  # Exit on any error
set -o pipefail  # Fail if any part of the pipeline fails

# Ensure the script is run as root or with sudo
if [[ "$EUID" -ne 0 ]]; then
    echo "Please run this script as root or with sudo"
    exit 1
fi

echo "Starting to download package dependencies..."

# Download dependencies for build-essential, excluding libc-dev and debconf-2.0
apt-get download $(apt-rdepends build-essential \
    | grep -v "^ " \
    | grep -v "^libc-dev$" \
    | grep -v "^debconf-2.0$")

# Download dependencies for gcc-arm-linux-gnueabihf
apt-get download $(apt-rdepends gcc-arm-linux-gnueabihf \
    | grep -v "^ ")

# Download dependencies for python3-pyelftools
apt-get download $(apt-rdepends python3-pyelftools \
    | grep -v "^ ")

# Download dependencies for device-tree-compiler
apt-get download $(apt-rdepends device-tree-compiler \
    | grep -v "^ ")

# Download dependencies for pkg-config
apt-get download $(apt-rdepends pkg-config \
    | grep -v "^ ")

# Download dependencies for uuid-dev, excluding libc-dev and debconf-2.0
apt-get download $(apt-rdepends uuid-dev \
    | grep -v "^ " \
    | grep -v "^libc-dev$" \
    | grep -v "^debconf-2.0$")

echo "All downloads completed successfully."


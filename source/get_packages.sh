#!/bin/bash

set -e  # Exit on any error
set -o pipefail  # Fail if any part of the pipeline fails

# Ensure the script is run as root or with sudo
if [[ "$EUID" -ne 0 ]]; then
    echo "Please run this script as root or with sudo"
    exit 1
fi

# Check if at least one package name was provided
if [[ "$#" -eq 0 ]]; then
    echo "Usage: $0 <package1> [package2 ...]"
    exit 1
fi

echo "Starting to download package dependencies for: $@"

# List of packages to exclude
EXCLUDE_LIST=(
    "libc-dev"
    "debconf-2.0"
    "dbus-system-bus"
    "default-dbus-system-bus"
    "mime-support"
    "systemd-sysusers"
    "libc6"
    "libglib2.0-0"
    "libcurl3"
    "dbus-session-bus"
    "default-dbus-session-bus"
    "gsettings-backend"
)

# Build regex pattern for grep -E (e.g. ^pkg1$|^pkg2$|...)
EXCLUDE_PATTERNS=$(printf "^%s$|" "${EXCLUDE_LIST[@]}")
# Remove trailing '|'
EXCLUDE_PATTERNS="${EXCLUDE_PATTERNS%|}"

for pkg in "$@"; do
    echo "Processing package: $pkg"

    # Download dependencies excluding the ones matching EXCLUDE_PATTERNS
    apt-get download $(
        apt-rdepends "$pkg" \
        | grep -v "^ " \
        | grep -Ev "$EXCLUDE_PATTERNS"
    )
done

echo "All downloads completed successfully."

# sudo ../debian/get_packages.sh build-essential gcc-arm-linux-gnueabihf python3-pyelftools device-tree-compiler pkg-config uuid-dev
# sudo ../debian/get_packages.sh dislocker cryptsetup libcryptsetup-dev libcryptsetup12 cryptmount cryptmount overlayroot qemu-user-static
# sudo ../debian/get_packages.sh abootimg binfmt-support binutils cpp device-tree-compiler dosfstools lbzip2 libxml2-utils  nfs-kernel-server python3-yaml qemu-user-static sshpass udev uuid-runtime whois openssl cpio
# sudo ../debian/get_packages.sh fonts-lato javascript-common libjs-jquery libnss-systemd libpam-modules libpam-systemd ruby-rubygems ruby3.0 rubygems-integration systemd systemd-sysv systemd-timesyncd udev
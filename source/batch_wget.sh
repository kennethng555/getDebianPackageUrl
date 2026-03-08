#!/bin/bash

# Check if the user provided a filename
if [ -z "$1" ]; then
  echo "Usage: $0 <file_with_urls>"
  exit 1
fi

# Read each line (URL) from the file and run wget if the file doesn't exist
while IFS= read -r url; do
  # Skip empty lines or lines starting with #
  [[ -z "$url" || "$url" =~ ^# ]] && continue

  # Extract the filename from the URL
  filename=$(basename "$url")

  # Check if the file already exists
  if [[ -f "$filename" ]]; then
    echo "File already exists: $filename — skipping download."
  else
    echo "Downloading: $url"
    wget "$url"
  fi
done < "$1"

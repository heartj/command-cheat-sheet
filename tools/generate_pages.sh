#!/bin/bash

# Script to generate Markdown pages for Command Cheat Sheet
# Prompts for YAML data file and runs tools/generate_pages.py
# Output is saved to out/<yaml_filename>/

set -e  # Exit on error

# Prompt for YAML data file
echo "Enter the path to the YAML data file (e.g., data/linux_system.yaml):"
read -r yaml_file

# Check if YAML file exists
if [ ! -f "$yaml_file" ]; then
    echo "Error: YAML file '$yaml_file' not found."
    exit 1
fi

# Extract filename without path and extension (e.g., linux_system from data/linux_system.yaml)
filename=$(basename "$yaml_file" .yaml)

# Set output directory (e.g., out/linux_system)
output_dir="out/$filename"

# Ensure out/ directory exists
mkdir -p "$(dirname "$output_dir")"

# Run generate_pages.py
echo "Generating pages to $output_dir..."
python3 ./generate_pages.py \
    --data-file "$yaml_file" \
    --template-dir ../templates \
    --output-dir "$output_dir"

echo "Generation complete. Check $output_dir for Markdown files."
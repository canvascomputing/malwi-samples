#!/usr/bin/env bash

# Check for correct usage
# The script expects two arguments:
# 1. The exact number of files a project folder must contain
# 2. The directory to move matching project folders into
if [ $# -ne 2 ]; then
    echo "Usage: $0 <number_of_files> <target_directory>"
    exit 1
fi

# Read input arguments
TARGET_COUNT=$1         # Number of files to match
TARGET_DIR=$2           # Target directory to move folders to

# Create the target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Loop over all folders under triage/data*/ (e.g., triage/data10, triage/data123, etc.)
for data_dir in triage/data*/; do
    # Loop over all project subfolders inside each data folder
    for project_dir in "$data_dir"*/; do
        if [ -d "$project_dir" ]; then
            # Count the number of files (not directories) in the project folder
            file_count=$(find "$project_dir" -type f | wc -l)

            # If the number of files matches the target, move the folder
            if [ "$file_count" -eq "$TARGET_COUNT" ]; then
                echo "Moving $project_dir (file count: $file_count)"
                mv "$project_dir" "$TARGET_DIR/"
            fi
        fi
    done
done

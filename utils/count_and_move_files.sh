#!/usr/bin/env bash

# Usage info
if [ $# -lt 2 ] || [ $# -gt 3 ]; then
    echo "Usage: $0 <number_of_files> <target_directory> [source_directory]"
    exit 1
fi

# Arguments
TARGET_COUNT=$1
TARGET_DIR=$2
SOURCE_GLOB=${3:-triage/data*/}  # Default to 'triage/data*/' if not provided

# Create the target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Loop over all folders under the given source glob
for data_dir in $SOURCE_GLOB; do
    # Ensure it's a directory
    [ -d "$data_dir" ] || continue

    # Loop over project subfolders
    for project_dir in "$data_dir"*/; do
        if [ -d "$project_dir" ]; then
            # Count regular files
            file_count=$(find "$project_dir" -type f | wc -l)

            # Move if file count matches
            if [ "$file_count" -eq "$TARGET_COUNT" ]; then
                echo "Moving $project_dir (file count: $file_count)"
                mv "$project_dir" "$TARGET_DIR/"
            fi
        fi
    done
done

#!/usr/bin/env bash
set -euo pipefail

root_dir="malware-samples"

# Iterate over all data* folders (e.g. data1, data2, ...)
for data_dir in "$root_dir"/data*; do
    echo "Processing $data_dir..."
    
    # Step 1: Move data/*/pkg/version/ → data/pkg_version/
    find "$data_dir" -mindepth 2 -maxdepth 2 -type d | while read -r pkg_version_dir; do
        # Check if directory still exists (may have been moved/deleted)
        if [ ! -d "$pkg_version_dir" ]; then
            continue
        fi
        
        parent_dir=$(dirname "$pkg_version_dir")
        pkg_name=$(basename "$parent_dir")
        version=$(basename "$pkg_version_dir")
        new_dir="$data_dir/${pkg_name}_${version}"
        
        if [ "$pkg_version_dir" = "$new_dir" ]; then
            continue
        fi
        
        echo "Moving $pkg_version_dir -> $new_dir"
        mv "$pkg_version_dir" "$new_dir"
        rmdir "$parent_dir" 2>/dev/null || true
    done
    
    # Step 2: Flatten nested folders recursively, even if names differ
    find "$data_dir" -mindepth 1 -maxdepth 1 -type d | while read -r pkg_dir; do
        # Check if directory still exists
        if [ ! -d "$pkg_dir" ]; then
            continue
        fi
        
        echo "Flattening all nested content in $(basename "$pkg_dir")"
        
        # Keep flattening until no more nested directories can be flattened
        changed=true
        while [ "$changed" = true ]; do
            changed=false
            
            # Re-check if directory still exists in the loop
            if [ ! -d "$pkg_dir" ]; then
                break
            fi
            
            # Find all subdirectories at any depth
            find "$pkg_dir" -mindepth 2 -type d 2>/dev/null | while read -r nested_dir; do
                if [ ! -d "$nested_dir" ]; then
                    continue
                fi
                
                # Check if this nested directory contains only files (no subdirectories)
                subdir_count=$(find "$nested_dir" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l)
                
                if [ "$subdir_count" -eq 0 ]; then
                    # This is a leaf directory (contains only files), move its contents up
                    echo "  Moving contents from nested directory: $(basename "$nested_dir")"
                    
                    # Move all files from nested directory to the main package directory
                    find "$nested_dir" -mindepth 1 -maxdepth 1 -type f 2>/dev/null -exec mv {} "$pkg_dir/" \; 2>/dev/null || true
                    
                    # Remove the now-empty nested directory
                    rmdir "$nested_dir" 2>/dev/null || true
                fi
            done
            
            # Check if we still have any nested directories - if so, continue
            nested_count=$(find "$pkg_dir" -mindepth 2 -type d 2>/dev/null | wc -l)
            if [ "$nested_count" -gt 0 ]; then
                changed=true
            fi
            
            # Also handle the case where there's exactly one subdirectory at the top level
            # and it should be flattened
            top_subdirs=$(find "$pkg_dir" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l)
            top_files=$(find "$pkg_dir" -mindepth 1 -maxdepth 1 -type f 2>/dev/null | wc -l)
            
            if [ "$top_subdirs" -eq 1 ] && [ "$top_files" -eq 0 ]; then
                subdir=$(find "$pkg_dir" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | head -n1)
                
                if [ -n "$subdir" ] && [ -d "$subdir" ]; then
                    echo "  Flattening single top-level subdirectory: $(basename "$subdir")"
                    
                    # Move all contents from the subdirectory to the parent
                    find "$subdir" -mindepth 1 2>/dev/null -exec mv {} "$pkg_dir/" \; 2>/dev/null || true
                    
                    # Remove the now-empty subdirectory
                    if rmdir "$subdir" 2>/dev/null; then
                        changed=true
                    fi
                fi
            fi
        done
    done
    
    # Step 3: Remove any empty directories
    find "$data_dir" -type d -empty -delete
done

echo "✅ Done."
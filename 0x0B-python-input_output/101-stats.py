#!/bin/bash

# Initialize variables
total_size=0
declare -A status_counts

# Function to print statistics
print_statistics() {
    echo "Total file size: File size: $total_size"
    for code in 200 301 400 401 403 404 405 500; do
        count=${status_counts[$code]}
        if [ -n "$count" ]; then
            echo "$code: $count"
        fi
    done
}

# Trap Ctrl+C to print statistics
trap 'print_statistics' INT

# Read input line by line
while read -r line; do
    # Extract file size and status code
    file_size=$(echo "$line" | awk '{print $NF}')
    status_code=$(echo "$line" | awk '{print $(NF-1)}')

    # Update total size
    total_size=$((total_size + file_size))

    # Update status code count
    ((status_counts[$status_code]++))

    # Print statistics every 10 lines
    if ((++line_count % 10 == 0)); then
        print_statistics
    fi
done

# Print final statistics
print_statistics


#!/bin/bash

python_script="/home/amir/Desktop/PULSARS/program.py"
data_directory="/home/amir/Desktop/PULSARS/Data/"

if [ ! -f "$python_script" ]; then
    echo "Error: Python script not found at $python_script"
    exit 1
fi

if [ ! -d "$data_directory" ]; then
    echo "Error: Data directory not found at $data_directory"
    exit 1
fi

for file in "$data_directory"/*
do
    if [ -f "$file" ]; then
        echo "Running $python_script with input file: $file..."
        python3 "$python_script" "$file"
        echo "-----------------------------------------"
    fi
done


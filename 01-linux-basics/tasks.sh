#!/bin/bash
# ========================================================
# Linux Basics - Lab Assignment
# Name: Prajakta Chavan
# Repository : https://github.com/PrajaktaChavan/Devops-assignments
# ========================================================

# Task 1: Creating and Renaming Files/Directories
echo "=== Task 1: Creating and Renaming Files/Directories ==="
mkdir -p test_dir
touch test_dir/example.txt
ls -l test_dir
mv test_dir/example.txt test_dir/renamed_example.txt
ls -l test_dir

# Task 2: Viewing File Contents
echo "=== Task 2: Viewing File Contents ==="
cat /etc/passwd
head -n 5 /etc/passwd
tail -n 5 /etc/passwd

# Task 3: Searching for Patterns
echo "=== Task 3: Searching for Patterns ==="
grep "root" /etc/passwd

# Task 4: Zipping and Unzipping
echo "=== Task 4: Zipping and Unzipping ==="
zip -r test_dir.zip test_dir
unzip test_dir.zip -d unzipped_dir
ls -l unzipped_dir/test_dir

# Task 5: Downloading Files
echo "=== Task 5: Downloading Files ==="
wget -O sample.txt https://example.com/sample.txt
ls -l sample.txt

# Task 6: Changing Permissions
echo "=== Task 6: Changing Permissions ==="
touch secure.txt
ls -l secure.txt
chmod 444 secure.txt
ls -l secure.txt

# Task 7: Working with Environment Variables
echo "=== Task 7: Working with Environment Variables ==="
export MY_VAR="Hello, Linux!"
echo $MY_VAR

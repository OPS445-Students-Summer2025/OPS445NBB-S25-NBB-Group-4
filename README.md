# Winter 2025 Assignment 2
OPS445NBB-S25-NBB-Group-4

# Assignment 2
Program: assignment2.py 
Topic: Memory usage tracker
MVP: 
1. Show overall and used memory 
2. Show memory usage by application name -> process ID
**Additonal: Show top-memory using  processes sorted by percentage
Author: Group 4
Members: Aung Kaung Satt, Daniel Rhodes, Marian Derlina Fernando, Raffy Limon, Yuefan Zhang

# Overview

This Python script scans the host computer and reports on memory usage. It reads from system files like /proc/meminfo and /proc/[pid]/status to get the memory details and formats them for the user. The script is designed to be simple, readable and extendable.

# Features
-Reads from '/proc/meminfo'
-Prints total memory in MiB or GiB
-Prints used memory in MiB or GiB

# Sample output
./assignment2.py
Total Memory: 7800 MiB
Used Memory: 3500 MiB

./assignment2.py --showGB
Total Memory: 7.8 GiB
Used Memory: 3.2 GiB

./assignment2.py --loop 5 #Output refreshes every 5 seconds

# Division of work
-Raffy: Reads from '/proc/meminfo', gets total and available memory
-Daniel: Raeds memory info from '/proc/[pid]/status' for each process\
-Yuefan: Sorts memory usage and handles top-N filtering
-Aung: Formats and print the final report
-Marian: Adds '--loop' , '--showGB', '--top' options and builds 'main()'


# Communication
We meet weekly via Microsoft Teams on Mondays at 8PM. We stayed via group chat for smaller updates.

# Development Flow
-Each member works on their own branch
-Opens pull request for review
-After review, merge into main

References

    GitHub Docs. (n.d.). Creating and deleting branches within your repository.
    Retrieved July 15 2025, https://docs.github.com/en/repositories/creating-and-managing-repositories

    Python Software Foundation. (2025). argparse — Parser for command‑line options, arguments and sub‑commands.
    https://docs.python.org/3/library/argparse.html

    Kerrisk, M. (2024). proc(5) — Linux manual page.
    https://man7.org/linux/man-pages/man5/proc.5.html

    Linux Kernel Documentation. (n.d.). /proc/meminfo — Memory information file.
    https://docs.kernel.org/filesystems/proc.html#meminfo

    Python Software Foundation. (2025). Numeric types — int, float.
    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float

    Python Software Foundation.* (2025). Built‑in types — list.
    https://docs.python.org/3/library/stdtypes.html#list.sort

    Python Software Foundation.* (2025). argparse — Parser for command‑line options.
    https://docs.python.org/3/library/argparse.html


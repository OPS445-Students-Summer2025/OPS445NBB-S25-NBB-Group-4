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

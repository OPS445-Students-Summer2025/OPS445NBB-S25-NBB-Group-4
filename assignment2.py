#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: assignment2.py 
Topic: Memory usage tracker - A script that scans the host computer and returns total memory and used memory. 
MVP: 1. Overall memory usage 2. By application name -> process id
Additonal: Lists per process memory use, sorted by percent
Author: Group 4
Members: Aung Kaung Satt, Daniel Rhodes, Marian Derlina Fernando, Raffy Limon, Yuefan Zhang
'''

import os
import argparse

# Raffy-Limon:read /proc/meminfo block
def get_overall_mem():
    #Assigned task: Raffy Limon to implement: read from /proc/meminfo
    """Reads total and available memory from /proc/meminfo"""
    #Add parsing logic to read total and available memory lines from /proc/meminfo.
    total_kib = 0  #store 0 as initial value
    avail_kib = 0  #store 0 as initial value
    try:
        f = open('/proc/meminfo', 'r') #reads /proc/meminfo
        for line in f:         #read the file line by line
            parts = line.split()   #split each line into words
        if len(parts) >= 2:    #check if line has at least key and value
            if parts[0] == 'MemTotal:':
                total_kib = int(parts[1])        #save total mem to KB
            elif parts[0] == 'MemAvailable:':
                avail_kib = int(parts[1])        #save avail mem to KB
        f.close()     #close after reading
    except OSError:   #handle error if there's a problem reading /proc/meminfo 
        print ('error: could not read /proc/meminfo')
        return (total_kib // 1024, avail_kib // 1024)   #convert values from KB to MB
   
      

# Daniel Rhodes: gather per‑process memory usage block
def get_process_mem():
    #Assigned task: Daniel Rhodes to implement: get process memory usage
    '''Initializes the list to store mem information per process'''
    mem_data = []
#This creates a list to hold the information on memory needed to be accessed later
    for pid in os.listdir('/proc'):
#Iterates throught the list in the process directory and searches for process id's
        if pid.isdigit():
#Ensures the information is a PID because it is a digit
            path = '/proc/' + pid + '/status'
#Gives the path to the file for the process being looked at
            try:
                f = open(path)
            except:
                continue
#Moves to the next process if the one in the loop cannot be done
            name = ''
            rss_kib = 0
#Above two lines set up variables for process and memory info
            for line in f:
                if line.startswith('Name:'):
#Checks for the process name
                    name = line.split()[1]
#Pulls the name once it establishes it is there
                elif line.startswith('VmRSS:'):
#Checks for RSS to know it is using memory
                    rss_kib = int(line.split()[1])
#Pulls usage and makes it a usable number
                    break
        f.close()
#Closes file
#Now we Calculate percentages and add the process to the list
        if rss_kib > 0 and name != '':
#The above checks that it has something in memory and below it converts it to MiB
            rss_mib = rss_kib // 1024
#Sets percentage usage to the MiB divided by the overall memory
            percent = (rss_mib * 100.0) / get_overall_mem()[0]
            mem_data.append((percent, name))
#Appends to mem_data to avoid overwriting previous entries
    return mem_data






# Aung Kaung Satt: memory usage display block 
# Assigned task: Aung Kaung Satt to implement: calculate used memory and print header
def print_report():
    print("Memory Usage Report")
    print("-------------------")
# Get total and available memory in MiB from the system
    total_mib, avail_mib = get_overall_mem()
# Calculate used memory by subtracting available from total
    used_mib = total_mib - avail_mib
# Display total memory
    print("Total Memory:", total_mib, "MiB")
# Display used memory
    print("Used  Memory:", used_mib, "MiB")
    print()
    print("Top Processes by Memory Use:")
    print("----------------------------")
    # Process list will be printed here later
# Retrieve a list of processes with their memory usage
    proc_list = get_process_mem()

# Sort the process list by memory usage (usually descending)
    sorted_list = sort_processes(proc_list)

# Filter the top 5 memory-consuming processes
    top_list = filter_top(sorted_list, 5)  # show top 5 for now

# Display the top memory-consuming processes
    show_top(top_list)

# Yuefan Zhang: sorting and displaying top processes - put inside memory usage display block
# Yuefan Zhang: sorting and formatting for later
def sort_processes(proc_list):
# Sort the list in descending order
    return sorted(proc_list, reverse=True)
# Add filter logic for top N processes (value passed later).
def filter_top(proc_list, top_n):
# Check if a specific number of top processes is requested
    if top_n is not None:
# Return only the top N processes
        return proc_list[:top_n]
# If no specific number requested, return the full list
    return proc_list

# Marian Derlina Fernando: Additional features: 
# --showGB   show values in GiB instead of KiB which is default from /proc
# --loop N   refresh every N seconds until Ctrl‑C
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--showGB', action='store_true') #helps to show the memory in GiB
    parser.add_argument('--loop', type=int) #allow the user to loop the report N times
    return parser.parse_args() #returns user's output
#Assigned task: Marian Derlina Fernando to implement: handle command-line arguments
    pass





def main():
    #Assigndd task: Marian Derlina Fernando to implement: main block
    pass






if __name__ == '__main__':
    pass

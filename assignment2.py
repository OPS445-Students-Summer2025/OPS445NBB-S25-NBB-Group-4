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
    #This is the lost that will store the information to pull
#This creates a list to hold the information on memory needed to be accessed later
    for pid in os.listdir('/proc'):
#Iterates throught the list in the process directory and searches for process id's
        if pid.isdigit():
#Ensures the information is a PID because it is a digit
            try:
#opens the file to run through data retrieving needed memory info
                f = open('/proc/' + pid + '/status', 'r')
                name = ''
                rss_kib = 0
#Memory in KiB
                for line in f:
                    if line.startswith('Name:'):
#This pulls process name to be scanned for info
                        name = line.split()[1]
                    elif line.startswith('VmRSS:'):
                        rss_kib = int(line.split()[1])
#Takes memory and stores as an interger
                        break
                f.close()
#Closing the file to conserve memory and cpu usage
                if rss_kib > 0 and name != '':
                    rss_mib = rss_kib // 1024
#Converting grom KiB to MiB to make it more easily read
                    percent = (rss_mib * 100.0) / get_overall_mem()[0]
#This is what measures it against the total memory to see more acurate percentage
                    mem_data.append((percent, name))
#Takes the result and adds to the list created at the beginning of the function
            except:
                pass
#Moves past errors with possible permission issues or closed processes
    return mem_data

#Some /proc/[pid]/status files may disappear quickly; just ignore and watch for failures
#Some skipped processes may be due to missing infor or access issues






# Aung Kaung Satt: memory usage display block 
# Assigned task: Aung Kaung Satt to implement: calculate used memory and print header
def print_report(total, available, proc_list, show_gb):
    # Print report header
    print("Memory Usage Report")
    print("--------------------")

    # Calculate used memory
    used = total - available

    # Set default unit and divisor (MiB)
    unit = 'MiB'
    divisor = 1.0

    # If show_gb is True, convert to GiB
    if show_gb:
        unit = 'GiB'
        divisor = 1024.0

    # Display total and used memory in selected unit
    print('Total Memory :', round(total / divisor, 2), unit)
    print('Used  Memory :', round(used / divisor, 2), unit)
    print()

    # Print process memory usage section header
    print("Top Processes by Memory Use:")
    print("----------------------------")

    # Print each top process: name and memory usage percentage
    for item in proc_list:
        print(item[1].ljust(15), str(round(item[0], 2)) + ' %')

# Yuefan Zhang: sorting and displaying top processes - put inside memory usage display block
# Refactor sorting and filtering helpers with docstrings.
def sort_processes(proc_list):
    """Sorts by percent usage (descending)"""
    proc_list.sort()  # Sort the list in ascending order by default
    proc_list.reverse()  # Reverse it to get descending order
    return proc_list  # Return the sorted list

def filter_top(proc_list, n):
    """Returns top N entries or all if N is None"""
    if n is None:  # If n is None, return the entire list
        return proc_list
    return proc_list[:n]  # return only the top n items

#Add simple sorting function
def show_top(proc_list):
    for item in proc_list:  # Round the percentage value to 2 decimal places
        pct = round(item[0], 2)
        name = item[1]  # Extract the process name
        print(name.ljust(15), str(pct) + ' %')  # Print the name and percentage with a '%'

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
    total, available = get_overall_mem()
    print("Total Memory    :", total, "MiB")        #test reading total mem
    print("Available Memory:", available, "MiB")    #test reading avail mem

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
    except:
        print("Error opening meminfo file.")
        return (0, 0)
   
      

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




# Aung Kaung Satt: memory usage display block 
def name_here():
    #Assigned task: Aung Kaung Satt to implement: calculate used memory and print header
    


# Yuefan Zhang: sorting and displaying top processes - put inside memory usage display block




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

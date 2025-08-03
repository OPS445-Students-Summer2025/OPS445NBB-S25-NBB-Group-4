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
    try:
        f = open('/proc/meminfo', 'r')
    except:
        print("Error opening meminfo file.")
        return (0, 0)
   #Add parsing logic to read total and available memory lines from /proc/meminfo.
    total_kib = 0
    avail_kib = 0
    for line in f:
        parts = line.split()
        if len(parts) >= 2:
            if parts[0] == 'MemTotal:':
                total_kib = int(parts[1])
            elif parts[0] == 'MemAvailable:':
                avail_kib = int(parts[1])    



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




# Aung Kaung Satt: memory usage display block 
def print_report(total, available, proc_list, show_gb):
    print("Memory Usage Report")
    print("-------------------")
    print("-------------------")
    total_mib, avail_mib = get_overall_mem()
    used_mib = total_mib - avail_mib

    print("Total Memory:", total_mib, "MiB")
    print("Used  Memory:", used_mib, "MiB")
    print()
    print("Top Processes by Memory Use:")
    print("----------------------------")
    used = total - available
    unit = 'MiB'
    divisor = 1.0
    if show_gb:
        unit = 'GiB'
        divisor = 1024.0
    proc_list = get_process_mem()
    sorted_list = sort_processes(proc_list)
    top_list = filter_top(sorted_list, 5)  # show top 5 for now
    show_top(top_list)

    print('Total Memory :', round(total / divisor, 2), unit)
    print('Used  Memory :', round(used / divisor, 2), unit)
    print('')
    print('Top Processes by Memory Use:')
    print('----------------------------')
    for item in proc_list:
        print(item[1].ljust(15), str(round(item[0], 2)) + ' %')
# Yuefan Zhang: sorting and displaying top processes - put inside memory usage display block

    # build list of [pct, name, pid], the name trimmed to 15 chars
    tops = []
    for name, pid, rss in proc_list:
        pct = (rss * 100.0) / used if used else 0.0
        tops.append([pct, name[:15], pid])

    print("\nTop processes by memory use:")
    print("--------------------------------")
    print("Process            PID     %MEM")

    # select-and-pop the largest five 
    for _ in range(5):
        if not tops:            # fewer than 5 processes
            break
        # find index of current max
        idx_max = 0
        for i in range(1, len(tops)):
            if tops[i][0] > tops[idx_max][0]:
                idx_max = i
        pct, p_name, p_pid = tops.pop(idx_max)

        # prints one table row
        short_name = p_name
        print(short_name, " "*(17-len(short_name)), pid, " "*(7-len(str(pid))), str(round(pct,2))+' %')

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

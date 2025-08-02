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

# Raffy-Limon:read /proc/meminfo block
def name_here():
    #Assigned task: Raffy Limon to implement: read from /proc/meminfo
    pass






# Daniel Rhodes: gather per‑process memory usage block
def name_here():
    #Assigned task: Daniel Rhodes to implement: get process memory usage
    pass





# Aung Kaung Satt: memory usage display block 
def print_report(total, available, proc_list, show_gb):
    print("Memory Usage Report")
    print("-------------------")  
    total_mib, avail_mib = get_overall_mem()
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




# Marian Derlina Fernando: Additional features: 
# --showGB   show values in GiB instead of MiB
# --loop N   refresh every N seconds until Ctrl‑C
def name_here():
#Assigned task: Marian Derlina Fernando to implement: handle command-line arguments
    pass





def main():
    #Assigndd task: Marian Derlina Fernando to implement: main block
    pass






if __name__ == '__main__':
    pass
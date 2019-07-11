import os
import csv
import sys
from datetime import datetime

if __name__ == '__main__':
 #read in the input text file:
 inactivity_period = 0 
 fmt = '%Y-%m-%d %H:%M:%S'
 with open('../input/inactivity_period.txt') as inactve_file:
    inactivity_period = inactve_file.read()
    print(inactivity_period)

 #extract the current timestamp ie : the first row:
 with open('../input/log.csv') as csvfile:
    readerfile = csv.reader(csvfile)
    row1 = next(readerfile)
    row2 = next(readerfile)
    
    current_time = datetime.strptime(row2[1] + ' ' + row2[2],fmt )
    print(current_time)


 #store the ip-address information which have been accessed at a particular time in a dictionary:
 ip_requests_time = {}
 ip_requests_list = []
 with open('../input/log.csv') as csvfile:
    readerfile = csv.DictReader(csvfile)
   
    
    for row in readerfile:
        rowcount = 0
        ip_requests_time = {}
        row_time = datetime.strptime(row['date'] + ' ' + row['time'], fmt)
        
        time_difference =  row_time - current_time
        
        time_diff_seconds = int(time_difference.total_seconds())
        print(time_diff_seconds)
        inactivity_period = 2
        if(time_diff_seconds < inactivity_period):
           if row['date'] + ' ' + row['time'] == current_time:
              ip_requests_time['ip'] = row['ip']
              ip_requests_time['cik'] = row['cik']
              ip_requests_time['acc'] = row['accession']
              ip_requests_time['req_time'] = current_time
              
              ip_requests_list.append(ip_requests_time)


           else:
              current_time = row['date'] + ' ' + row['time']
        print(rowcount)
        rowcount = rowcount + 1


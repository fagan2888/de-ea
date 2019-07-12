import os
import csv
import sys
from datetime import datetime


giant_metric_info = []
ip_addrs_list = []
"""
def calculate_metrics(SessionList):
  for session_info in SessionList:
     if session_info['ip'] not in ip_addrs_list:
        ip_addrs_list.append(session_info['ip'])
        metric_dict ={}
        metric_dict['ip'] =  session_info['ip']
        metric_difct['pages_accessed'] = {}
        


     else:
        #calculate the number of pages accessed by the session:
""" 

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
 ip_addrs_list = []
 seconds_elapsed  = 0
 with open('../input/log.csv') as csvfile:
    readerfile = csv.DictReader(csvfile)
   
    
    for row in readerfile:
        rowcount = 0
        ip_requests_time = {}
        row_time = datetime.strptime(row['date'] + ' ' + row['time'], fmt)
        # time_difference =  row_time - current_time
        #time_diff_seconds = int(time_difference.total_seconds())
        #print(time_diff_seconds)
        if row_time == current_time:
           # as long as the row time is equal to the current time, push all the rows to the list ; collating them by the same timestamp
           """
           session_info_dict = {}
           session_info_dict['ip'] = row['ip']
           session_web_pages_info_list = []
           session_web_page_info = {}
           session_web_page_info['date_time'] = row['date'] + ' ' + row['time']
           session_web_page_info['web_log'] = row['cik'] + ' ' + row['accession'] + ' ' + row['extension']
           session_web_page_info
           ip_requests_list.append(session_info_dict)
           """
           if row['ip'] not in ip_addrs_list:
              ip_addrs_list.append(row['ip'])
              session_info_dict = {}
              session_info_dict['ip'] = row['ip']
              session_web_pages_info_list = []
              session_web_page_info = {}
              session_web_page_info['date_time'] = row['date'] + ' ' + row['time']
              session_web_page_info['web_log'] = row['cik'] + ' ' + row['accession'] + ' ' + row['extention']
              session_web_page_info['seconds_elapsed'] = seconds_elapsed
              session_web_pages_info_list.append(session_web_page_info)
              session_info_dict['web_log'] = session_web_pages_info_list
              #new_dict = dict(zip(row['ip'], session_info_dict))
              #print(session_info_dict)
              print(new_dict)              
              ip_requests_list.append(session_info_dict)

           else:
              """            
              session_web_page_info = {}
              session_web_page_info['date_time'] = row['date'] + ' ' + row['time']
              session_web_page_info['web_log'] = row['cik'] + ' ' + row['accession'] + ' ' + row['extension']
              session_web_page_info['seconds_elapsed'] = seconds_elapsed
              session_web_pages_info_list.append(session_web_page_info)
              """


           #calculate metrics for each second:
           
           
        #else:
           #seconds_elapsed += (row_time - current_time)
           #current_time =  row_time
           #if seconds_elapsed 

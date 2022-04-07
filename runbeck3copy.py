#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 19:14:04 2022

@author: Mindy
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:28:23 2022

@author: Mindy
"""
# =============================================================================
# Ask whether the file exists in directory?
# =============================================================================
# =============================================================================
# Ask Questions to Users
# =============================================================================

print("Where is the file located?")
location= input()
print("Is the file CSV or TSV (tab-seperated values)?")
file_type=input().upper()
print("How many fields should each record contain?")
quantity=int(input())

# =============================================================================
# Create List, Sorted by Whether They are Approved or Not
# =============================================================================
approve_list=[]
error_list=[]

# =============================================================================
# Distinguish The File Type And Create Paths
# =============================================================================
        
if (file_type == "CSV") or (file_type=="TSV"):
     import csv
     import re
     
# =============================================================================
# Locate File   
# =============================================================================
     with open(location, 'r') as csv_file:
         csv_reader= csv.reader(csv_file)
# =============================================================================
# Remove Headings         
# =============================================================================
         next(csv_reader)
# =============================================================================
# Read The File, Set Conditions For File Type And Create New List To Add To        
# =============================================================================
         if file_type== "CSV":    
             for line in csv_reader:
                 #print(line)
                 #print(len(line))
                 if len(line)==quantity:
                     approve_list.append(line)
                 else:
                     error_list.append(line)
                 
         if file_type== "TSV":         
             for line in csv_reader:
                 #print(line)
                 tabList = re.split(r'[ \t]',line[0])
                 #print(len(tabList))
                 #print(tabList)
                 #print(len(line))
                 if len(tabList)==quantity:
                     approve_list.append(tabList)
                 else:
                     error_list.append(tabList)
                 

# =============================================================================
#          print("\n")
#          print(approve_list)
#          print(error_list)
#          print (len(approve_list))
#          print (len(error_list))
# =============================================================================

# =============================================================================
# Format Data Onto New Files         
# =============================================================================
         if len(approve_list)>0:
             final_csv=open("final_approved.csv", "w+")  
             for data in approve_list:
                 if file_type== "CSV":
                    final_csv.write(",".join(data))
                    final_csv.write("\n")
                 else:
                    final_csv.write("\t".join(data))
                    final_csv.write("\n")
             final_csv.close()
                 
         if len(error_list)>0:
             final_error=open("final_errors.csv", "w+")  
             for data in error_list:
                 if file_type== "CSV":
                    final_error.write(",".join(data))
                    final_error.write("\n")
                 else:
                    final_error.write("\t".join(data))
                    final_error.write("\n")
             final_error.close()          
     
else:
    print("You did not select a valid file type.")

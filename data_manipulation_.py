# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 13:50:23 2019
@author: maynard Collin

This code helps with accessing each indivdual data file for better analysis of data and for performing data manipulations

"""
from time import time, ctime
from datetime import datetime

def populate():
# file 1 of each data collection ---NOT USALABLE UNTIL MANIPULATION
    ########    RAWWWWWWWWWWWWWWWWWWWWWWWWWWWW FILE_LOCATION's 
    file_path = "C:\\Users\\mayna\\Desktop\\Senior Research Snippets\\Senior_Research_\\SR_Data Collection\\Data_as_text_files"
    
    ORG_file = file_path + "\\_org_.txt"
    
    GOV_file = file_path + "\\_gov_.txt"
    
    EDU_file = file_path + "\\_edu_.txt" 
    
    NET_file = file_path + "\\_net_.txt"
    
    COM_file = file_path + "\\_com_.txt"
    
    
    # dictionary for each file group location values
    #FILE_dictionary={'gov':GOV_file,'org':ORG_file,'net':NET_file,'edu':EDU_file,'com':COM_file}
    
    FILE_dictionary = {}
    #empy_file_list = [] # holds each group of files for dictionary
    full_file_list = [ORG_file, GOV_file, EDU_file, NET_file, COM_file]
    
    key_list = ['org','gov', 'net', 'edu', 'com'] # holds dictionary key values
    
    
    
    ####################################################
    # key for adding in differnt numbered files
    #print(FILE_dictionary['gov'])
    #manipulation = FILE_dictionary['gov'][:-4] + str(itr) + ".txt"
    #print(manipulation)
    ####################################################
    
    
    
    """-----------------------------------------------
    LOOP FOR POPULATING DICTIONARY WITH FILE NAMES
    loop description:
        
        There are a total of 5 files for each group the filename are unusable without the correct number. Each file are named the same but have a number an example _gov_1.txt for each group these files range from _gov_1.txt through _gov_5
        
        Outer loop loops through each key group org, gov, edu, net, com
        Inner loop loops through each file name and adds it to each group
        
        Example first iteration is 'gov'
        
    -----------------------------------------------"""
    
    """COUNTERS"""
    outer_itr = 0 # outter loop iterator
    inner_itr = 1 # inner loop iterator
    #file_iter = 0 
    # Code the rest in
    for repetition in range(0,5):
        for repetition in range(0,5):
            
            new_key = (str(key_list[outer_itr])) + str(inner_itr) # creates new key for each instance
            #old_key = (str(key_list[outer_itr])) outdated methodology for loop
            
            manipulation = full_file_list[outer_itr][:-4] + str(inner_itr) + ".txt"
            #FILE_dictionary[new_key] = FILE_dictionary[old_key][:-4] + str(inner_itr) + ".txt" # outdated methodology for loop
            
            
            FILE_dictionary[new_key] = str(manipulation) # add file name to dict
    
            """ITERATOR INCREMENTER"""
            inner_itr +=1
            
        inner_itr = 1 # reset inner loop iterator at the increment of outer loop
        outer_itr+=1
    return FILE_dictionary

#
#file_dictionary = populate()
#
#inner_ctr = 1
#outer_ctr = 0
#
#for repetition in range(0,5):
#    for repetition in range(0,5):
#        
#


##### FIGURE out SPlicing Algorithm
aFile="C:\\Users\\mayna\\Desktop\\Senior Research Snippets\\Senior_Research_\\SR_Data Collection\\Data_as_text_files\\_org_1.txt"

with open(aFile) as infile:
    table = infile.readlines()


#print(table[0])
#print()
#print(table[1])

table = table[1:] # removes header

comma_counter = 0 # counts comma for positional argument
data_splice = "" # stores spliced data

inner_itr = 0
#outer_itr = 0

#new_table = {} list might be better than dictionary for this???
table_list = []
# loops through each instance in table
for rows in table:    
    # loops through each row in table and extracts specific columns desired
    # specific columns are ID, expiry, last accessed, and creation time
    for character in rows: # removed working rows[inner_itr]
        
        if character == ',': # increments comma counter to locate data position
            comma_counter += 1
            
        if comma_counter == 0:
            data_splice += character 
        if comma_counter == 7:
            data_splice += character 
        if comma_counter == 8:
            
            data_splice += character 
        if comma_counter == 9:
            data_splice += character
            
            
    #----------- end of inner loop------------------------
    #new_table['ID_'+str(inner_itr)] = data_splice # overwrites table with only desired atrbts
    table_list.insert(inner_itr, data_splice) 
    data_splice = "" # resets data_splice for next round
    comma_counter = 0 # resets comma counter
    inner_itr+=1 # creates new key

#--------------  end of outer loop -------------------------    

#print(new_table['ID_'+str(1)])
#print(new_table)

#print(table_list)

#start_pos = 0
#end_pos = 0
#itr = 0
comma_counter = 0
#example = ""
timestamp1 = ""
timestamp2 = ""
timestamp3 = ""

timestamp = []
save_switch = True
for row in table_list:
    for character in row:
        
        if character == ',':
            comma_counter += 1          
        
        if comma_counter == 1:
            timestamp1 += character
        
        
        if comma_counter == 2:
            timestamp2 += character
        
        if comma_counter == 3:
            timestamp3 += character
    
    # end of inner loop
    # calculate UTC from unix timestamp
        
        
timestamp1 = datetime.fromtimestamp(float(timestamp1[1:]))
    #timestamp2 = datetime.fromtimestamp(float(timestamp2[1:]))
    #timestamp3 = datetime.fromtimestamp(float(timestamp3[1:]))    
print(timestamp1)    
    
    
#print(timestamp1[1:]) # prints timestamp minus comma
#print(timestamp2[1:]) # prints timestamp minus comma
#print(timestamp3[1:]) # prints timestamp minus comma


#print(FILE_dictionary)
##### FOR TESTING LOOP ############################
#print(FILE_dictionary) # print out all modified file locations
#print(len(FILE_dictionary)) # test the correct number of files
#################################################
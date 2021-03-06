# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 13:50:23 2019
@author: maynard Collin

This code helps with accessing each indivdual data file for better analysis of data and for performing data manipulations

"""
from datetime import datetime

"""
This function populates a dictionary with all the different data file locations.
"""
def populate():
# file 1 of each data collection ---NOT USALABLE UNTIL MANIPULATION
   
    ######## FILE_Directory  ########################
    file_path = "C:\\Users\\mayna\\Desktop\\Senior Research_2019\\Senior Research Snippets\\Senior_Research_\\SR_Data Collection\\Data_as_text_files"
    
    ORG_file = file_path + "\\_org_.txt"
    
    GOV_file = file_path + "\\_gov_.txt"
    
    EDU_file = file_path + "\\_edu_.txt" 
    
    NET_file = file_path + "\\_net_.txt"
    
    COM_file = file_path + "\\_com_.txt"
    
    
    FILE_dictionary = {}
    #empy_file_list = [] # holds each group of files for dictionary
    full_file_list = [ORG_file, GOV_file, EDU_file, NET_file, COM_file]
    
    key_list = ['org','gov', 'net', 'edu', 'com'] # holds dictionary key values
    
    
    
    ####################################################
    # key for adding in differnt numbered files
    # manipulation = FILE_dictionary['gov'][:-4] + str(itr) + ".txt"
    # manipulation goes back before the .txt and adds the file number 
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
           
            
            manipulation = full_file_list[outer_itr][:-4] + str(inner_itr) + ".txt"
            
            FILE_dictionary[new_key] = str(manipulation) # add file name to dict
    
            """ITERATOR INCREMENTER"""
            inner_itr +=1
            
        inner_itr = 1 # reset inner loop iterator at the increment of outer loop
        outer_itr+=1
    return FILE_dictionary

######################################
"""END OF DEF POPULATE()"""
######################################

# Function calculates persistency of cookie!
def check_persitency(counter,cookie):
        return cookie['exp_'+str(counter)]-cookie['creationT_'+str(counter)]


def proccess_data_files(file):
    
    ##### FIGURE out SPlicing Algorithm ##########
    #aFile="C:\\Users\\mayna\\Desktop\\Senior Research_2019\\Senior Research Snippets\\Senior_Research_\\SR_Data Collection\\Data_as_text_files\\_org_1.txt"
    
    aFile = file
    
    with open(aFile) as infile:
        table = infile.readlines()
    
    
    #print(table[0])
    #print()
    #print(table[1])
    header = table[0]
    print("Header of Table:",header)
    table = table[1:] # removes header
    
    comma_counter = 0 # counts comma for positional argument
    
    data_splice1 = "" # stores spliced data
    data_splice2 = "" # stores spliced data
    data_splice3 = "" # stores spliced data
    data_splice4 = "" # stores spliced data
    
    inner_itr = 1
    pos_itr1 = 0
    pos_itr2 = 0
    
    cookie_data = {}
    
    
    #table_list = []
    """Nested loop for data conversion 
    outer loop part 1: goes through each row one file 
    
    inner loop: goes through each character of the row of a file. Upon finding a comma updates position. When certain positions are found store data. 
    
    outer loop part 2: converts spliced data from inner loop to date time structure
    
    """
    
    # loops through each instance in table
    for rows in table:    
        """Outer Loop Part 1"""
        # loops through each row in table and extracts specific columns desired
        # specific columns are ID, expiry, last accessed, and creation time
        for character in rows: # removed working rows[inner_itr]
            
            ###----- MOVE THROUGH DATA ----------
            ###----- Program to gather specific pieces out of the database
            if character == ',': # increments comma counter to locate data position
                comma_counter += 1   
            ###----- Select data at position 0
            ###----- Gets the database ID
            if comma_counter == 0:
                data_splice1 += character # dictionaries don't play with +=
                cookie_data['ID_'+str(inner_itr)] = data_splice1 
            ###----- Select data at position 7
            ###----- Data at position 7 is expiration date
            if comma_counter == 7:
                data_splice2 += character # dictionaries don't play with +=
                cookie_data['exp_'+str(inner_itr)] = data_splice2
            ###----- Select data at position 8
            ###----- Position 8 is last accessed date
            if comma_counter == 8:
                """Decimal place insertion after tenth digit"""
                if pos_itr1 == 11:
                    data_splice3 += "." # places decimal after tenth digit
                data_splice3 +=character # dictionaries don't play with +=
                cookie_data['lastAccessed_'+str(inner_itr)] = data_splice3
                pos_itr1 +=1
            ###----- Select data at position 9
            ###----- Position 9 is creation time
            if comma_counter == 9:
                """Decimal place insertion after tenth digit"""
                if pos_itr2 == 11:
                    data_splice4 += "." # places decimal after tenth digit
                data_splice4 += character # dictionaries don't play with +=
                cookie_data['creationT_'+str(inner_itr)] = data_splice4
                pos_itr2 +=1
        
        ######## VARIABLE RESET #############################
        data_splice1 = "" # resets data_splice for next round
        data_splice2 = "" # resets data_splice for next round
        data_splice3 = "" # resets data_splice for next round
        data_splice4 = "" # resets data_splice for next round    
        
        pos_itr1 = 0
        pos_itr2= 0
        
        comma_counter = 0 # resets comma counter
        ###########################################################
        """------------Outer Loop Part 2---------------------------"""
        """------------TIME STAMP CONVERSION ALGORITHM ------------"""
        ###########################################################
        """
        Note the [1:] removes a comma that is included in the string
        Then the string stored at each dictionary location is casted to a float type
        Then the float type is casted to a date_time type
        Then the location is overwritten with this conversion
        """    
        cookie_data['exp_'+str(inner_itr)] = datetime.fromtimestamp(float(cookie_data['exp_'+str(inner_itr)][1:]))
        cookie_data['lastAccessed_'+str(inner_itr)] = datetime.fromtimestamp(float(cookie_data['lastAccessed_'+str(inner_itr)][1:]))
        cookie_data['creationT_'+str(inner_itr)] = datetime.fromtimestamp(float(cookie_data['creationT_'+str(inner_itr)][1:]))
        
        
        inner_itr+=1 # creates new key
    
    #print(cookie_data)  
    
    print() # page break
    print() # page break
    print() # page break
    
    itr = 1 #--- resets iterator for new loop
    
    ###------ Displays Data to Screen
    for rows in table:    
        print("Persistance of cookie",str(itr),check_persitency(itr,cookie_data))
        itr+=1
        
#############################################################################
        # MAIN BODY OF CODE
#############################################################################

for num in range(0,2):
    key_list = ['org','gov', 'net', 'edu', 'com'] # holds dictionary key values
    data_files = populate()
    num = num+1
    
    print() # first page break
    print() # first page break
    print() # first page break
    
    print("Datafiles", data_files[key_list[0]+str(num)])
            
    proccess_data_files(data_files[key_list[0]+str(num)])
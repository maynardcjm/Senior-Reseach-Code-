# -*- coding: utf-8 -*-
"""
Senior Research COokie Data Processsing Python Script
Collin Maynard 
12/13/2019

"""
# Python Modules for timestamp datastructures
from datetime import datetime


################    FUNCTIONS  SECTION     ################################
"""
Function Name: getRealTime
Function Params: row is the instance of the cookie table
Function Description: 1) Splices information out of the table
                      2) Inserts CRITICALLY important decimal place
                      3) converts information into UTC format 
                      4) stores in list
                      5) Repeats this for two more timestamps
                      6) returns list
"""
def getRealTime(row):
   
    timestamps = [] # creates list to hold three different timestamps
    counter = 0
    
    # set decimal position for timestamp1
    timestamp = row[0:10].strip() + "." + row[10:17].strip() # splicing data
    timestamp = datetime.fromtimestamp(float(timestamp)) # formats to UTC
    timestamps.insert(counter,timestamp) # adds value to list
    
    counter +=1 # incrementer for list insertion
    
    # set decimal position for timestamp2
    timestamp = row[17:27].strip() + "." + row[27:33].strip()# slices data
    # convert to UTC
    timestamp = datetime.fromtimestamp(float(timestamp)) # formats to UTC
    timestamps.insert(counter,timestamp) # adds value to list
    
    counter +=1
    
    # No decimal point needed for the 10-digit timestamps
    timestamp =  row[34:44].strip()# slices data
    timestamp = datetime.fromtimestamp(float(timestamp)) # formats to UTC
    timestamps.insert(counter,timestamp) # adds value to list
    
    return timestamps
################    end of getRealTime func  ################################


"""
Function Name: check_persistence
Function Params: An iterator named counter to keep place, and the cookie dict
Function Description: Calculates and returns difference of creation and expiration time
"""
def check_persistence(cookie, counter):
    return cookie['ID'+str(counter)][2]-cookie['ID'+str(counter)][1]
    
################    end of check_persistence func ############################


"""
Function Name: writeFile
Function Params: cookie dictionary 
Function Description: Creates new table of processed data and writes two files
File Output: 
             File 1: contains timestamp information for last accessed, creation time,                      
                           and expiration time
             File 2: contains the life span of the cookie
"""
def writeFile(cookie):
    
    counter = 1 # iterator for table instances
    newfile = open("mySR_resutls.txt", "w") # creates file for timestamp conversions
    newfile.write("lastAccessed\t\t\t\t creationTime\t\t\t\t exipires\n") # table header

#### Loop 1 ####    
    for row in cookie:
        if counter > 273:
            break
        newfile.write(str(cookie['ID'+str(counter)][0])+"\t") # writes last accessed
        newfile.write(str(cookie['ID'+str(counter)][1])+"\t") # writes creation time
        newfile.write(str(cookie['ID'+str(counter)][2])+"\n") # writes expiration
        
        counter +=1 #
        
###### end of Loop 1 #####
        
    newfile.close() # closes file 1
    counter = 1
    persFile = open("my_SR_persist_cookies.txt","w")
    persFile.write("ID\t\t Persistent\n")
    for row in cookie:
        if counter > 273:
            break
        persFile.write(str(counter) + "\t\t" + str(cookie['persistence'+str(counter)]) + "\n")
        counter +=1
    persFile.close()


"""----------------------------------------------------------------------

def sortPersistenceLIFE(cookie):
    
    itr = 2
    pos = 1
    greatest = cookie['persistence'+str(1)]
    cookie['sorted'+str(1)] = greatest
    while pos < 272:
        for row in cookie:
            if itr > 273:
                break
            if cookie['persistence'+str(itr)] > greatest:
                cookie['sorted'+str(pos)] = greatest
            itr +=1
        pos+=1
    return cookie
"""

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
*******************************************************************************
------------------------ MAIN BODY --------------------------------------------
*******************************************************************************
"""
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#################   FILE LOCATION      ####################################
ALL_file = "C:\\Users\\mayna\\Desktop\\Senior Research_2019\\Senior Research Snippets\\Senior_Research_\\SR_Data Collection\\textData_files_forPYTHON\\All_cookies_timestamp.txt"

#########################   Open up file  ###################################
with open(ALL_file) as infile :
    table = infile.readlines()

#print(table[0]) #prints headers for visual

table = table[1:] # removes headers


itr = int(1) # iterator shifts dictionary key value to allow new instances loop 

cookie_lifecyle={} # dictionary to hold cookies' timestamp data


# Loops through every instance in the table
for row in table:
    
    # populate dictionary with each row instance 
    cookie_lifecyle['ID'+str(itr)] = getRealTime(row)
    cookie_lifecyle['persistence'+str(itr)] = check_persistence(cookie_lifecyle,itr)
    itr = int(itr)+1 # increase iterator

print("Your Cookie-data Files are Ready!!!")
print("The data has been written to: my_SR_persist_cookies.txt & mySR_resutls.txt")
# output test 
#print(cookie_lifecyle['ID1'][0])
#print(cookie_lifecyle['persistence1'])   

 
#sortPersistenceLIFE(cookie_lifecyle)
writeFile(cookie_lifecyle) # method call to write files!
########################################################################
"""
########################     END OF CODE     ###########################
"""
########################################################################
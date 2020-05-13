
path = "C:\\Users\\mayna\\Desktop\\Senior Research_2019\\Senior Research Snippets\\Senior_Research_\SR_Data Collection\\textData_files_forPYTHON"

ORG_file = path+"\\ORG_DataSET_.txt"

GOV_file = path+"\\GOV_DataSET_.txt"

EDU_file = path+"\\EDU_DATAset_.txt" 

NET_file = path+"\\NET_DATAset_.txt"

COM_file = path+"\\COM_DATAset_.txt"

filelist=[ORG_file, GOV_file, EDU_file, NET_file, COM_file]

# Display file names
#for f in range(0,len(filelist)):
#    print(filelist[int(f)])


itr = 0
for f in filelist:
    with open(filelist[itr]) as infile :
        table = infile.readlines()
    
    if itr == 0:
        print("File Sizes")    
    table = table[1:]
    print(filelist[int(itr)][-16:-13], "files =", len(table))
    itr+=1
    
    
#python exe03.py src.txt dst.txt
import sys
import os

if len(sys.argv) < 3:
    print("ERROR: please insert second file name")
else:
    read_file_name = sys.argv[1]
    write_file_name = sys.argv[2]


    if os.path.exist(read_file_name):   
        fr = open(read_file_name, "r")
    else:
        print("ERROR: File Name is wrong or not exist!")
    if os.path.exist(write_file_name):   
        fw = open(write_file_name, "w")
    else:
        print("ERROR: File Name is wrong or not exist!")

    for line in fr:
        fw.write(line)
    
    fw.close()
    fr.close()


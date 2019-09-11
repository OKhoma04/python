import csv
import sys
import json

csv_path = sys.argv[1]      # 1st argument (csv name) from cmd
json_path = sys.argv[2]     # 2nd argument (json name) from cmd,


#remove column 'password' from csv and write into json file
with open(csv_path, 'r') as csv_file, open(json_path, 'w') as json_file:                #read from CSV and write to JSON file
    csv_reader = csv.DictReader(csv_file)                                               #read csv as dictionary
    new_list = [{k: v for k, v in d.items() if k != 'password'} for d in csv_reader]    #remove column 'password' from csv
    qq=json.dump([lines for lines in new_list], json_file)

#read json file
lines = json.loads((open(json_path,'r').read()))
print('JSON printed as list in one line: \n', lines)
print('CSV rows printed as separate JSON files: \n', *lines, sep = "\n")




import csv
import sys
import re


file_name = sys.argv[1]                 # 1st argument (file name) from cmd
col_name = " ".join(sys.argv[2:])       # 2nd argument (column name) from cmd, argument can includes several whitespaces
col_name_clean = re.sub("[^A-Za-z]", " ", col_name.lower()) #remove incorrect characters from column name

#Work with inserted arguments, retrieve corresponding data from csv
with open(file_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)       #read csv as dictionary
            csv_header_real = csv_reader.fieldnames     #csv header
            csv_header = [x.lower() for x in csv_reader.fieldnames]     #csv header lowercase
            pos = csv_header.index(col_name_clean)      #verify position of inserted column name in csv header
            for lines in csv_reader:
                col_name_csv = csv_header_real[pos]     #looking for real csv column header for inserted position
                col_name_value = lines.pop(col_name_csv) #retrieve data from selected column
                print(col_name_value)


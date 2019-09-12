import sys
import pyodbc
import json
import decimal

file_sql = sys.argv[1] #argument from cmd

#connection to MS SQl Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=EPUALVIW1270;'
                      'Database=TSQL2012;'
                      'Trusted_Connection=yes;')


#execution of SQL file
def exec_sql(file_sql):
    fd=open(file_sql,'r')
    sql_file = fd.read()
    fd.close()
    cursor = conn.cursor()
    cursor.execute(sql_file)
    conn.commit()
    cursor.execute('select user_id, username, first_name, last_name, gender, status from dbo.[user_details] FOR JSON AUTO')
    for row in cursor:
        print(row)


exec_sql(file_sql)



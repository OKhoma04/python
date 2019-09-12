import sys
import pyodbc
import json

file_sql = sys.argv[1] #SQL file name - argument from cmd

#connection to MS SQl Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=EPUALVIW1270;'
                      'Database=TSQL2012;'
                      'Trusted_Connection=yes;')


#execution of SQL file, retrieveing and converting data to JSON format
def exec_sql(file_sql):
    fd=open(file_sql,'r')       #read SQL file
    sql_file = fd.read()
    fd.close()
    cursor = conn.cursor()
    cursor.execute(sql_file)    #execute scripts from SQL file(drop table if exist, create table and insert data)
    conn.commit()
    #retrieve data from created table(MS SQL Server) and convert to JSON format
    cursor.execute('select user_id, username, first_name, last_name, gender, status from dbo.[user_details] FOR JSON AUTO')
    results = cursor.fetchall()
    for row in results:         #print JSON in cmd
        print (row[0])

exec_sql(file_sql)



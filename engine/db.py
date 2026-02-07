import sqlite3

conn = sqlite3.connect('GG1.db')

cursor = conn.cursor()

# Create the sys_cmds table if it doesn't exist
query = "CREATE TABLE IF NOT EXISTS sys_cmds (id INTEGER PRIMARY KEY, name VARCHAR(255), path VARCHAR(255))"
cursor.execute(query)

# Insert data into the sys_cmds table
'''query = "INSERT INTO sys_cmds VALUES (null,'Microsoft PowerPoint', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE')"
cursor.execute(query)
conn.commit() # Commit the changes to the database
conn.close()# Close the connection when done
'''
# C:\Users\shubh\AppData\Local\Programs\Microsoft VS Code\\code.exe
# "C:\Program Files (x86)\VMware\VMware Workstation\vmware.exe"
#C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE
#"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
# "C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"

#to delete a record from the database
# conn = sqlite3.connect('GG1.db')  
# cursor = conn.cursor()
'''query = "DELETE FROM sys_cmds WHERE id='8'"
cursor.execute(query)
conn.commit()
conn.close()'''


# Create the web_cmds table if it doesn't exist
query = "CREATE TABLE IF NOT EXISTS web_cmds (id INTEGER PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))"
cursor.execute(query)

query = "INSERT INTO web_cmds VALUES (null,'wikipedia', 'https://wikipedia.org')"
cursor.execute(query)
conn.commit() # Commit the changes to the database
conn.close()


'''query = "DELETE FROM web_cmds WHERE id='1'"
cursor.execute(query)
conn.commit()
conn.close()
'''
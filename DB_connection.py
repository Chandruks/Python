import pyodbc
con = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-EOTU3DK\SQLEXPRESS;'
    'Database=Vidly;'
    'Trusted_Connection=yes;'
)
mycursor = con.cursor()
print(mycursor)

##insert Query
## Insert Values in table.
##mycursor.execute('''
##insert into register_page
##(name,email,password,conformpassword,dob,place) values
##('binoy','binoy@gmail.com','binoy','binoy','05/01/1987','gobi')
##''')


##Update Query
##Update values in table.
##mycursor.execute('''
##update register_page set place = 'ooty' where email='binoy@gmail.com'
##''')



##Delete Query
##delete row in table:
##mycursor.execute('''
##delete from register_page where email='hello@gmail.com'
##    ''')
##con.commit();
##
##

Display Query:
mycursor.execute('SELECT * FROM register_page')

for row in mycursor: print(row)
con.close()

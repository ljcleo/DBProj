import pyodbc
import xlrd

########## Connect with SQL Server ###########

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=film_db;UID=;PWD=')

# Create a cursor from the connection
cursor = cnxn.cursor()


########### Open the Excel ###########
data = xlrd.open_workbook('Film 4.xlsx')


################## Company ####################
table = data.sheets()[1]
sql = """
    INSERT INTO Company
    VALUES ('{:s}', '{:s}')
"""
for i in range(1, table.nrows):
    cursor.execute(sql.format(table.cell(i, 1).value, table.cell(i, 2).value))
cursor.commit()


################# Users ######################
table = data.sheets()[2]
sql = """
    INSERT INTO Users
    VALUES ('{:s}', '{:s}', {:d}, '{:s}', '{:s}', {:d})

"""
for i in range(1, table.nrows):
    cursor.execute(sql.format(str(int(table.cell(i, 0).value)), table.cell(i, 1).value, int(table.cell(i, 2).value),
                    table.cell(i, 3).value, str(int(table.cell(i, 4).value)), int(table.cell(i, 5).value)))
cursor.commit()


################# Film ##########################
table = data.sheets()[0]
sql = """
    INSERT INTO Film(Film_Chinese_Name, Film_Original_Name, Release_Date, Length, Company_ID, Storyline, Picture)
    VALUES ('{:s}', '{:s}', '{:s}', {:d}, {:d}, '{:s}', '{:s}')
"""
for i in range(1, table.nrows):
    name = '\'\''.join(table.cell(i, 2).value.strip().split('\''))
    date = xlrd.xldate_as_datetime(table.cell(i, 3).value, 'YYYY-MM-DD').strftime('%Y/%m/%d')
    storyline = '\'\''.join(table.cell(i, 6).value.split('\''))
    cursor.execute(sql.format(table.cell(i, 1).value, name, date, int(table.cell(i, 4).value),
                    int(table.cell(i, 5).value), storyline, table.cell(i, 9).value))
cursor.commit()


################# Comment ########################
table = data.sheets()[3]
sql = """
    INSERT INTO Comment
    VALUES ({:d}, '{:s}', {:f}, NULL)
"""
for i in range(1, table.nrows):
    cursor.execute(sql.format(int(table.cell(i, 0).value), str(int(table.cell(i, 1).value)), table.cell(i, 2).value))
cursor.commit()


################## Cast ###############################
table = data.sheets()[4]
sql = """
    INSERT INTO Film_Cast
    VALUES ('{:s}', '{:s}', '{:s}', '{:s}')
"""
for i in range(1, table.nrows):
    name = '\'\''.join(table.cell(i, 2).value.strip().split('\''))
    cursor.execute(sql.format(table.cell(i, 1).value, name, table.cell(i, 3).value, table.cell(i, 4).value))
cursor.commit()


###################### Play ##############################
table = data.sheets()[5]
sql = """
    INSERT INTO Play (Film_ID, Cast_ID)
    VALUES ({:d}, {:d})
"""
for i in range(1, table.nrows):
    cursor.execute(sql.format(int(table.cell(i, 0).value), int(table.cell(i, 1).value)))
cursor.commit()


###################### Directing ############################
table = data.sheets()[7]
sql = """
    INSERT INTO Directing
    VALUES ({:d}, {:d}, '{:s}')
"""
for i in range(1, table.nrows):
    cursor.execute(sql.format(int(table.cell(i, 0).value), int(table.cell(i, 1).value), table.cell(i, 2).value))
cursor.commit()


######################## Genre ###############################
table = data.sheets()[8]
sql = """
    INSERT INTO Genre
    VALUES('{:s}')
"""
for i in range(1, table.nrows):
    cursor.execute(sql.format(table.cell(i, 1).value))
cursor.commit()


##################### Film_Genre ###############################
table = data.sheets()[9]
sql = """
    INSERT INTO Film_Genre
    VALUES({:d}, {:d})
"""
for i in range(1, table.nrows):
    cursor.execute(sql.format(int(table.cell(i, 0).value), int(table.cell(i, 1).value)))
cursor.commit()


cursor.close()


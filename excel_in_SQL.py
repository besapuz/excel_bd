import xlrd

from connect_db import connect_db

book = xlrd.open_workbook("C:/имя файла")
sheet = book.sheet_by_name("pos книга в файле")

database = connect_db()

cursor = database.cursor()

query = """INSERT INTO имя таблицы (имя колонки) VALUES (%s, %s)"""

for r in range(1, sheet.nrows):
    Daily_Date = sheet.cell(r,0).value
    Days = sheet.cell(r,1).value

    values = (Daily_Date, Days)

    cursor.execute(query, values)

cursor.close()

database.commit()

database.close()
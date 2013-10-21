# -*- encoding: utf-8 -*-
import xlrd
import sqlite3

dbconnection = sqlite3.connect("database.db")
db = dbconnection.cursor()

#DB QUERIES
db.execute("DROP TABLE IF EXISTS schools")
db.execute("CREATE TABLE schools (nome text, district text, courses number)")
db.execute("DROP TABLE IF EXISTS courses")

#FILE OPS
openfile = xlrd.open_workbook("cna131fresultados.xls", encoding_override="utf-8")
openfile.sheet_names()
sheet = openfile.sheet_by_index(0)

for n, s in enumerate(openfile.sheets()):
	print "#XLRD#\nFile:%s Sheet:%s Columns:%d Rows:%d" % (s.name, n, s.ncols, s.nrows)

print "Teste: Açores, Heroísmo, Nutrição"
print sheet.row_values(4)
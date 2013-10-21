# -*- utf-8 -*-
import xlrd
import sqlite3

dbconnection = sqlite3.connect("database.db")
db = dbconnection.cursor()
db.execute("DROP TABLE IF EXISTS schools")
db.execute("CREATE TABLE schools (nome text, district text, courses number)")
db.execute("DROP TABLE IF EXISTS courses")
openfile = xlrd.open_workbook("cna131fresultados.xls")
openfile.sheet_names()
listindex = openfile.sheet_by_index(0)
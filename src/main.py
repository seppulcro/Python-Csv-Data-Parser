# -*- encoding: utf-8 -*-
import xlrd
import sqlite3

#FILE OPS
openfile = xlrd.open_workbook("cna131fresultados.xls", encoding_override="utf-8")
sheet = openfile.sheet_by_index(0)

nrows = sheet.nrows
ncols = sheet.ncols

conn = sqlite3.connect('trabalho.sqlite3')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS inscritos")

cursor.execute('''CREATE TABLE inscritos( cod_inst number, cod_curso number, nome_inst text(100), nome_curso text(100), grau text(2), vagas_inicial number, colocados number, last_grade number, vagas_final number)''')


for i in range(3, nrows - 2):
	cursor.execute('INSERT INTO inscritos VALUES (?,?,?,?,?,?,?,?,?)', sheet.row_values(i))

#everything = [];
#for x in range(3, nrows - 2):
#	row = []
#	for y in range(ncols):
#		row.append(sheet.cell_value(x,y))
#		pass
#	everything.append(row)
#	pass

#cursor.executemany('INSERT INTO inscritos VALUES (?,?,?,?,?,?,?,?,?)', everything)

conn.commit()
conn.close()
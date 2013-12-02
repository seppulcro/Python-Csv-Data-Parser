# -*- encoding: utf-8 -*-
import xlrd
import sqlite3

#FILE OPERATIONS
openfile = xlrd.open_workbook("cna131fresultados.xls", encoding_override="utf-8")
sheet = openfile.sheet_by_index(0)

#DATABASE OPERATIONS
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS inscritos")
cursor.execute('''CREATE TABLE inscritos(cod_inst text(10), cod_curso text(10), 
	nome_inst text(100), nome_curso text(100), grau text(10), 
	vagas_inicial number, colocados number, last_grade number, 
	vagas_final number)''')

#INSERT TO DATABASE.DB ALL ROW VALUES PER ROW STARTING FROM NO.3 AND ENDING IN THE N-2 ROW
for i in range(3, sheet.nrows - 2):
	cursor.execute('INSERT INTO inscritos VALUES (?,?,?,?,?,?,?,?,?)', sheet.row_values(i))

conn.commit()
conn.close()
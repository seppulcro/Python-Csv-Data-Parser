# -*- encoding: utf-8 -*-

"""plot_handler.py: Gets statistics and draws plots."""

"""
__author__      = "Marco Sacristão, Jorge Batista"
__copyright__   = "Copyright 2013, ESTIG - IPBeja"
__license__ 	= "GPL"
__version__		= "1.0.0"
__maintainer__	= "Jorge Batista"
__email__		= "dwjorgeb@gmail.com"
__status__		= "Development"
"""

import xlrd
import sqlite3
from ttk import *
from Tkinter import *
from data_manager import populate_database
from statistics_handler import *
from plot_handler import *

class Trab(Frame):

	districts = ["Aveiro", "Beja", "Braga", "Bragança", "Castelo Branco", "Coimbra", "Évora", "Faro", "Guarda", "Leiria", "Lisboa", "Portalegre", "Porto", "Santarém", "Setúbal", "Viana do Castelo", "Vila Real", "Viseu", "Angra do Heroísmo", "Funchal", "Horta", "Lamego", "Ponta Delgada"]

	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title("Trabalho Python")
		self.createNB()

	def createNB(self):
		nb = Notebook(self.parent, name='notes')
		nb.enable_traversal()
		nb.pack(fill=X)
		self.status = Label(self.parent, bd=1, relief=SUNKEN, anchor=W)
		self.status.pack(fill=X)
		self.updateStatus("Pronto")
		self.createTab1(nb, "criar BD")
		self.createTab2(nb, "estatísticas")
		self.createTab3(nb, "gráficos")
		self.createTab4(nb, "acerca")

	def createTab1(self, nb, name):
		frame = Frame(nb, name=name, width=300, height=280)
		msg = ["\n\n\nPara criar a base de dados clique no botão abaixo:\n\n\n"]
		lbl = Label(frame, wraplength='4i', justify=CENTER, anchor=N,text=''.join(msg))
		lbl.pack(fill=X)
		button = Button(frame, text="Criar BD", command=self.dbcreate)
		button.pack(fill=X)
		frame.pack(fill=X)
		nb.add(frame, text=name, underline=0, padding=2)


	def createTab2(self, nb, name):
		frame = Frame(nb, name=name, width=300, height=280)
		msg = ["\n\n\nPara criar as estatísticas clicar num dos botões abaixo:\n\n\n"]
		button1 = Button(frame, text ="Estatistica 1", command=self.stat1)
		button2 = Button(frame, text ="Estatistica 2", command=self.stat2)
		button3 = Button(frame, text ="Estatistica 3", command=self.stat3)
		button4 = Button(frame, text ="Estatistica 4", command=self.stat4)
		button5 = Button(frame, text ="Estatistica 5", command=self.stat5)
		button6 = Button(frame, text ="Estatistica 6", command=self.stat6)
		button1.grid(row=0, column=0, pady=(2,4))
		button2.grid(row=0, column=1, pady=(2,4))
		button3.grid(row=1, column=0, pady=(2,4))
		button4.grid(row=1, column=1, pady=(2,4))
		button5.grid(row=2, column=0, pady=(2,4))
		button6.grid(row=2, column=1, pady=(2,4))
		frame.rowconfigure(3, weight=1)
		frame.columnconfigure((0,1), weight=1, uniform=1)
		frame.pack(fill=X)
		nb.add(frame, text=name, underline=0, padding=2)

	def createTab3(self, nb, name):
		graphFrame = Frame(nb, name=name, width=300, height=280)
		optionsCombomBox = ['o numero de alunos colocados por instituicao', 'o numero de alunos colocados por distrito', 'a permilagem de alunos colocados por distrito','relacao de alunos colocados na instituicao/global','o numero de vagas por colocar por instituicao','o numero de vagas por colocar por distrito']
		self.comboBox = Combobox(graphFrame, state='readonly',values=optionsCombomBox)
		self.comboBox.pack(fill=X)
		self.graphlb = Listbox(graphFrame)
		self.graphlb.pack(fill=X)
		button = Button(graphFrame, text="Desenhar Gráfico", command=self.plot)
		button.pack(fill=X)
		self.comboBox.bind("<<ComboboxSelected>>", self.graphlist)
		graphFrame.pack(fill=X)
		nb.add(graphFrame, text=name, underline=0, padding=2)

	def createTab4(self, nb, name):
		frame = Frame(nb, name=name, width=300, height=280)
		msg = ["Trabalho de Linguagens de Programação 2013/2014\n\n\nAnálise de colocações no Ensino Superior\n\n\nPor: Jorge Batista && Marco Sacristão\n\n\n\n\n\n\n\n\n\n"]
		lbl = Label(frame, wraplength='4i', justify=CENTER, anchor=N,text=''.join(msg))
		lbl.pack(fill=X)
		frame.pack(fill=X)
		nb.add(frame, text=name, underline=0, padding=2)


	def graphlist(self, event):

		option = self.comboBox.get()

		if (option == 'o numero de alunos colocados por distrito') or (option == 'a permilagem de alunos colocados por distrito') or (option == 'o numero de vagas por colocar por distrito'):
			self.graphlb.delete(0, END)

			for dis in self.districts:
				self.graphlb.insert(END, dis)
		else:
			self.graphlb.delete(0, END)
			if (option == 'o numero de alunos colocados por instituicao'):
				institutes = getAllInstitutes("students_placed_by_institution.csv")
			elif (option == 'relacao de alunos colocados na instituicao/global'):
				institutes = getAllInstitutes("percentage_all_students_placed_by_institution.csv")
			else:
				institutes = getAllInstitutes("openings_remaining_by_institution.csv")
			for dis in institutes:
				self.graphlb.insert(END, dis)




	def dbcreate(self):

		self.updateStatus("A criar BD...")

		populate_database()

		self.updateStatus("BD Criada!")

	def plot(self):
		self.updateStatus("A desenhar gráfico...")
		selected = self.graphlb.get(self.graphlb.curselection())
		option = self.comboBox.get()
		if (option == 'o numero de alunos colocados por instituicao'):
			draw_students_placed_by_institution_graph(selected)
		elif (option == 'o numero de alunos colocados por distrito'):
			draw_students_placed_by_district_graph(selected)
		elif (option == 'a permilagem de alunos colocados por distrito'):
			draw_per_mil_students_placed_by_district_graph()
		elif (option == 'relacao de alunos colocados na instituicao/global'):
			draw_percentage_all_students_placed_by_institution_graph(selected)
		elif (option == 'o numero de vagas por colocar por instituicao'):
			draw_openings_remaining_by_institution_graph(selected)
		else:
			draw_openings_remaining_by_district_graph(selected)

		self.updateStatus("Gráfico desenhado!")

	def stat1(self):
		self.updateStatus("A gerar estatística..")
		students_placed_by_institution()
		self.updateStatus("Estatistica gerada!")

	def stat2(self):
		self.updateStatus("A gerar estatística..")
		students_placed_by_district()
		self.updateStatus("Estatistica gerada!")

	def stat3(self):
		self.updateStatus("A gerar estatística..")
		per_mil_students_placed_by_district()
		self.updateStatus("Estatistica gerada!")

	def stat4(self):
		self.updateStatus("A gerar estatística..")
		percentage_all_students_placed_by_institution()
		self.updateStatus("Estatistica gerada!")

	def stat5(self):
		self.updateStatus("A gerar estatística..")
		openings_remaining_by_institution()
		self.updateStatus("Estatistica gerada!")

	def stat6(self):
		self.updateStatus("A gerar estatística..")
		openings_remaining_by_district()
		self.updateStatus("Estatistica gerada!")

	def updateStatus(self, text):
		self.status.config(text=text)
		self.status.update_idletasks()

root = Tk()
root.geometry("330x285+300+300")
app = Trab(root)
root.mainloop()  
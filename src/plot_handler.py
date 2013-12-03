#!/usr/bin/python
# -*- coding: utf-8 -*-
"""plot_handler.py: Gets statistics and draws plots."""

"""
__author__      = "Marco Sacristão, Jorge Batista"
__copyright__   = "Copyright 2013, ESTIG - IPBeja"
__license__ 	= "GPL"
__version__		= "1.0.0"
__maintainer__	= "Marco Sacristão"
__email__		= "msacristao@gmail.com"
__status__		= "Development"
"""

import csv
from plotter import plot

def draw_students_placed_by_institution_graph(institute):
	filled = openFile("students_placed_by_institution.csv", institute)
	unfilled = openFile("openings_remaining_by_institution.csv", institute)
	
	lbls = ["Alunos colocados: " + str(filled), "Vagas livres: " + str(unfilled)]
	percs = [filled, unfilled]
	expls = [0.05, 0]

	plot("Numero de alunos colocados por instituicao:\n" + unicode(institute), lbls, percs, expls)


def draw_students_placed_by_district_graph(district):
	filled = openFile("students_placed_by_district.csv", district)
	unfilled = openFile("openings_remaining_by_district.csv", district)

	lbls = ["Alunos colocados: " + str(filled), "Vagas livres: " + str(unfilled)]
	percs = [filled, unfilled]
	expls = [0.05, 0]
	
	plot("Numero de alunos colocados por distrito:\n" + unicode(district), lbls, percs, expls)


def draw_openings_remaining_by_institution_graph(institute):
	filled = openFile("students_placed_by_institution.csv", institute)
	unfilled = openFile("openings_remaining_by_institution.csv", institute)

	lbls = ["Alunos colocados: " + str(filled), "Vagas livres: " + str(unfilled)]
	percs = [filled, unfilled]
	expls = [0, 0.05]
	
	plot("Numero de alunos colocados por instituicao:\n" + unicode(institute), lbls, percs, expls)


def draw_openings_remaining_by_district_graph(district):
	filled = openFile("students_placed_by_district.csv", district)
	unfilled = openFile("openings_remaining_by_district.csv", district)

	lbls = ["Alunos colocados: " + str(filled), "Vagas livres: " + str(unfilled)]
	percs = [filled, unfilled]
	expls = [0, 0.05]
	
	plot("Numero de alunos colocados por distrito:\n" + unicode(district), lbls, percs, expls)


def draw_per_mil_students_placed_by_district_graph():
	try:
		openfile = csv.reader(open('per_mil_students_placed_by_district.csv', "rb"))
	except:
		print "Can't open .csv file!"
	openfile = list(openfile)

	lbls = []
	percs = []
	expls = []

	for row in openfile:
		lbls.append(unicode(row[0].decode('utf-8')))
		percs.append(row[1])
		expls.append(0)

	plot("Permilagem de alunos colocados por distrito:", lbls, percs, expls)


def draw_percentage_all_students_placed_by_institution_graph(selected):
	perc = openFile("percentage_all_students_placed_by_institution.csv", selected)
	lbls = [selected, "Todos"]
	percs = [perc, 100 - float(perc)]
	expls = [0.1, 0]

	plot("Percentagem de alunos colocados por instituicao\nem relacao a todos os alunos colocados:", lbls, percs, expls)


def openFile(filename, rowname):
	try:
		openfile = csv.reader(open(filename, "rb"))
	except:
		print "Can't open .csv file!"
	openfile = list(openfile)
	for row in openfile:
		if row[0].decode('utf-8') == rowname:
			return row[1]

def getAllInstitutes(filename):
	try:
		openfile = csv.reader(open(filename, "rb"))
	except:
		print "Can't open .csv file!"
	openfile = list(openfile)
	institutes = []
	for row in openfile:
		institutes.append(row[0])

	return institutes

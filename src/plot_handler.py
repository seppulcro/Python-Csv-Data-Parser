#!/usr/bin/python
# -*- coding: utf-8 -*-
"""plot_handler.py: Gets statistics and draws plots."""

"""
__author__      = "Marco SacristÃ£o, Jorge Batista"
__copyright__   = "Copyright 2013, ESTIG - IPBeja"
__license__ 	= "GPL"
__version__		= "1.0.0"
__maintainer__	= "Marco Sacristão"
__email__		= "msacristao@gmail.com"
__status__		= "Development"
"""

import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pylab as p

def draw_students_placed_by_institution_graph():
	try:
		openfile = csv.reader(open("students_placed_by_institution.csv", "rb"))
	except:
		print "Can't open .csv file!"
	openfile = list(openfile)
	y_values = []
	x_values = []
	for row in openfile:
		y_values.append(int(row[1]))
		x_values.append(row[0])

	fig = p.figure()
	ax = fig.add_subplot(1,1,1)
	ind = range(len(y_values))
	plot = ax.bar(ind, y_values, facecolor='#00ffff',
		align='center', ecolor="black")
	ax.set_ylabel(u'Alunos colocados')
	ax.set_xlabel(u'Instituição')
	ax.set_title(u'Alunos colocados por Instituição', fontstyle='italic')
	ax.set_xticks(ind)
	ax.set_xticklabels(x_values)
	fig.autofmt_xdate()
	p.show()

draw_students_placed_by_institution_graph()
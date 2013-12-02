#!/usr/bin/python
# -*- coding: utf-8 -*-
"""statistics_handler.py: Queries database to perform statistics."""

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
from sqlalchemy import *

try:
	# Target database to be used
	DATABASE = create_engine('sqlite:///database.db', echo=True)
	METADATA = MetaData(DATABASE)
	# Target Table
	RESULTS = Table('Results', METADATA, autoload=True)
	print ("Successfully loaded Database('" + str(DATABASE) + "') and Table('" 
		+ str(RESULTS) + "')")
except:
	print ("Error: Could not import Database('" + str(DATABASE) +
	 "') or Table('" + str(RESULTS) + "')")


# Number of students placed by Institution
def students_placed_by_institution():

	# Name of the file to be handled by the current function
	file_name = "students_placed_by_institution.csv"

	# CSV File to contain statistics current function
	try:
		csvfile = csv.writer(open(file_name,"wb"),
			quoting=csv.QUOTE_ALL)
		print "Successfully opened file: " + str(file_name)
	except:
		print "Failed to open CSV file: " + str(file_name) + "!"

	# Run a query Selecting all elements
	query = RESULTS.select()
	run_query = query.execute()

	'''
	We use this variable to only count all the placed students 
	once per institute
	'''
	last_institution_code = 0 
	
	# For each row in the previous query
	for column in run_query:		
		new_institution_code = column[1] # column[1] being InstituteCode
		result_list = [] # Creates no list to which data will be appended
		if last_institution_code != new_institution_code:			
			result_list.append(column[3].encode('utf-8')) # Apnd InstitutionName
			'''
			The code below selects from the query all the entries that 
			match the given InstitutionCode and adds the students 
			that got placed in each row value until 
			another InstitutionCode is detected
			'''
			get_all_intiution_by_id = RESULTS.select(
				RESULTS.c.InstitutionCode.like(int(column[1])))
			getocurrencies = get_all_intiution_by_id.execute()
			placed_students = 0
			for x in getocurrencies:
				placed_students = placed_students + int(x[7]) # No.Placed in row
			result_list.append(placed_students) # Appends total placed students
			csvfile.writerow(result_list)
		last_institution_code = column[1]


def students_placed_by_district():	
	# Name of the file to be handled by the current function
	file_name = "students_placed_by_district.csv"

	# CSV File to contain statistics current function
	try:
		csvfile = csv.writer(open(file_name,"wb"),
			quoting=csv.QUOTE_ALL)
		print "Successfully opened file: " + str(file_name)
	except:
		print "Failed to open CSV file: " + str(file_name) + "!"

	# Run a query Selecting all elements
	query = RESULTS.select()
	run_query = query.execute()

	'''
	We use this variable to only count all the placed students 
	once per institute
	'''
	last_institution_code = ""
	
	# For each row in the previous query
	for column in run_query:		
		new_institution_code = column[10].encode('utf-8') # column[1] being InstituteCode
		print new_institution_code
		result_list = [] # Creates no list to which data will be appended
		if last_institution_code != new_institution_code:			
			result_list.append(column[10].encode('utf-8')) # Apnd InstitutionName
			'''
			The code below selects from the query all the entries that 
			match the given InstitutionCode and adds the students 
			that got placed in each row value until 
			another InstitutionCode is detected
			'''
			get_all_intitution_by_id = RESULTS.select(
				RESULTS.c.District.like(column[10]))
			order_by_asc = get_all_intitution_by_id.order_by(asc(RESULTS.c.District)).all()
			getocurrencies = order_by_asc.execute()

			placed_students = 0
			for x in getocurrencies:
				placed_students = placed_students + int(x[7]) # No.Placed in row
			result_list.append(placed_students) # Appends total placed students
			csvfile.writerow(result_list)
		last_institution_code = column[10].encode('utf-8')
		print last_institution_code


# Debug
students_placed_by_institution()
students_placed_by_district()



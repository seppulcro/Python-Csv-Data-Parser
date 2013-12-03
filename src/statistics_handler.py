#!/usr/bin/python
# -*- coding: utf-8 -*-
"""statistics_handler.py: Queries database to perform statistics."""

"""
__author__      = "Marco Sacristão, Jorge Batista"
__copyright__   = "Copyright 2013, ESTIG - IPBeja"
__license__ 	= "GPL"
__version__		= "1.1.0"
__maintainer__	= "Marco Sacristão"
__email__		= "msacristao@gmail.com"
__status__		= "Development"
"""

import csv
from sqlalchemy import *

try:
	# Target database to be used
	DATABASE = create_engine('sqlite:///database.db', echo=False)
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
		result_list = [] # Creates a list to which data will be appended
		if last_institution_code != new_institution_code:			
			result_list.append(column[3].encode('utf-8')) # Apnd InstitutionName
			'''
			The code below selects from the query all the entries that 
			match the given InstitutionCode and adds the students 
			that got placed in each row value until 
			another InstitutionCode is detected
			'''
			get_all_institution_by_id = RESULTS.select(
				RESULTS.c.InstitutionCode.like(int(column[1])))
			getocurrencies = get_all_institution_by_id.execute()
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

	'''
	Run a query Selecting all elements and ordering it by District Ascending
	'''
	query = RESULTS.select()
	order_by_asc = query.order_by(asc(RESULTS.c.District))
	run_query = order_by_asc.execute()

	'''
	We use this variable to only count all the placed students 
	once per institute
	'''
	last_district = ""
	
	# For each row in the previous query
	for column in run_query:
		'''
		column[10] being District
		'''	
		new_institution_code = column[10].encode('utf-8')
		result_list = [] # Creates no list to which data will be appended
		if last_district != new_institution_code:	
			'''
			Append InstitutionName
			'''		
			result_list.append(column[10].encode('utf-8'))
			'''
			The code below selects from the query all the entries that 
			match the given District and adds the students 
			that got placed in each row value until 
			another District is detected
			'''
			get_all_intitution_by_id = RESULTS.select(
				RESULTS.c.District.like(column[10]))
			getocurrencies = get_all_intitution_by_id.execute()

			placed_students = 0
			for x in getocurrencies:
				placed_students = placed_students + int(x[7]) # No.Placed in row
			result_list.append(placed_students) # Appends total placed students
			csvfile.writerow(result_list)
		last_district = column[10].encode('utf-8')

# TODO: Optimize code
def per_mil_students_placed_by_district():
	# Name of the file to be handled by the current function
	file_name = "per_mil_students_placed_by_district.csv"

	# CSV File to contain statistics current function
	try:
		csvfile = csv.writer(open(file_name,"wb"),
			quoting=csv.QUOTE_ALL)
		print "Successfully opened file: " + str(file_name)
	except:
		print "Failed to open CSV file: " + str(file_name) + "!"

	'''
	Run a query Selecting all elements and ordering it by District Ascending
	'''
	query = RESULTS.select()
	order_by_asc = query.order_by(asc(RESULTS.c.District))
	run_query = order_by_asc.execute()

	'''
	We use this variable to only count all the placed students 
	once per institute
	'''
	last_district = ""
	
	# For each row in the previous query
	for column in run_query:
		'''
		column[10] being District
		'''	
		new_institution_code = column[10].encode('utf-8')
		result_list = [] # Creates no list to which data will be appended
		if last_district != new_institution_code:	
			'''
			Append InstitutionName
			'''		
			result_list.append(column[10].encode('utf-8'))
			'''
			The code below selects from the query all the entries that 
			match the given District and adds the students 
			that got placed in each row value until 
			another District is detected
			'''
			get_all_intitution_by_id = RESULTS.select(
				RESULTS.c.District.like(column[10]))
			getocurrencies = get_all_intitution_by_id.execute()

			placed_students = 0
			for x in getocurrencies:
				placed_students = placed_students + int(x[7]) # No.Placed in row
			'''
			Appends total placed students * 0.001 (Per mil)
			Formatting to float only 3 decimals
			'''
			result_list.append("{0:.3f}".format(placed_students*0.001))
			csvfile.writerow(result_list)
		last_district = column[10].encode('utf-8')

def get_all_placed():
	# Run a query Selecting all elements
	query = RESULTS.select()
	run_query = query.execute()
	total_placed = 0.0
	for i in run_query:
		total_placed = total_placed + i[7]

	return total_placed



def percentage_all_students_placed_by_institution():
	# Name of the file to be handled by the current function
	file_name = "percentage_all_students_placed_by_institution.csv"

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
		result_list = [] # Creates a list to which data will be appended
		if last_institution_code != new_institution_code:			
			result_list.append(column[3].encode('utf-8')) # Apnd InstitutionName
			'''
			The code below selects from the query all the entries that 
			match the given InstitutionCode and adds the students 
			that got placed in each row value until 
			another InstitutionCode is detected
			'''
			get_all_institution_by_id = RESULTS.select(
				RESULTS.c.InstitutionCode.like(int(column[1])))
			getocurrencies = get_all_institution_by_id.execute()
			placed_students = 0
			for x in getocurrencies:
				placed_students = placed_students + int(x[7]) # No.Placed in row
			'''
			Appends total placed students * 0.01 (Percentage)
			Formatting to float only 2 decimals
			'''
			# Gets all placed students with get_all_placed()
			total_placed = get_all_placed()
			# Calculates the percentage of placed students
			percentage_placed = (placed_students*100)/total_placed
			result_list.append("{0:.2f}".format(percentage_placed))
			csvfile.writerow(result_list)
		last_institution_code = column[1]

def openings_remaining_by_district():
	# Name of the file to be handled by the current function
	file_name = "openings_remaining_by_district.csv"

	# CSV File to contain statistics current function
	try:
		csvfile = csv.writer(open(file_name,"wb"),
			quoting=csv.QUOTE_ALL)
		print "Successfully opened file: " + str(file_name)
	except:
		print "Failed to open CSV file: " + str(file_name) + "!"

	'''
	Run a query Selecting all elements and ordering it by District Ascending
	'''
	query = RESULTS.select()
	order_by_asc = query.order_by(asc(RESULTS.c.District))
	run_query = order_by_asc.execute()

	'''
	We use this variable to only count all the openings remaining
	once per District
	'''
	last_district = ""
	
	# For each row in the previous query
	for column in run_query:
		'''
		column[10] being District
		'''	
		new_institution_code = column[10].encode('utf-8')
		result_list = [] # Creates no list to which data will be appended
		if last_district != new_institution_code:	
			'''
			Append InstitutionName
			'''		
			result_list.append(column[10].encode('utf-8'))
			'''
			The code below selects from the query all the entries that 
			match the given District and adds the openings
			remaining in each row value until 
			another District is detected
			'''
			get_all_intitution_by_id = RESULTS.select(
				RESULTS.c.District.like(column[10]))
			getocurrencies = get_all_intitution_by_id.execute()

			remaining_openings = 0
			for x in getocurrencies:
				# No.Openings Remaining in row
				remaining_openings = remaining_openings + int(x[9])
			# Appends total remaining openings
			result_list.append(remaining_openings) 
			csvfile.writerow(result_list)
		last_district = column[10].encode('utf-8')


def openings_remaining_by_institution():
	
	# Name of the file to be handled by the current function
	file_name = "openings_remaining_by_institution.csv"

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
	We use this variable to only count all the openings remaining
	once per institute
	'''
	last_institution_code = 0 
	
	# For each row in the previous query
	for column in run_query:		
		new_institution_code = column[1] # column[1] being InstituteCode
		result_list = [] # Creates a list to which data will be appended
		if last_institution_code != new_institution_code:			
			result_list.append(column[3].encode('utf-8')) # Apnd InstitutionName
			'''
			The code below selects from the query all the entries that 
			match the given InstitutionCode and adds the openings remaining 
			in each row value until 
			another InstitutionCode is detected
			'''
			get_all_institution_by_id = RESULTS.select(
				RESULTS.c.InstitutionCode.like(int(column[1])))
			getocurrencies = get_all_institution_by_id.execute()
			openings_remaining = 0
			for x in getocurrencies:
				# No.Placed in row
				openings_remaining = openings_remaining + int(x[9])
			# Appends total of openings remaining
			result_list.append(openings_remaining)
			csvfile.writerow(result_list)
		last_institution_code = column[1]

# Debug!
students_placed_by_institution()
students_placed_by_district()
per_mil_students_placed_by_district()
percentage_all_students_placed_by_institution()
openings_remaining_by_district()
openings_remaining_by_institution()
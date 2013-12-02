#!/usr/bin/python
# -*- coding: utf-8 -*-
"""create_database.py: Description of what foobar does."""

"""
__author__      = "Marco Sacristão, Jorge Batista"
__copyright__   = "Copyright 2013, ESTIG - IPBeja"
__license__ 	= "GPL"
__version__		= "1.0.1"
__maintainer__	= "Marco Sacristão"
__email__		= "msacristao@gmail.com"
__status__		= "Development"
"""

import sqlite3
import xlrd
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine

# File's name to open using XLRD
FILE_NAME 		= "cna131fresultados.xls"
# Sheet number that contains the information
SHEET_NUMBER 	= 0

# Open FILE_NAME forcing utf-8 encoding and set current sheet as 0
try:
	OPEN_FILE = xlrd.open_workbook(FILE_NAME, encoding_override="utf-8")
	SHEET = OPEN_FILE.sheet_by_index(SHEET_NUMBER)
	"""
	'Row offsets' are used to know from what interval we should start
	extracting data from, this way we can exclude any rows that do not contain
	information that should be extracted. This way we can guarantee that 
	changes	to the row structure can be easily altered below to read 
	from a different interval.
	"""
	ROW_INTERVAL_START 		= 3
	ROW_INTERVAL_END 		= SHEET.nrows - 2 #SHEET.nrows = Total rows in file.
except:
	print FILE_NAME + " not found in current directory!"


# SQAlchemy defining declarative base class, connection and debugging.
try:
	BASE = declarative_base()
	DATABASE = create_engine('sqlite:///:memory:', echo=True)
	print "Running SQLAchemy version... " + sqlalchemy.__version__
	print "Successfully allocated Database: " + str(DATABASE) + "!"
except:
	print "Failed to create the SQLAlchemy database!"


# Class to which we map the SQLAlchemy table we are going to use.
class results(BASE):
	"""
	Creates table to be filled with information from the .XLS file
	"""
	try:
		__tablename__ = "Results"
		id 					= Column(Integer, primary_key=True)
		InstitutionCode 	= Column(Integer(4))
		CourseCode 			= Column(Integer(4))
		InstiutionName 		= Column(String(100))
		CourseName 			= Column(String(100))
		Degree 				= Column(String(2))
		InitialOpenings		= Column(Integer(2))
		Placed				= Column(Integer(3))
		LastApplicantGrade	= Column(Float(4))
		RemainingOpenings	= Column(Integer(4))
		print "Successfully setup table: '" + __tablename__ + "'!"
	except:
		print "Failed to setup SQAlchemy database's table!"


# Function which populates the generated Database's table
# TODO(Jorge): utilize this function
def populate_database():
	# Drop the existing database
	try:
		BASE.metadata.drop_all(DATABASE) # Delete table if it exists
	except:
		print "Warning: Could not delete the Database!"

	# Create the database
	try:
		BASE.metadata.create_all(DATABASE) # Create the Database
	except:
		print "Error: Could not create the Database!"

	# Populate the Database's table
	try:
		data_number = 0
		for i in range(ROW_INTERVAL_START, ROW_INTERVAL_END):
			DATABASE.execute(results.__table__.insert()),
			[{
			"InstitutionCode": SHEET.row_values(i),
			"CourseCode": SHEET.row_values(i),
			"InstiutionName": SHEET.row_values(i),
			"CourseName": SHEET.row_values(i),
			"Degree": SHEET.row_values(i),
			"InitialOpenings": SHEET.row_values(i),
			"Placed": SHEET.row_values(i),
			"LastApplicantGrade": SHEET.row_values(i),
			"RemainingOpenings": SHEET.row_values(i),
			}]
			datanumber=datanumber+1
		print "Inserted " + data_number + " values!"
	except:
		print "Error: Could not populate the Database's table."
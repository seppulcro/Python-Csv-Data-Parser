#!/usr/bin/python
# -*- coding: utf-8 -*-
"""create_database.py: Module used for creating and populating SQLAlchemy
Database."""

"""
__author__      = "Marco Sacristão, Jorge Batista"
__copyright__   = "Copyright 2013, ESTIG - IPBeja"
__license__ 	= "GPL"
__version__		= "1.0.1"
__maintainer__	= "Marco Sacristão"
__email__		= "msacristao@gmail.com"
__status__		= "Development"
"""

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
	# populate_database() needs to be ran in order to Create Database.
	BASE = declarative_base()
	DATABASE = create_engine('sqlite:///database.db', echo=True)
	DB_SESSION = scoped_session(sessionmaker())
	DB_SESSION.configure(bind=DATABASE, autoflush=False, expire_on_commit=False)
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
		CourseCode 			= Column(String(4))
		InstitutionName 	= Column(String(100))
		CourseName 			= Column(String(100))
		Degree 				= Column(String(2))
		InitialOpenings		= Column(Integer(2))
		Placed				= Column(Integer(3))
		LastApplicantGrade	= Column(String(4))
		RemainingOpenings	= Column(Integer(4))
		District			= Column(String(10))
		print "Successfully setup table: '" + __tablename__ + "'!"
	except:
		print "Failed to setup SQAlchemy database's table!"


# Function which populates the generated Database's table
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

	# Insert values into Table
	try:
		DATABASE.execute(results.__table__.insert(),
		[{
		"InstitutionCode": SHEET.cell(i,0).value,
		"CourseCode": SHEET.cell(i,1).value,
		"InstitutionName": SHEET.cell(i,2).value,
		"CourseName": SHEET.cell(i,3).value,
		"Degree": SHEET.cell(i,4).value,
		"InitialOpenings": SHEET.cell(i,5).value,
		"Placed": SHEET.cell(i,6).value,
		"LastApplicantGrade": SHEET.cell(i,7).value,
		"RemainingOpenings": SHEET.cell(i,8).value,
		"District": check_district(SHEET.cell(i,2).value)
		} for i in range(ROW_INTERVAL_START, ROW_INTERVAL_END)])
		print "Successfully inserted values into table!"
	except:
		print "Error: Could not populate database!"

def check_district(institution_name):
	# List of districts that exist in Portugal
	available_districts = ['Lisboa','Porto',u'Setúbal','Braga','Aveiro',
	'Leiria',u'Santarém','Faro','Coimbra','Viseu','Madeira',u'Açores',
	'Viana do Castelo','Vila Real','Castelo Branco', u'Évora','Guarda','Beja',
	u'Bragança','Portalegre']

	'''
	Checks the Institution name for any available District, if it finds one it 
	return the district that was found in the name and set it as the 
	Institution's district
	'''
	for i in range(0,len(available_districts)):
		if(available_districts[i] in institution_name):
			return available_districts[i]

	# List of regions to be associated with a district that exists in Portugal
	unset_districts = ['Algarve','Beira Interior','Minho',
	u'Trás-os-Montes e Alto Douro',u'Cávado e do Ave','Tomar',
	u'Náutica Infante D. Henrique','Estoril']

	'''
	After checking the Institution's name and no available district is found 
	within, we should convert the Region that we find in the name to an 
	available district
	'''
	for i in range(0, len(unset_districts)):
		if(unset_districts[i] in institution_name):
			if(i==0): 	# Region Algarve found
				return available_districts[7] 	# Return Faro
			if(i==1): 	# Region Beira Interior(Covilhã) found
				return available_districts[14]	 # Return Castelo Branco
			if(i==2): 	# Region Minho found
				return available_districts[3] 	# Return Braga
			if(i==3):	# Region Trás-os-Montes e Alto Douro found
				return available_districts[13]	# Return Vila Real
			if(i==4): 	# Region Cávado e do Ave found
				return available_districts[3] 	# Return Braga
			if(i==5): 	# Region Tomar found
				return available_districts[6]	# Return Santarém
			if(i==6): 	# Region Paço de Arcos -> Oeiras
				return available_districts[0]	# Return Lisboa
			if(i==7):	# Region Estoril -> Cascais
				return available_districts[0]	# Return Lisboa
	return "Unknown District"

# Execute code if needed by using populate_database()
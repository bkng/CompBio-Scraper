#!/usr/bin/python

# Bennett Ng, Niraj Amalkanti
# BioE 231
# Project 1: web db scraper

# BioPython
import Bio
from Bio import Entrez

# interface object
import Entry

class Scraper:

	def __init__(self, email):
		Entrez.email = email

	def getVirusEntry(self, id):
		pass
	
	def getGenomeEntry(self, gbIdentifier):
		handle = Entrez.esummary(db="genome", id=gbIdentifier)
		record = Entrez.read(handle)
		name = record[0]["Organism_Name"]
		description = record[0]["DefLine"]
		value = record[0]["Number_of_Chromosomes"]
		
		# TODO
		picture_url = ""
		
		return Entry.Entry(name, description, Entry.GENOME, value, picture_url)
	

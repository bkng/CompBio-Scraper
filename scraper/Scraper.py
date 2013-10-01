#!/usr/bin/python

# Bennett Ng, Niraj Amalkanti
# BioE 231
# Project 1: web db scraper
#
# Some code adapted from:
# stackoverflow.com/questions/11242967/python-search-with-image-google-images 

# interface object
import Entry

# BioPython
import Bio
from Bio import Entrez
from Bio import ExPASy
from Bio import SwissProt

# Google Image Search
import os
import sys
import time
from urllib import FancyURLopener
import urllib2
import simplejson

class Scraper:

	def __init__(self, email):
		Entrez.email = email
	
	# get the URL of the first image found on Google Image Search
	def getImageUrl(self, query):
		# execute query
		query = query.replace(' ','%20')
		version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
		url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q=' + query + '&start=0' + '&userip=MyIP')
		request = urllib2.Request(url, None, {'Referer': 'testing'})
		response = urllib2.urlopen(request)

		# parse results JSON
		results = simplejson.load(response)
		data = results['responseData']
		dataInfo = data['results']

		# extract and return first URL
		return dataInfo[0]["unescapedUrl"]
	
	# get a GenomeEntry for a specific GenBank identifier
	def getGenomeEntry(self, gbIdentifier):
		# issue request
		handle = Entrez.esummary(db="genome", id=gbIdentifier)
		record = Entrez.read(handle)
		
		# parse data
		name = record[0]["Organism_Name"]
		description = record[0]["DefLine"]
		value = record[0]["Number_of_Chromosomes"]
		picture_url = self.getImageUrl(name)
		
		return Entry.Entry(name, description, Entry.GENOME, value, picture_url)
			
	def getVirusEntry(self, id):
		pass
	

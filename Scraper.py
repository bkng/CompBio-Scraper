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
	
	# get image URLs from Google Image Search
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
		if data == None:
                        return ""
		dataInfo = data['results']

		# extract and return first URL
		return [row["unescapedUrl"] for row in dataInfo]
	
	# get an Entry for a specific genome db identifier
	def getEntry(self, gbIdentifier, entry_type):
		# fetch genome data
		gHandle = Entrez.esummary(db="genome", id=gbIdentifier)
		gRecord = Entrez.read(gHandle)
		
		# lookup linked nucleotide data
		linkHandle = Entrez.elink(db="nucleotide", dbfrom="genome", id=gbIdentifier)
		linkRecord = Entrez.read(linkHandle)
		try:
			ntId = linkRecord[0]["LinkSetDb"][0]["Link"][0]["Id"]
		except IndexError:
			base_count = 0;
		else:
			ntHandle = Entrez.esummary(db="nucleotide", id=ntId, rettype="xml")
			ntRecord = Entrez.read(ntHandle)		
			base_count = ntRecord[0]["Length"]
		
		# construct Entry	
		name = gRecord[0]["Organism_Name"]
		description = gRecord[0]["DefLine"]
		chromosome_count = gRecord[0]["Number_of_Chromosomes"]
		picture_url = self.getImageUrl(name)
		
		return Entry.Entry(name, description, entry_type, chromosome_count, base_count, picture_url)
	
	# get num Virus Entries, by querying for "virus" genomes
	def getVirusEntries(self, num, offset):
		handle = Entrez.esearch(db="genome", term="virus", field="title", retmax=num, retstart=offset)
		record = Entrez.read(handle)		
		return [self.getEntry(id, Entry.VIRUS) for id in record["IdList"]]
	
	# get num Genome Entries
	def getGenomeEntries(self, num, offset):		
		handle = Entrez.esearch(db="genome", term="has chromosome", field="properties", retmax=num, retstart=offset)
		record = Entrez.read(handle)		
		return [self.getEntry(id, Entry.GENOME) for id in record["IdList"]]

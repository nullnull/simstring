#!/usr/bin/env python
# -*- coding:utf-8 -*-

SIMSTRING_NAME = "SimString"
SIMSTRING_MAJOR_VERSION = "1"
SIMSTRING_MINOR_VERSION = "0"
SIMSTRING_COPYRIGHT = "Copyright (c) 2012 Katsuma Narisawa, Naoaki Okazaki"

import pymongo, math, sys, time
from collections import defaultdict
from optparse import OptionParser
import build_stringsdb, build_freqdb, search

def show_version():
	print SIMSTRING_NAME,SIMSTRING_MAJOR_VERSION+"."+SIMSTRING_MINOR_VERSION,SIMSTRING_COPYRIGHT+"\n"		

if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option("-v","--version", action="store_true", dest = "version", help = "help version") 
	parser.add_option("-b","--build", action="store_true", dest="build", help="build a database for strings read from STDIN")
	parser.add_option("-c","--connection", action="store", dest="CON", default="", help="specify a mongo connection") 
	parser.add_option("-d","--database", action="store", type="str", dest="DB", default="simstring", help="specify a database name")
	parser.add_option("-u","--unicode", action="store_true", dest="unicode", help="use Unicode (wchar_t) for representing characters")
	parser.add_option("-n","--ngram", action="store", type="int", dest="N", default=3, help="specify the unit of n-grams (DEFAULT=3)")
	parser.add_option("-m","--mark", action="store_true", dest="mark", help="include marks for begins and ends of strings")
	parser.add_option("-s","--similarity", action="store", type="str", dest="SIM", default="cosine" , help="""specify a similarity measure (DEFAULT='cosine'):\n
		exact                 exact match\n
		dice                  dice coefficient\n
		cosine                cosine coefficient\n 
		jaccard               jaccard coefficient\n
		overlap               overlap coefficient""")
	parser.add_option("-t","--threshold", action="store", type="float", dest="TH", default=0.7, help="specify the threshold (DEFAULT=0.7)") 
	parser.add_option("-e","--echo-back", action="store_true", dest="echoback", help="echo back query strings to the output") 
	parser.add_option("-q","--quiet", action="store_true", dest="quiet", help="suppress supplemental information from the output") 
	parser.add_option("-p","--benchmark", action="store_true", dest="benchmark", help="show benchmark result (retrieved strings are suppressed)")
	parser.add_option("-f","--feature", action="store_true", dest="feature", help="use original feature")
	options, args = parser.parse_args()
	
	if options.version :
		show_version()
		
	elif options.build :
		#build termsdb and termfreqdb
		starttime = time.clock()
		if not options.quiet : show_version()
		build_stringsdb.build_stringsdb(options.CON, options.DB, options.unicode, options.N, options.mark, options.feature)
		build_freqdb.build_freqdb(options.CON, options.DB)
		print "Seconds required:", time.clock() - starttime
		
	else :
		#search similar strings
		while(1):
			#set input
			sentence = u""
			features = ""
			if options.feature :
				sentence = raw_input("please input sentence : ")
				features = raw_input("please input features : ")
			else :
				sentence = raw_input("")
			if options.unicode :
				sentence = unicode(sentence)
				features = unicode(features)
				
			#output search result
			starttime = time.clock()
			if options.echoback : print sentence
			similar_stringss = search.search(options.CON, options.DB, options.TH, options.SIM, sentence, options.N, options.feature, features)
			for similar_strings in similar_stringss :
				print "\t",similar_strings
				
			if not options.quiet : print len(similar_stringss),"strings retrieved",
			if not options.quiet : print "("+str(time.clock()-starttime)+" sec)"

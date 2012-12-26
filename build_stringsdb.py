#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymongo, sys
	
def create_ngrams(strings,n):
	ret = []
	#strings = " "*(n-1) + strings + " "*(n-1) #count strings starts or ends
	for i in xrange(0, len(strings)-(n-1)) : 
		ret.append(strings[i:i+n])
	return ret

def build_stringsdb(con_name, db_name, is_unicode, N, is_mark, is_feature) :
	#setting output DB
	if(con_name!="") : conn = pymongo.Connection(con_name)
	else : conn = pymongo.Connection()
	db = conn[db_name]
	coll = db["strings"]
	coll.remove()
	#setting input
	fin = sys.stdin
	
	print "Constructing the database"
	print "Connection name:",con_name
	print "Database name:",db_name
	if is_feature : print "use original feature"
	else : print "N-gram length:",N
	print "Begin/end marks:",is_mark
	if is_unicode : print "Char type: w (4)"
	else : print "Char type: c (1)"
	insert_items = []
	cnt=1
	while(1) :
		line = fin.readline()
		if(line=="") : break;
		if(not is_mark) : line = line.strip()
		if(is_unicode) : line = unicode(line)
		strings = line
		if is_feature :
			line = fin.readline()
			terms = line.strip().split("\t")
		else :
			terms = create_ngrams(line, N)
		terms_size = len(terms)
		id = cnt
		insert_items.append({"strings":strings, "id":id, "terms":terms, "terms_size":len(terms)})
		if cnt%10000 == 0 :
			coll.insert(insert_items)
			insert_items = []
			print cnt
		cnt+=1
	if not len(insert_items) == 0 :
		coll.insert(insert_items)
	coll.ensure_index("terms")
	coll.ensure_index("id")
	conn.disconnect()
	print "\nFlushing the database\n"
	print "Total number of strings:",cnt
	

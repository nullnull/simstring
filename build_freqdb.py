#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymongo
from collections import defaultdict

def build_freqdb(con_name, db_name) :
	#set up freqDB(output)
	if(con_name!="") : conn = pymongo.Connection(con_name)
	else : conn = pymongo.Connection()
	db = conn[db_name]
	coll_out = db["freq"]
	coll_out.remove()
	
	#set up sentence-termDB(input)
	coll_in = db["strings"]
	all = coll_in.count()
	cnt = 0;
	insert_items = defaultdict(int) 
	
	for data in coll_in.find() :
		terms = data["terms"]
		for term in terms :
			insert_items[term] += 1
		if(cnt%10000==0) : 
			coll_out.ensure_index("term")
			for key,value in insert_items.items() :
				coll_out.update( {"term":key }, { "$inc": { "freq":value } }, True )
			insert_items = defaultdict(int)
	for key,value in insert_items.items() :
		coll_out.update( {"term":key }, { "$inc": { "freq":value } }, True )
	coll_out.ensure_index("term")
	conn.disconnect()

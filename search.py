#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
simstringのポイント
1. 式変換より特徴集合Yのサイズの範囲が定まる。（範囲外はチェックする必要がない）
2. 式変換より類似度が閾値以上となるときの最小オーバーラップ数がτで求められる。（cosineのとき、τ = [α√|X||Y|]
　 すなわち、最小オーバーラップ数に達する見込みのないものは、枝刈りしていける (CPMerge)
4. 更に、重複しにくい特徴集合Yの特徴から、オーバーラップをチェックしていけば、効率よく枝刈りが行える (CPMerge)
"""

import pymongo, math
from collections import defaultdict
import build_stringsdb

def set_Y_range(measure, threshold, terms_size) :
	if measure == "cosine" :
		minY = int(math.ceil(threshold*threshold*terms_size))
		maxY = int(terms_size/(threshold*threshold))
	elif measure == "dice" :
		minY = int(math.ceil(threshold/(2.0-threshold)*terms_size))
		maxY = int((2-threshold)/threshold*terms_size)
	elif measure == "jaccard" :
		minY = int(math.ceil(threshold * terms_size))
		maxY = int(terms_size / threshold)
	elif measure == "overlap" :
		minY = 1
		maxY = 99999999999
	else : #exact
		minY = terms_size
		maxY = terms_size
	
	return minY, maxY
				
def calc_similarity(measure, x, y, N) :
	X = build_stringsdb.create_ngrams(x, N)
	Y = build_stringsdb.create_ngrams(y, N)
	similarity = -1
	if measure == "cosine" : similarity = len(set(X)&set(Y)) / math.sqrt(len(X) * len(Y)), set(X)&set(Y)
	print x,y,similarity


def min_overlap(measure, terms_size, size_Y, threshold) :
	if measure == "cosine" : return int(math.ceil(threshold*math.sqrt(terms_size*size_Y)))
	elif measure == "dice" : return int(math.ceil(0.5 * threshold * (size_Y + terms_size) ) )
	elif measure == "jaccard" : return int(math.ceil( threshold * (size_Y + terms_size) / (1 + threshold ) ) )
	elif measure == "overlap" : return int(math.ceil( threshold * min(size_Y, terms_size) ) )
	else : return size_Y #exact
	

def cpmerge(terms_freq, minY, maxY, threshold, measure):
	global conn,db,coll,coll_freq
	matched_ids = []
	size_X = len(terms_freq)
	
	for size_Y in xrange(minY, maxY+1) : #範囲内のYのみ探索する
		candidate_num_overlap = defaultdict(int)
		candidate_terms = {}
	
		#setup tau
		tau = min_overlap(measure, size_X, size_Y, threshold)
		
		#性質1 要素数がkの集合Xと，要素数が任意の集合Yがある．要素数が(k−τ+1)となる任意の部分集合Z⊆Xを考える．もし，|X ∩ Y | ≥ τ ならば，Z ∩ Y ≠ ϕ である.
		#これより、terms_freq[0:k-τ+1]を少なくとも1つもつyを探索する。ここで転置インデックスを用いる（1つ1つsentencesを探索すると遅い）
		for i in xrange(0, size_X-tau+1):
			term = terms_freq[i][1]
			for data in coll.find({"terms":term, "terms_size":size_Y}):
				candidate_num_overlap[data["_id"]] += 1
				candidate_terms[data["_id"]] = data["terms"]
		
		#Xの残りの要素について探索。最小オーバーラップ数に達する見込みがない場合は、枝刈りする
		for id, num_overlap in candidate_num_overlap.items() :
			for i in xrange(size_X-tau+1, size_X) :
				term = terms_freq[i][1]
				if term in candidate_terms[id]:
					num_overlap+=1
					if tau <= num_overlap :
						matched_ids.append(id)
						break
				else :
					if num_overlap+(size_X-i-1) < tau : break
					
	return matched_ids


def search(con_name, db_name, threshold, measure, sentence, N, is_feature, features) :
	#setup stringsDB and freqDB
	global conn, db, coll
	if(con_name!="") : conn = pymongo.Connection(con_name)
	else : conn = pymongo.Connection()
	db = conn[db_name]
	coll = db["strings"]
	coll_freq = db["freq"]
	
	#setupt terms
	if not is_feature :
		terms = build_stringsdb.create_ngrams(sentence, N)
	else : 
		terms = features.strip().split("\t")
	terms_size = len(terms)
	
	#sort terms by frequency
	terms_freq = []
	for term in terms :
		d = coll_freq.find_one({"term":term})
		if not d : 
			terms_freq.append([0, term])
		else :
			terms_freq.append([d["freq"], term])
	terms_freq.sort(key = lambda x : x[0])
	
	#setupt measure method
	minY, maxY = set_Y_range(measure, threshold, terms_size)
	
	#search matched ids
	matched_ids = cpmerge(terms_freq, minY, maxY, threshold, measure)
	
	#translate ids to stringss
	similar_stringss = []
	for matched_id in matched_ids :
		for data in coll.find({"_id":matched_id}) :
			similar_stringss.append(data["strings"])
	conn.disconnect()
	
	return similar_stringss
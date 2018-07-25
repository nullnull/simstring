# Simple benchmark script when searching similar strings by using elasticsearch instead of SimString.
# Since Elasticsearch uses Apache Lucene, TF/IDF based searching algorithm, the purpose for searching text will be different from this library.

from elasticsearch import Elasticsearch
from benchmarker import Benchmarker

es = Elasticsearch('http://localhost:9200/')

SEARCH_COUNT_LIMIT = 10**4
index = 'simstring'
type = 'sample'
path = './dev/data/company_names.txt'
number_of_lines = len(open(path).readlines())

with Benchmarker(width=20) as bench:
    with open(path, 'r') as lines:
        for i, line in enumerate(lines):
            strings = line.rstrip('\r\n')
            res = es.index(index=index, doc_type=type, id=i, body={'strings': line})

    @bench("search text({0} times)".format(min(number_of_lines, SEARCH_COUNT_LIMIT)))
    def _(bm):
        with open(path, 'r') as lines:
            for i, line in enumerate(lines):
                strings = line.rstrip('\r\n')
                res = es.search(index=index, body={"query": {"match": {'strings': strings}}, "min_score": 20})

                # print(strings)
                # print("Got %d Hits:" % res['hits']['total'])
                # for hit in res['hits']['hits']:
                #     print(hit)


# $ python dev/benchmark_for_elasticsearch.py
# ## benchmarker:         release 4.0.1 (for python)
# ## python version:      3.5.5
# ## python compiler:     GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)
# ## python platform:     Darwin-17.6.0-x86_64-i386-64bit
# ## python executable:   /usr/local/miniconda3/envs/myenv/bin/python
# ## cpu model:           Intel(R) Core(TM) i7-6567U CPU @ 3.30GHz
# ## parameters:          loop=1, cycle=1, extra=0
#
# ##                        real    (total    = user    + sys)
# search text(5797 times)   18.0541    4.9900    4.6500    0.3400
#
# ## Ranking                real
# search text(5797 times)   18.0541  (100.0) ********************
#
# ## Matrix                 real    [01]
# [01] search text(5797 times)   18.0541   100.0

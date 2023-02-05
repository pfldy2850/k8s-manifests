import json
from datetime import datetime
from elasticsearch import Elasticsearch, ElasticsearchWarning

import warnings
warnings.filterwarnings('ignore', category=ElasticsearchWarning)

es = Elasticsearch("http://localhost:9200")

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", id=1, document=doc)
print(res)
print(res['result'])

res = es.get(index="test-index", id=1)
print(res)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", query={"match_all": {}})
print(res)
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

res = es.delete(index="test-index", id=1)
print(res)

# outputs 
"""
{'_index': 'test-index', '_type': '_doc', '_id': '1', '_version': 10, 'result': 'created', '_shards': {'total': 2, 'successful': 2, 'failed': 0}, '_seq_no': 9, '_primary_term': 1}
created
{'_index': 'test-index', '_type': '_doc', '_id': '1', '_version': 10, '_seq_no': 9, '_primary_term': 1, 'found': True, '_source': {'author': 'kimchy', 'text': 'Elasticsearch: cool. bonsai cool.', 'timestamp': '2023-02-05T21:53:58.450733'}}
{'author': 'kimchy', 'text': 'Elasticsearch: cool. bonsai cool.', 'timestamp': '2023-02-05T21:53:58.450733'}
{'took': 1, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1, 'relation': 'eq'}, 'max_score': 1.0, 'hits': [{'_index': 'test-index', '_type': '_doc', '_id': '1', '_score': 1.0, '_source': {'author': 'kimchy', 'text': 'Elasticsearch: cool. bonsai cool.', 'timestamp': '2023-02-05T21:53:58.450733'}}]}}
Got 1 Hits:
2023-02-05T21:53:58.450733 kimchy: Elasticsearch: cool. bonsai cool.
{'_index': 'test-index', '_type': '_doc', '_id': '1', '_version': 11, 'result': 'deleted', '_shards': {'total': 2, 'successful': 2, 'failed': 0}, '_seq_no': 10, '_primary_term': 1}
"""
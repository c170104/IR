import os
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import scoring

if not os.path.exists("index"):
    exit

ix = open_dir("index")

#with ix.searcher() as searcher:
# print(list(ix.searcher().lexicon("passage")))  
# print(list(ix.searcher().lexicon("movie")))
# print(list(ix.searcher().lexicon("title")))

index = "passage"
search_query = "Long"

qp = QueryParser(index, schema=ix.schema)
query = qp.parse(search_query)

with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
    results = searcher.search(query)
    print(results[0])




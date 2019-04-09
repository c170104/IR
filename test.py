import os
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import scoring

if not os.path.exists("index"):
    exit

ix = open_dir("index")

with ix.searcher(weighting=scoring.TF_IDF) as searcher:
    # print(list(ix.searcher().lexicon("passage")))  
    print(list(ix.searcher().lexicon("movie")))
    # print(list(ix.searcher().lexicon("title")))
    # qp = QueryParser("passage", schema=ix.schema)
    # query = qp.parse("long")
    # results = searcher.search_page(query, 1, pagelen=10)
    # content = []
    # for i in range(10):
    #     content.append(dict(results[i]))

    # print(content)


# index = "passage"
# search_query = "long"

# qp = QueryParser(index, schema=ix.schema)
# query = qp.parse(search_query)

# with ix.searcher() as searcher:
#     results = searcher.search(query)
#     print(results[0])




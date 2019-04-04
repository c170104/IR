from django.shortcuts import render
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import scoring
import os
from django.utils.html import escape

# Create your views here.

def index(request):
    if request.method == 'GET':
        print(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'index'))  
        if not os.path.exists(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'index')):
            return render(request, 'index.html')

        ix = open_dir(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'index'))
        print("HI")
        index = "passage"
        search_query = escape(request.GET.get('q', ''))
        print(search_query)

        qp = QueryParser(index, schema=ix.schema)
        query = qp.parse(search_query)

        with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
            results = searcher.search(query)

    return render(request, 'index.html', results)


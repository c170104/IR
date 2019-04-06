from django.shortcuts import render
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import scoring
import os
from django.utils.html import escape
from .forms import SearchForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST': 
        f = SearchForm(request.POST)
        if f.is_valid():
            if not os.path.exists(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'index')):
                return render(request, 'index.html')

            print("hit")
            ix = open_dir(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'index'))
            index = "passage"
            search_query = f.cleaned_data['query']
            print(search_query)

            qp = QueryParser(index, schema=ix.schema)
            query = qp.parse(search_query)
            searcher = ix.searcher(weighting=scoring.TF_IDF())
            # with ix.searcher(weighting=scoring.TF_IDF()) as s:
            results = searcher.search(query, limit=10)
            if(len(results) > 0):
                print(dict(results[0]))
                print(dict(results))
            return render(request, 'index.html')
    return render(request, 'index.html')


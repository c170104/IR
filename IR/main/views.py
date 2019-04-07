from django.shortcuts import render
from whoosh.index import open_dir
from whoosh.qparser import QueryParser, MultifieldParser
from whoosh import scoring
import os
from django.utils.html import escape
from .forms import SearchForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'GET': 
        f = SearchForm(request.GET)
        if f.is_valid():
            if not os.path.exists(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'index')):
                return render(request, 'index.html')

            ix = open_dir(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, 'index'))
            index = "passage"
            search_query = f.cleaned_data['query']
   
            qp = QueryParser(index, schema=ix.schema)
            query = qp.parse(search_query)
            page = int(request.GET.get('page')) if request.GET.get('page') is not None else 1
            if page == 0:
                page = 1
            pages = [{'previous': page-1, 'current': page, 'next': page+1}]

            searcher = ix.searcher(weighting=scoring.TF_IDF())
            results = searcher.search_page(query, page, pagelen=10)
            content = []
            for result in results:
                content.append(dict(result))
            return render(request, 'index.html', {'content': content, 'pages' : pages, 'query' : search_query})
    return render(request, 'index.html')


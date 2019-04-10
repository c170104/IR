from django.shortcuts import render
from whoosh.index import open_dir
from whoosh.qparser import QueryParser, MultifieldParser
from whoosh import scoring, fields, index, qparser
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
            # index = "movie"
            search_query = f.cleaned_data['query']
            category = request.GET.get('category') if request.GET.get('category') is not None else "default"
            if request.GET.get('sort') is None or request.GET.get('sort') == 'default':
                sort = None
            else:
                sort = request.GET.get('sort')
   
            page = int(request.GET.get('page')) if request.GET.get('page') is not None else 1
            if page == 0:
                page = 1
            
            pages = [{'previous': page-1, 'current': page, 'next': page+1}]

            with ix.searcher(weighting=scoring.TF_IDF) as searcher:
                if category == "default":
                    qp = MultifieldParser(["movie", "title", "passage"], schema=ix.schema)
                else:
                    qp = QueryParser(category, schema=ix.schema)

                user_query = qp.parse(search_query)
                results = searcher.search_page(user_query, page, pagelen=10, sortedby=sort)
                corrected = searcher.correct_query(user_query, search_query)
                print(corrected.string)
                test = searcher.search(user_query)
                print(test)
                print(len(test))
                content = []
                for result in results:
                    content.append(dict(result))
            return render(request, 'index.html', {'content': content, 'pages' : pages, 'query' : search_query, 'category' : category})
    return render(request, 'index.html')


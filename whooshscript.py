from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.analysis import StemmingAnalyzer
import os.path
import json, os

wd = os.getcwd() +"\\scrappedata\\"


# Specify schema
schema = Schema(
            title=              TEXT(stored=True, analyzer=StemmingAnalyzer()),
            author=             TEXT,
            movie=              KEYWORD(stored=True),
            url=                ID(stored=True),
            passage=            TEXT(analyzer=StemmingAnalyzer()),
            passage_summary=    STORED
        )

# Creates the index
if not os.path.exists("index"):
    os.mkdir("index")
    ix = create_in("index", schema)
else:
    ix = open_dir("index")

writer = ix.writer()

count = 0
#keys Movie, Title, Author, Hyperlink, Passage, Summary
while(True):
    txtfile = (wd+"textfile%i.txt" % (count))
    if os.path.exists(txtfile):
        with open(txtfile, 'r', encoding ="utf-8") as txt_file:
            datastore = json.load(txt_file)
            for i in range(len(datastore)):
                t = datastore[i]["Title"]
                a = datastore[i]["Author"]
                m = datastore[i]["Movie"]
                h = datastore[i]["Hyperlink"]
                p = datastore[i]["Passage"]
                s = datastore[i]["Summary"]
                
                # print(s.encode("utf-8").decode("utf-8"))
                
                writer.add_document (
                title = str(t, 'utf-8'),
                author = str(a, 'utf-8'),
                movie = str(m, 'utf-8'),
                url = str(h, 'utf-8'),
                passage = str(p, 'utf-8'),
                passage_summary = str(s, 'utf-8'),
                )
                
        count = count + 1
    else:
        break
            
writer.commit()




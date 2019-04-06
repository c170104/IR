from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.analysis import StemmingAnalyzer
import os.path


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

# LAWRANN PARSER

writer.add_document(
    title=u'Testing is this correction',
    author=u'Bill Gates',
    movie=u'Batman',
    url=u'https://testingonetwo.com',
    passage=u'Some super duper long ass passage that no one wants to read. I am having difficulties trying to think of what else to write.',
    passage_summary=u'Some super duper long ass passage that no one wants to read.'
)

writer.commit()




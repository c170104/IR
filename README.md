# EduOne

CZ4034 Information Retrieval Project source code

## Installation

**Method 1**

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [pipenv](https://github.com/pypa/pipenv).

```bash
pip install pipenv
```

Clone or download the [repository](https://github.com/ibenrawkss/IR).

```bash
git clone https://github.com/ibenrawkss/IR
```

Change directory into the folder IR.

```bash
cd IR
```

Use pipenv to install the packages that resides in the Pipfile.

```bash
pipenv install
```

**OR**

**Method 2**

Use package manager [pip](https://pip.pypa.io/en/stable/) to install the relevant packages.

```bash
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
whoosh = "*"
django = "*"
bs4 = "*"
nltk = "*"
requests = "*"
textblob = "*"

[requires]
python_version = "3.6"
```

## Required Step

nltk library TextBlob requires this code to be runned once to download the "punkt" library

```bash
nltk.download('punkt')
```

## Indexing

Due to GitHub file size limit, the indexes could not be uploaded.
The index has to be rebuild before running the server. (This part would take some time. ETA: 50 minutes)
There is a total of 103 scrapped data files. The script will print out the number for the file it is 
current working on.
```bash
python whooshscript.py
```

## Starting the server (Developer mode)

To run the server, enter:

```bash
python manage.py runserver [ip-address]:[port]
```


## License

[MIT](https://choosealicense.com/licenses/mit/)
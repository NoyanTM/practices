# practice-1

1.1. Setup on Linux (unix-like) environment:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
1.2. Setup on Windows environment:
```
py -m venv .venv
.venv\Scripts\Activate
```

2.1. Download dataset and analysis drafts:
```
python3 ./notebooks/download_dataset.py
python3 -m nltk.downloader popular
jupyter notebook -> ./notebooks/analysis.py
```


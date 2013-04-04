# Mobile Oxford's blog

Simple Pelican blog for the Mobile Oxford team.


## Local setup

1. Setup dependencies (you probably want to be in a virtualenv first) `pip install -r requirements.txt`
2. Generate CSS 
   `cd mox`
   `compass compile`
3. Generate HTML from the articles 
   `cd ..`
   `make html`

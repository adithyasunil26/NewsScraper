# hack-daddys

Contents:
1)IPyNb - contains ipynb notebooks in which the scripts were created and tested
2)Web-flask- contains all the main files

How to run:
1)clone the repo or download as zip and extract
2)change working directory to hack-daddys/
3)enter the following commands into terminal
  pip install pipenv
  pipenv install bs4 pandas newspaper3k requests nltk spacy
  pipenv shell 
  python -m spacy download en_core_web_sm
  export FLASK_APP=Web-flask
  export FLASK_DEBUG=1
  flask run
4)copy paste the url which will probably be https://127.0.0.1:5000 into browser 
5)enter the keywords in the texbox and click search button
6)give it a minute or two to take you to the next page
7)go to the hack-daddys folder to find the 1.csv and 1.json which are the outputs generated

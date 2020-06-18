# hack-daddys

<br/>Contents:
<br/>1)IPyNb - contains ipynb notebooks in which the scripts were created and tested
<br/>2)Web-flask- contains all the main files
<br/>
<br/>How to run:
<br/>1)clone the repo or download as zip and extract
<br/>2)change working directory to hack-daddys/
<br/>3)enter the following commands into terminal
<br/>    pip install pipenv
<br/>    pipenv install bs4 pandas newspaper3k requests nltk spacy
<br/>    pipenv shell 
<br/>    python -m spacy download en_core_web_sm
<br/>    export FLASK_APP=Web-flask
<br/>    export FLASK_DEBUG=1
<br/>    flask run
<br/>4)copy paste the url which will probably be https://127.0.0.1:5000 into browser 
<br/>5)enter the keywords in the texbox and click search button
<br/>6)give it a minute or two to take you to the next page
<br/>7)go to the hack-daddys folder to find the 1.csv and 1.json which are the outputs generated

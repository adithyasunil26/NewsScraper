#!/usr/bin/env python
# coding: utf-8

#run these in your terminal to install the packages if u dont have them already
#pip install requests
#pip install beautifulsoup4
#pip install nltk
#pip install newspaper3k
#pip install pandas
#pip install spacy
#python -m spacy download en_core_web_sm
#if u see any more missing packages just pip install them as well

def func(keyword):
  from flask import redirect,url_for
  import requests
  from bs4 import BeautifulSoup
  google_results=requests.get("https://www.google.com/search?q={}&tbm=nws".format(keyword))
  soup=BeautifulSoup(google_results.text,"html.parser")

  resulturls=soup.select('.kCrYT a')

  i=0
  k=[]
  for link in resulturls:
    a=link.get('href').split('=')
    a.pop(0) 
    a=''.join(a)
    a=a.split('&')
    a=a.pop(0)
    k.append(a)

  import nltk
  from newspaper import Article 
  #nltk.download('punkt')

  import pandas as pd
  import numpy as np
  from summarization import summarization
  import spacy
  import re
  from spacy.lang.en.stop_words import STOP_WORDS
  from string import punctuation
  from heapq import nlargest


  df=pd.DataFrame(columns=['Author','Publish Date','Top image','Text','Summary','Link'])

  i=0
  for link in k:
    article=Article('{}'.format(link))
    article.download()
    article.parse()
    article.nlp
    summ=summarization(article.text)
    df2=pd.DataFrame({'Author':[article.authors],'Publish Date':[article.publish_date],'Top image':[article.top_image],'Text':[article.text],'Summary':[summ],'Link':[link]},index=[i])
    df=pd.concat([df,df2])
    i=i+1

  df.to_json(r'1.json')
  df.to_csv('1.csv')
  return redirect(url_for('main.results'))

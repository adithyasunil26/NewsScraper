#!/usr/bin/env python
# coding: utf-8

import spacy
import re
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarization(text):
    punctuations=punctuation+'\n'+'\n\n'+'.\n\n'+'. \n\n'
    stopwords=list(STOP_WORDS)
    nlp=spacy.load('en_core_web_sm')

    doc=nlp(text)
    tokens=[token.text for token in doc]
    sent_tokens=[sent for sent in doc.sents]

    frq={}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuations:
                if word.text not in frq.keys():
                    frq[word.text]=1
                else:
                    frq[word.text]+=1

    maxfrq=max(frq.values())    
    for word in frq.keys():
        frq[word]=frq[word]/maxfrq

    sentscore={}
    for sent in sent_tokens:
        for word in sent:
            if word.text.lower() in frq.keys():
                if sent not in sentscore.keys():
                    sentscore[sent]=frq[word.text.lower()]
                else:
                    sentscore[sent]+=frq[word.text.lower()]

    sumlen=int(len(sent_tokens)*0.4
    )

    summary=nlargest(sumlen,sentscore,key=sentscore.get)
    summary=' '.join([word.text for word in summary])
    summary=re.sub('\n', '', summary)

    print(summary)
    return summary



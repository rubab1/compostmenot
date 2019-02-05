#! /usr/bin/env python
import pandas as pd
import numpy as np
import pickle, io
from nltk.stem import WordNetLemmatizer

from google.cloud import vision
from google.cloud.vision import types
from oauth2client.client import GoogleCredentials

clf,vectorizer= pickle.load(open('CompostClassifier.pkl','rb'))

credentials = GoogleCredentials.get_application_default()
client = vision.ImageAnnotatorClient()

def get_lemma(word,lemmatizer=WordNetLemmatizer()):
    _word = word.split(' ')
    for i,_w in enumerate(_word):
        _word[i] = lemmatizer.lemmatize(_w.lower())
    return ' '.join(_word)

def get_vect(x,vectorizer):
    return vectorizer.transform(x).toarray()

def get_class_weights(word,clf=clf,vectorizer=vectorizer):
    return clf.predict_proba(get_vect(np.array([get_lemma(word)]),vectorizer))

def get_weighted_class(vision,clf=clf,vectorizer=vectorizer):
    i,x = 0,[]
    for key,value in vision.items():
        if i==0:
            if clf.predict(get_vect(np.array([get_lemma(key)]),vectorizer))==0:
                return 0
            else:
                i=1
        x.append(value*get_class_weights(key,clf,vectorizer).T)
    x = np.array(x).sum(axis=0)
    return np.argmax(x/x.sum())


def get_labels(filename,client=client):
    with io.open(filename, 'rb') as image_file:
        content=image_file.read()
    image = types.Image(content=content)
    response = client.label_detection(image=image)
    labels,scores = [],[]
    for label in response.label_annotations:
        labels.append(label.description)
        scores.append(label.score)
    return dict(zip(labels,scores))


def best_guess(vision,clf=clf,vectorizer=vectorizer):
    pred = get_weighted_class(vision)
    if pred==0:
        col = 'red'
        rec = 'CompostMeNot :-( :-( :-('
    else:
        col = 'green'
        rec = 'CompostMe!!! Yaaaay!!!!!!'
    return col,rec

def DoAll(filename):
    vision = get_labels(filename)
    col,rec = best_guess(vision)
    rec = '\n{:s}\n'.format(rec)
    return col,rec

# CompostMeNot

Seattle residents have to sort their trash into compostable 
and non-compostable following guidelines specified by the 
city. It can be confusing, specially but not limited to 
someone moving here. This app simplifies that 
daily chore: snap a pic and let an app decide :-)

I turned the hard to resolve problem of recognizing diverse 
images of everyday items into a manageable solution combining 
Computer Vision, Natural Language Processing and Machine Learning 
techniques. The Hybrid recommender backend is developed in Python 
using Google Cloud Vision API, NLTK Lemmatizer, Scikit-learn 
Countvectorizer and Random-Forest classifier. I scraped 1,300+ 
pages from Seattle.gov to train Machine Learning models on telling 
apart compostable from non-compostables, then cleaned, lemmatized 
and vectorized the data. Then I tackled imbalanced classes via 
class weights, optimized the ML models and end-to-end validated 
the pipeline using real life user provided images. he HTML/CSS frontend 
uses Python Flask and Bootstrap. It has been deployed using the Google 
App Engine platform

Please try it out !!!

[CompostMeNot](https://compostmenot.appspot.com)


In this repo, the Notebooks demonstrates key steps of developing 
this product and the project namesake directory contains 
the deployed codebase.

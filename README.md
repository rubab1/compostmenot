# CompostMeNot

Seattle residents have to sort their trash into compostable 
and non-compostable following guidelines specified by the 
city. It can be confusing, specially but not limited to 
someone moving here. This project aims to simplify this 
daily chore: snap a pic and let an app decide :-)

I combined Computer Vision, Natural Language Processing and 
Machine Learning techniques to build a hybrid recommender 
backend for the app that serves a Python Flask frontend, and 
deployed the service on Google App Engine platform. Scraped 1300+ 
pages from Seattle.gov, cleaned data, tackled imbalanced classes 
via class weights, trained the NLP+ML models and end-to-end 
validated the pipeline using real life user provided images.

The Notebooks demonstrates key steps of developing 
this product and the project namesake directory contains 
the deployed codebase.

Please try it out !!!

[CompostMeNot](https://compostmenot.appspot.com)

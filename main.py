#!/usr/bin/env python
import os, sys
from flask import Flask

sys.path.append(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = "redacted"

from views import *

import nltk

nltk.download('wordnet')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


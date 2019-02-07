#!/usr/bin/env python
import os,sys,uuid,subprocess
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

sys.path.append(os.path.dirname(__file__))

from main import app

from compost import *

UPLOAD_FOLDER = './tmp'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')

@app.route('/index')
def index():
   return redirect(url_for('upload_file'))

@app.route('/cleanse')
def clean():
   for _file in os.listdir(app.config['UPLOAD_FOLDER']):
      _path = os.path.join(app.config['UPLOAD_FOLDER'], _file)
      os.unlink(_path)
   _t = subprocess.run(['cp', 'foo.dat', 'tmp/'], stdout=subprocess.PIPE)
   return redirect(url_for('upload_file'))

def allowed_file(filename):
   return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template("upload.html")
        file = request.files['file']
        # if user provides filetypes not allowed
        if not allowed_file(file.filename):
            return render_template("upload.html")
        if file and allowed_file(file.filename):
            filename = '_'.join((str(uuid.uuid4())[:8],secure_filename(file.filename)))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            col,rec,msg = DoAll(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("result.html",
                                   filename='/uploads/'+filename,
                                   message=msg,
                                   recommend=rec,
                                   col=col)
   return render_template("upload.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
   return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


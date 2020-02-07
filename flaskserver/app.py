from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from utils import utils as u
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///discord.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/quotes/')
def currentQuotes():
    textList = []
    os.system('cp ../media/offensive.txt .')
    with open('offensive.txt') as my_file:
        textList = my_file.readlines()
    
    return render_template("currentQuotes.html", data=textList)

@app.route('/addquote/', methods=['POST', 'GET'])
def addQuotes():
    if request.method == 'POST':
        os.system('cp ../media/offensive.txt .')
        new_quote = request.form['content']
        u.addLineToFile(f'\n{new_quote} ', 'offensive.txt')
        os.system('cp offensive.txt ../media/')
        return render_template('addQuotes.html')

    else:        
        return render_template('addQuotes.html')

    

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0:69')
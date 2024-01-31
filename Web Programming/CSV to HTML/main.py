import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

file = pd.read_csv('Flask Data.csv')
file.to_csv('Flask Data.csv', index= None)

@app.route('/')
@app.route('/table')
def table():
    data = pd.read_csv('Flask Data.csv')
    return render_template('table.html',tables = [data.to_html()], titles = [''])

if __name__ == '__main__':
    app.run(host='localhost',port=int("5000"))
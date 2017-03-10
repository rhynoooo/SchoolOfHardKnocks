from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def search_page():
	return render_template('index.html')

@app.route('/search_results')
def hello():
    return 'search results'

@app.route('/add')
def add():
	return 'add page...'

app.run()
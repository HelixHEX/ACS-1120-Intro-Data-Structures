"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, flash, redirect, request 
from tokens import tokenize
from markov_chain2 import Markov_Chain
import twitter


app = Flask(__name__)

mark = None

@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    global mark
    tokens = tokenize('./data/sample.txt')
    mark = Markov_Chain(tokens)
    

@app.route("/", methods=['GET'])
def home():
    """Route that returns a web page containing the generated text."""
    global mark 
    return render_template('index.html', sentence = mark.walk())

@app.route("/", methods=['POST'])
def tweet():
    """Route that tweets the generated text."""
    global mark
    sentence = request.form['sentence']
    print(sentence)
    res = twitter.tweet(sentence)
    if res:
        print(res)
        return redirect('/')
    else:
        flash('Error: Unable to tweet sentence.')

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)

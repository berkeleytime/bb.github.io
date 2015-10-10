"""Idan Hovav
Hacking shit and shit.
"""

import sqlite3
import time
from flask import Flask, request, g, redirect, render_template

app = Flask(__name__)
DATABASE = 'bt.db'

@app.route("/")
def hello():
	return "Swando"
	#return render_template("index.html")

if __name__ == "__main__":
	app.run()

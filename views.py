import set_city as sc
import asyncio
from flask import Flask, render_template, request

debug = True
if debug:
    import nest_asyncio
    nest_asyncio.apply()

# MAIN

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
app.run(debug=True)
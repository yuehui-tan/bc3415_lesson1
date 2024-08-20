from flask import Flask, render_template, request
import google.generativeai as palm
import os

api = os.getenv("MAKERSUITE_API_TOKEN") 
palm.configure(api_key=api)
model = {"model": "models/chat-bison-001"}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()
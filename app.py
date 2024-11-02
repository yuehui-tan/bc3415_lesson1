from flask import Flask, render_template, request
import google.generativeai as genai
import os
from textblob import TextBlob

api= os.getenv("API_KEY") 
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))


# @app.route("/financial_FAQ",methods=["GET","POST"])
# def financial_FAQ():
#     return(render_template("financial_FAQ.html"))


@app.route("/ai_agent",methods=["GET","POST"])
def ai_agent():
    return(render_template("ai_agent.html"))

@app.route("/ai_agent_reply",methods=["GET","POST"])
def ai_agent_reply():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("ai_agent_reply.html",r=r.text))

@app.route("/joke",methods=["GET","POST"])
def joke():
    return(render_template("joke.html"))

#Sentiment Analysis
@app.route("/SA",methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))

#Sentiment Analysis Result
@app.route("/SAR",methods=["GET","POST"])
def SAR():
    q = request.form.get("q")
    r = TextBlob(q).sentiment
    return(render_template("SAR.html", r = r))

#Transfer Money
@app.route("/TM", methods = ['GET', 'POST'])
def TM():
    return(render_template("TM.html"))
    
@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("index.html"))



if __name__ == "__main__":
    app.run()
    

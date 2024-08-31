from flask import Flask, render_template, request
import google.generativeai as palm 
import os


makersuite_api= os.getenv("API_KEY") 
palm.configure(api_key = makersuite_api)
model = {"model": "models/text-bison-001"}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))


@app.route("/ai_agent",methods=["GET","POST"])
def ai_agent():
    return(render_template("ai_agent.html"))

@app.route("/ai_agent_reply",methods=["GET","POST"])
def ai_agent_reply():
    q = request.form.get("q")
    r = palm.chat(prompt=q, **model)
    return(render_template("ai_agent_reply.html",r=r.last))

@app.route("/joke",methods=["GET","POST"])
def joke():
    return(render_template("joke.html"))


@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("index.html"))



if __name__ == "__main__":
    app.run()
    

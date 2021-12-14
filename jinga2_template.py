# Jinga 2 template
# we would integaring it to some data source so that we would be getting it from there itself

"""""
{%....%} conditions,for,do,while loops
{{    }} expressions to print the template output --> (used in the result.html for result and score display)
{#....#} this is internal comments
"""""

from score_checker import result
from flask import Flask,redirect,url_for,render_template,request
import numpy as np
from numpy import ma, result_type

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("score_page.html")

@app.route("/fail/<int:score>")
def fail(score):
    return render_template("jinga_result.html",result = score)

@app.route("/success/<int:score>")
def success(score):
    result = ""
    if score>=50:
        result  = "PASS"
    else:
        result = "FAIL"
    expression = {"score":score,"result":result}
    return render_template("jinga_result.html",result = expression)

@app.route("/submit",methods = ["POST","GET"])
def submit():
    total_score = 0
    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["mathematics"])
        python = float(request.form["python"])
        total_score = np.mean([science,maths,python])
    result = ""
    if total_score >= 50:
        result = "success"
    else:
        result = "fail"
    return redirect(url_for(result,score = total_score))   

if __name__ == "__main__":
    app.run(debug = True)
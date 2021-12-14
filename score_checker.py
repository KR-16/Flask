from flask import Flask,redirect,url_for,render_template,request

import numpy as np

# request helps you to read the posted value

app = Flask(__name__)

@app.route("/")
def result():
    return render_template("score_page.html")

@app.route(rule = "/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template("result.html",result = res, score = score)

@app.route("/fail/<int:score>")
def fail(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template("result.html",result = res, score = score)

# # Result checker
# @app.route("/results/<int:marks>")
# def results(marks):
#     result = ""
#     if marks < 50:
#         result  = "fail"
#     else:
#         result = "success"
#     return render_template(url_for(result, score = marks))

# Result checker submit html page
@app.route(rule = "/submit" , methods = ["POST","GET"])
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
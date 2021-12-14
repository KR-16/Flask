# URL building Dynamically
# Variable Rules ad URL Building

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")

def welcome():
   return "Welcome to Flask :) "

# it is app decorator with  /successs as the URL and append some values with integer
# building URL dynamically and it is called as Variable Rules
@app.route(rule="/success/<int:score>") 
def success(score):
    return "<html><body><h1>The student has passed with</h1></body></html>" + str(score)


@app.route(rule="/fail/<int:score>") 
def fail(score):
    return "The student has failed and the marks are " + str(score)

@app.route(rule="/results/<int:marks>") 
def my_result(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result = "success"
    
    return redirect(url_for(result, score = marks))


if __name__ == "__main__":
    app.run(debug= True)
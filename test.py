from flask import Flask

app = Flask(__name__) ## Creates the WSGI application

# Decorator
@app.route(rule = "/") # rule tells the URL where we will be running the app

def welcome():
    return "Welcome to flask environment :)" # these function is seen in the URL web page

@app.route(rule = "/flask") # rule tells the URL where we will be running the app

def Wel():
    return "HI :)" # these function is seen in the URL web page


if __name__ == "__main__" :
    app.run(debug = True)
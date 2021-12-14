# Integrate HTML with Flask
# HTTP verb like GET and POST

from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route(rule= "/")

def welcome():
    return render_template("index.html")

# render_template you have to have a folder with template and should contain the file name inside the folder

if __name__ == "__main__":
    app.run(debug = True)
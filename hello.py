from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! this is a test. cool?'

@app.route('/myFirstPage')
def new_function():
    return "This is a new function"   

@app.route("/creepy/<persons_name>")
def say_hi(persons_name):
    return "Hello %s, I SEE YOU" % persons_name

@app.route('/exampleTemplate/<int:fav_num>')
def buildMyPage(fav_num=10):
    return render_template("myExample.html", fav_num=fav_num)
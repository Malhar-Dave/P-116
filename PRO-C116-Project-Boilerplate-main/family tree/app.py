# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "" # write your name
    age = "" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route('/')
def father():
    return 'hello'
app.run(debug=True)


# define the route to mother webpage
@app.route('/')
def mother():
    return 'hello'
app.run(debug=True)

# define the route to friends webpage
@app.route('/')
def friends():
    return 'hello'
app.run(debug=True)


# add other routes, if you want
@app.route('/')
def me():
    return 'hello'
app.run(debug=True)


# run the file
if __name__  ==  '__main__':
    app.run(debug=True)

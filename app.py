# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Sasha (not real image below)" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route('/father')
def father():
    name='Sunny (not real image below)'
    age='above 35 (not accurate)'
    return render_template('index.html' , name = name , age = age)
# define the route to mother webpage
@app.route('/mother')
def mother():
    name='Sheetal (not real image below)'
    age='above 35 (not accurate)'
    return render_template('index.html' , name = name , age = age)
# define the route to friends webpage
@app.route('/friend')
def friend():
    name='Anabia (not real image below)'
    age='14'
    return render_template('index.html' , name = name , age = age)

# add other routes, if you want
@app.route('/brother')
def brother():
    name='Ryan (not real image below)'
    age='11'
    return render_template('index.html' , name = name , age = age)
@app.route('/sisterPup1')
def sisterPup1 ():
    name='Daisy (Bichon Frise)'
    age='3'
    return render_template('index.html' , name = name , age = age)

@app.route('/sisterPup2')
def sisterPup2 ():
    name='Bella (Cavalier King Charles Spaniel)'
    age='1'
    return render_template('index.html' , name = name , age = age)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)

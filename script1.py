#run this program and open browser on localhost to see it

from flask import Flask, render_template
#from flask library import Flask Class

app = Flask(__name__)
#__name__ = a variable who will take the name of the python script
#case 1: when running this script, __name__ will be __main__
#case 2 when running other script with this imported, pythin will assing __name__ to app4.py and not __main__



@app.route('/')  #'/' means homepage; app.route('') is called a decorator
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/map/')
def map():
    return render_template("Map1.html")

if __name__ == "__main__":
    app.run(debug=True)

#all above is need for a website




from flask import Flask, render_template
import datetime

app = Flask(__name__)
title= ' Variable page '
dummy=[
    {
        'name': 'test1'
    },
    {
        'name': 'test2'
    }
]
now= datetime.datetime.now()

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/variable")
def var():
    return render_template('var.html', myname=dummy, titles=title, times=now)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "SK*HbPI]AMToPzt*8WycvXS$:nRbB"

@app.route('/')
def mainP():
    return render_template("rgb.html")


@app.route('/red')
def redC():
    session['color'] = "red"
    return redirect('/')


@app.route('/green')
def greenC():
    session['color'] = "green"
    return redirect('/')


@app.route('/blue')
def blueC():
    session['color'] = "blue"
    return redirect('/')


app.run(debug=True)

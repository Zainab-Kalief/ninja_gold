from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsMySecret'


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

def chance():
    chance = random.randrange(0,2)
    if chance == 1:
        return True
    else:
        return False

@app.route('/processMoney', methods=['POST'])
def giveGold():
    time = datetime.now()
    if request.form['action'] == 'farm':
        randomNum = random.randrange(10,21)
        session['gold'] += randomNum
        session['activities'].insert(0, (randomNum, request.form['action'], time))
    elif request.form['action'] == 'cave':
        randomNum = random.randrange(5,11)
        session['gold'] += randomNum
        session['activities'].insert(0, (randomNum, request.form['action'], time))
    elif request.form['action'] == 'house':
        randomNum = random.randrange(2,6)
        session['gold'] += randomNum
        session['activities'].insert(0, (randomNum, request.form['action'], time))
    elif request.form['action'] == 'casino':

        if chance() == True:
            randomNum = random.randrange(0,51)
            session['gold'] += randomNum
            bet = 'won'
        else:
            randomNum = random.randrange(0,51)
            session['gold'] -= randomNum
            bet = 'lost'
        session['activities'].insert(0, (randomNum, request.form['action'], time, bet))
    print session['activities']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear() #this will clear the dic
    return redirect('/')

app.run(debug=True)

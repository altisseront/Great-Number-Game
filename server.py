import random
from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'chiken'
@app.route('/')         # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def result():
    randNum = random.randint(1,100)
    num = int(request.form['num'])
    print(num)
    if randNum == num:
        session['txt'] = str(randNum) + "was the number!"
        session['backgroundclr'] = 'green'
        session['box'] = True
    elif randNum > num:
        session['txt'] = 'It was ' + str(randNum) + ', Too low!'
        session['backgroundclr'] = 'red'
        session['box'] = True
    else:
        session['txt'] = 'It was ' + str(randNum) + ', Too high!'
        session['backgroundclr'] = 'red'
        session['box'] = True
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
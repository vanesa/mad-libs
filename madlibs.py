from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

# route to display the yes or no question
@app.route('/game')
def show_game_form():
    answer = request.args.get("radiobutt")
    attitude = "dumb"
    # player = request.args.get("person")
    # goodbye = 
    print answer
    if answer == "no":
        return render_template("goodbye.html", compliment=attitude)
    elif answer == "yes":  
        return render_template("game.html")


@app.route('/madlib')
def show_madLib():
    color= request.args.get("colorselection")
    person = request.args.get("person")
    bodypart = request.args.get("bodypart")
    adj = request.args.getlist("description")

    return render_template("madlib.html", colorselection=color, person=person, bodypart=bodypart, descriptions=adj )

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)

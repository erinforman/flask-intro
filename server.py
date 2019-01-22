"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.<a href="http://localhost:5000/hello">try me!</a></html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="POST">
          What's your name? <input type="text" name="person">
          Compliment:
            <select name="compliment">
                <option value="Floral">Floral</option>
                <option value="Very dances with wolves">Very dances with wolves</option>
                <option value="Mathematical">Mathematical</option>
            </select>
        <input type="submit" value="Submit">
        </form>
        <form action="/diss" method="GET">
          Diss:
            <select name="diss">
                <option value="You smell like a subway">You smell like a subway</option>
                <option value="You could be a farmer in those clothes">You could be a farmer in those clothes</option>
                <option value="Avuncular">Avuncular</option>
            </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet", methods=["POST"])
def greet_person():
    """Get user by name."""

    player = request.form.get("person")

    compliment = request.form.get("compliment")

    # compliment = choice(AWESOMENESS)
   #y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss", methods=["GET"])
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    # compliment = choice(AWESOMENESS)
   #y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)

if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")

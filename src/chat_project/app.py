from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/adventure")

@app.route("/adventure")
def adventure():
    return render_template("adventure.html")

@app.route("/scene1")
def scene1():
    name = request.args.get('name', 'Aventurier')
    return render_template("scene1.html", name=name)

@app.route("/scene2")
def scene2():
    name = request.args.get('name', 'Aventurier')
    return render_template("scene2.html", name=name)

@app.route("/scene3")
def scene3():
    name = request.args.get('name', 'Aventurier')
    return render_template("scene3.html", name=name)

@app.route("/scene4")
def scene4():
    name = request.args.get('name', 'Aventurier')
    return render_template("scene4.html", name=name)

@app.route("/scene5")
def scene5():
    name = request.args.get('name', 'Aventurier')
    return render_template("scene5.html", name=name)

@app.route("/scene6")
def gameover():
    name = request.args.get('name', 'Aventurier')
    return render_template("gameover.html", name=name)

if __name__ == "__main__":
    app.run()
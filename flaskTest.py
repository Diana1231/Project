from flask import Flask, render_template,request
import foodProject

app = Flask(__name__)
@app.route('/')
def homepage():

    return render_template("index.html")


@app.route('/',methods=['POST'])
def getValue():
    userInput = request.form['userInput']
    yum_json = foodProject.getAllReipe(userInput)
    recepies = foodProject.getRecepieList(yum_json)
    return render_template("recipies.html",recepies=recepies,userInput=userInput)

@app.route('/',methods=["GET"])
def rerunIndex():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()


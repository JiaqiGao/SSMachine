from flask import Flask, render_template, request
import random, csv, string
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("begin.html")

@app.route("/auth", methods=['POST'])
def auth():
    name = request.form["username"]
    o = open("static/wishes.csv")
    w = o.read()
    o.close()

    wishes = w.split(';')
    wishes = wishes[:-1]
    count = 0
    for i in wishes:
        wishes[count] = i.split(':')
        count = count+1
    
    r = random.choice(wishes)
    while(r[0]==name):
        r = random.choice(wishes)
    result = r
    newwishes = []
    for i in wishes:
        if(i!=r):
            newwishes.append(i)
    combine = ''
    for x in newwishes:
        combine += x[0] + ":" + x[1]
        combine += ";"

    f = open('static/wishes.csv', 'w')
    f.write(combine)
    f.close()

    nresult = result[0]
    wresult = result[1] 

    return render_template("result.html", nresult=nresult, wresult=wresult)

@app.route("/add", methods=['POST'])
def add():
    return render_template("add.html")

@app.route("/create", methods=['POST'])
def create():
    name = request.form["username"]
    wishes = request.form["wishlist"]
    fields = name + ":" + wishes
    fd = open('static/wishes.csv','a')
    fd.write(fields+';')
    fd.close()
    
    return render_template("begin.html")

if __name__ == "__main__":
    app.debug = True
    app.run()

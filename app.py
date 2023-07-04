from flask import Flask, render_template, request

app = Flask(__name__)# interface between my server and my application wsgi

import pickle
model = pickle.load(open(r'G:/Project/model.pkl','rb'))

@app.route('/')#binds to an url
def helloworld():
    return render_template("index.html")

@app.route('/login', methods =['POST'])#binds to an url
def login():
    a =request.form["dd"]
    b= request.form["ee"]
    c= request.form["kk"]
    d= request.form["ll"]
    e= request.form["mm"]
    f= request.form["ss"]
    g= request.form["aa"]
    h= request.form["ii"]
    i= request.form["li"]
    j= request.form["vv"]
    k= request.form["tt"]
    
    t=[[float(a),float(b),int(c),float(d),int(e),float(f),float(g),float(h),float(i),float(j),float(k)]]
    output= model.predict(t)
    print(output)  
        
    return render_template("index.html",y = "the predicted genre is " + str(output[0]) )

#@app.route('/admin')#binds to an url
#def admin():
   # return "Hey Admin How are you?"

if __name__ == '__main__' :
    app.run(debug= False)
    

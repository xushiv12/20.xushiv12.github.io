from flask import Flask,request,render_template
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
x1=""
x2=""
y=""
xu=""
asd="r"
@app.route("/",methods=["POST","GET"])
def home():
    x1=request.form.get("x1") or "r"
    x2=request.form.get("x2")
    xa=0
    with open("value.txt","r",encoding="utf-8") as r:
        for xu in r:
            if xu.startswith(x1+":"):
                    xa=1
           
    if xa==0:
        with open("value.txt","a",encoding="utf-8") as f:
            f.write(f"https:{x1}:{x2}\n")
    return render_template("1.html")
@app.route("/1",methods=["POST","GET"])
def a1():
    asd=request.form.get("asd") or "r"
    xushi=""
    xu1=""
    xx=""
    with open("value.txt","r",encoding="utf-8") as r:
        for y in r:           
            if y.startswith(asd+":"):
                xushi=y.strip()
                xu1=xushi.split(":",2)[2]
                return xu1
    return "我们好像没有发现您的域名。"
if __name__=='__main__':
    app.run(host="localhost",port=1025)
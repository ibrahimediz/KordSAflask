from app import app
from flask import render_template,jsonify,request

data = [{
    "item": "Lattes",
    "price": 25,
    "size": "Tall",
    },]


# @app.route('/kahve')
# def kahveGetir():
#     return {"veri":data}


# @app.route('/')
# @app.route('/index')
# def index():
#     data ={"isim":"İbrahim"}
#     return render_template("index.html",data=data)



@app.get('/kahve')
def getKahve():
    return {"veri":data}


@app.post("/kahve")
def postKahve():
    request_data = request.get_json()
    new_kahve = {"item":request_data["item"],"price":request_data["price"],"size":request_data["size"]}
    data.append(new_kahve)
    return new_kahve,201
    
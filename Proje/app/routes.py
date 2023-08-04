from app import app
from flask import render_template,jsonify,request

data = [{
    "item": "Lattes",
    "price": 25,
    "size": "Tall",
    "icerik":{}
    },]


@app.get('/kahve')
def getKahveler():
    return {"veri":data}


@app.post("/kahve")
def postKahve():
    request_data = request.get_json()
    new_kahve = {"item":request_data["item"],"price":request_data["price"],"size":request_data["size"]}
    data.append(new_kahve)
    return new_kahve,201

# "kahve":20,"sut":40,"laktozsuz":[1,0]
@app.post("/kahve/<string:item>/icerik") # kahve/Latte/icerik
def postIcerik(item):
    request_data = request.get_json()
    for da in data:
        if da["item"] == item:
            yeni_icerik = {"kahve":request_data["kahve"],"sut":request_data["sut"],"laktozsuz":request_data["laktozsuz"]}
            da["icerik"] = yeni_icerik
            return da
    return {"message":"Kahve Bulunamadı"},404

@app.get("/kahve/<string:item>")
def getKahve(item):
    for da in data:
        if da["item"] == item:
            return da
    return {"message":"Kahve Bulunamadı"},404


@app.get("/kahve/<string:item>/icerik") # kahve/Latte/icerik
def getIcerik(item):
    for da in data:
        if da["item"] == item:
            return da
    return {"message":"Kahve Bulunamadı"},404
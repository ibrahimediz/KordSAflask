from app import app
from flask import request

data = [{
    "item": "Burger",
    "price": 50,
    "icerik":{}
    },
    {
    "item": "Lahmacun",
    "price": 50,
    "icerik":{}
    },]

@app.get('/burger')
def getburger():
    return {"veri":data}

@app.post("/burger")
def postburger():
    request_data = request.get_json()
    new_burger = {"item":request_data["item"],"price":request_data["price"]}
    data.append(new_burger)
    return new_burger,201

@app.post("/burger/<string:item>/icerik") # 
def postIcerik(item):
    request_data = request.get_json()
    for da in data:
        if da["item"] == item:
            yeni_icerik = {"et":request_data["et"],"mayonez":request_data["mayonez"],"vegan":request_data["vegan"]}
            da["icerik"] = yeni_icerik
            return da
    return {"message":"Burger bulunamadı"},404


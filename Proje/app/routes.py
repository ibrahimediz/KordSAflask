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



import numpy as np
from tensorflow.keras.models import load_model
import pickle
import os

@app.get("/sistemtest")
def sistemtest():
    sozluk = {}
    try:
        # print("ADDRESSS:",app.config["MODEL_ADRES"])
        # model = load_model(app.config["MODEL_ADRES"])
        model = load_model("flaskicinmodel.hdf5")
        if model:
            print("MODELiçeriği",model)
            sozluk["MODEL_YUKLENDI"] = "OK"
    except Exception as hata:
        print("MODEL",hata)
        sozluk["MODEL_YUKLENDI"] = str(hata)
    try:
        # olcek = pickle.load(open(app.config['OLCEK_ADRES'],"rb"))
        olcek = pickle.load(open("olcek.pkl","rb"))
        if model:
            sozluk["OLCEK_YUKLENDI"] = "OK"
    except Exception as hata:
        print("OLCEK",hata)
        sozluk["OLCEK_YUKLENDI"] = str(hata)
    # yeni_veri = [[3.57,7.5,-2.4,-0.35]]
    # sonuc = model.predict(olcek.transform(yeni_veri))[0]
    # sozluk["MODEL_SONUC"] = str(sonuc)
    return sozluk



@app.post("/tahmin")
def tahminEt():
    try:
        # model = load_model(app.config["MODEL_ADRES"])
        model = load_model("flaskicinmodel.hdf5")
    except Exception as hata:
        print("MODEL",hata)
    try:
        # olcek = pickle.load(open(app.config['OLCEK_ADRES'],"rb"))
        olcek = pickle.load(open("olcek.pkl","rb"))
    except Exception as hata:
        print("OLCEK",hata)
    request_data = request.get_json()
    # yeni_veri = [[3.57,7.5,-2.4,-0.35]]
    # variace	skewness	curtosis	entropy	
    liste = [[request_data["variace"],request_data["skewness"],request_data["curtosis"],request_data["entropy"]]]
    olcekli = olcek.transform(liste)
    sonuc = model.predict(olcekli)
    print("SONUC",sonuc)
    print("SONUC",np.round(sonuc)[0])   
    return {"tahmin":int(np.round(sonuc)[0])},201
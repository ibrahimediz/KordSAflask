import os
class Config(object):
    MODEL_ADRES = os.environ.get("MODEL_ADRES") or "/workspace/KordSAflask/Proje/flaskicinmodel.hdf5"
    OLCEK_ADRES = os.environ.get("OLCEK_ADRES") or "/workspace/KordSAflask/Proje/olcek.pkl"
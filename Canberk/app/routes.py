from app import app


data = [{"isim" : "Canberk"}]

@app.route('/index')
def index():
    return {"veri":data}

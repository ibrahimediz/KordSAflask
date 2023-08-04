from app import app
data = [{"isim" : "Canberk"}]

@app.route('/')
@app.route('/index')
def index():
    retun {"veri" :data}

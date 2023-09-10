from flask import Flask, render_template
from db import MongoDriver

app = Flask(__name__)
mongodb = MongoDriver()



@app.route('/')
def index():
    # Obtención de datos almacenados en MongoDB
    data = mongodb.get_products(username="Marvel")
    return render_template('web.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

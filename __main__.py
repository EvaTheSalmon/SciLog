import os, logging
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv('.env')
mongo_adress = os.environ.get('MONGO_ADRESS')
db_name = os.environ.get('DB_NAME')

app = Flask(__name__)

client = MongoClient('mongodb://' + mongo_adress)
db = client[str(db_name)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all.html')
def all():
    return render_template('all.html')

@app.route('/add.html')
def add():
    return render_template('add.html')

@app.route('/save-form-data', methods=['POST'])
def save_form_data():
    # result = jsonify(request.form.to_dict())
    result = jsonify(request.form.to_dict())
    logging.debug(result)
    return result

if __name__ == '__main__':
    app.run(debug=True)
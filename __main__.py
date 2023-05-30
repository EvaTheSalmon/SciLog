import os, logging
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.json_util import dumps

load_dotenv('.env')
mongo_adress = os.environ.get('MONGO_ADRESS')
db_name = os.environ.get('DB_NAME')
collection_name = os.environ.get('COLLECTION_NAME')

app = Flask(__name__)

client = MongoClient('mongodb://' + mongo_adress)
db = client[str(db_name)]
collecton = db[str(collection_name)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all.html')
def all():
    try:
        processes = db.collection_name.find()
        return render_template('all.html',processes=processes)
    except Exception as e:
        return dumps({'error': str(e)})
    
@app.route('/add.html')
def add():
    return render_template('add.html')

@app.route('/save-form-data', methods=['GET'])
def save_form_data():
    result = jsonify(request.form.to_dict())
    logging.debug(result)
    # collecton.insert_one(result)
    return result

if __name__ == '__main__':
    app.run(debug=True)
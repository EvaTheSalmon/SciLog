from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
    result = jsonify(request.form)
    return result

if __name__ == '__main__':
    app.run(debug=True)
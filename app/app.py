from flask import Flask, jsonify, request
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo à Aplicação Web Flask!"

@app.route('/api/data')
def get_external_data():
    response = requests.get('https://api.exemplo.com/data')
    data = response.json()

    df = pd.DataFrame(data)

    df = df[['coluna1', 'coluna2']]

    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

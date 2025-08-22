# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from calc import Calcular

app = Flask(__name__)
CORS(app)

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    expressao = data.get('expressao', '')
    try:
        resultado = Calcular(expressao)
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Define a route for recognizing named entities
@app.route('/named_entity', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    data['sentence'] = data['sentence'].replace("\n", " ")
    data_updated = {data['sentence']}
    return jsonify({'named_entities': "Venkat"})

if __name__ == '__main__':
    app.run(debug=True)
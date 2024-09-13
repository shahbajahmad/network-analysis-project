from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Mock data for simplicity
    data = {"message": "Data delivered to ML application"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

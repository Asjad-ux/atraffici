from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Backend is up and running!'})

@app.route('/api/traffic/status')
def traffic_status():
    return jsonify({'total_vehicles': 1250, 'status': 'working'})

if __name__ == '__main__':
    print("🚦 Starting Traffic Management Backend...")
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__=="__main__":
    app.run
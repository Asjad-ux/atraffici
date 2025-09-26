from flask import Flask, request, jsonify, send_file
import os
import requests

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')  # Render environment variable se API key le

@app.route('/')
def home():
    # index.html ko serve karta hai, yeh file project root mein honi chahiye
    return send_file(os.path.join(os.getcwd(), 'html.html'))

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter missing'}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': data.get('message', 'Error fetching weather data')}), 400

    return jsonify({
        'temperature': data['main']['temp'],
        'condition': data['weather'][0]['description']
    })

if __name__ == "__main__":
    # 0.0.0.0 host karke pura network access milta hai, port 8000 me chale
    app.run(host='0.0.0.0', port=8000)

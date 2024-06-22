from flask import Flask, send_file
import os
import zipfile

app = Flask(__name__)
port = 8000

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))

@app.route('/', methods=['GET'])
def download_file():
    folder = "test"
    zip_filename = folder + ".zip"

    # Créez un fichier zip du dossier
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(folder, zipf)

    # Envoyez le fichier zip au client
    return send_file(zip_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

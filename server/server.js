const express = require('express');
const app = express();
const port = 3000;

// Middleware pour parser le corps des requêtes JSON
app.use(express.json());

// Middleware pour gérer les en-têtes CORS
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    next();
});

// Route pour envoyer une réponse simple pour la route GET
app.get('/', (req, res) => {
    res.send('Hello World!');
});

// Route pour recevoir les données du client
app.post('/key', (req, res) => {
    const receivedData = req.body;
    console.log('Données reçues key :', receivedData);
    res.send('Données reçues');
});


app.post('/click', (req, res) => {
    const receivedData = req.body;
    console.log('Données reçues click :', receivedData);
    res.send('Données reçues');
});

app.post('/location', (req, res) => {
    const receivedData = req.body;
    console.log('Données de localisation reçues :', receivedData);
    res.send('Données de localisation reçues par le serveur');
});

// Démarrer le serveur
app.listen(port, () => {
    console.log(`Serveur démarré sur http://localhost:${port}`);
});

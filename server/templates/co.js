// const CryptoJS = require('crypto-js');

function connection(){
    console.log('click')
    Name = document.getElementById('name').value
    mdp = document.getElementById('mdp').value
    console.log(Name, mdp)
    if(Name.trim().length > 0 && mdp.trim().length > 0){
        console.log("________________________________")

        good_Name = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
        good_mdp = "5fcf82bc15aef42cd3ec93e6d4b51c04df110cf77ee715f62f3f172ff8ed9de9"

        encode_Name = CryptoJS.SHA256(Name).toString(CryptoJS.enc.Hex);
        encode_mdp = CryptoJS.SHA256(mdp).toString(CryptoJS.enc.Hex);

        if(encode_Name == good_Name){
            console.log('good')
            window.location.href = 'index.html'
        }else{
            console.log('no good')
        }

        console.log("________________________________")
    }else{
        document.getElementById('info').classList.remove('info')
    }
}
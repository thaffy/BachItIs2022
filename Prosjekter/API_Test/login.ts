var myHeaders = new Headers();

myHeaders.append('username', 'geir'); //legger til brukernavnet - MÅ HETE USERNAME
myHeaders.append('password','Rq2AAz6HcH2EDCv') //legger til passordet - MÅ HETE PASSWORD

var myInit = {
    method: 'GET',
    headers: {
        Accept: "text/plain",
        RequestMode: "no-cors"
    }
    };


var myRequest = new Request('http://127.0.0.1:8000/login', myInit);

fetch(myRequest).then(function(response) {
    return response.json();
})
.then(function(parsedData) {
    if(parsedData===0){ //dersom vi returner NULL fra apiet
        console.log('No user found')
    }
    else {
        let token = parsedData['token'] // lagrer token fra responsen i variabel
        document.cookie = 'token='+token // og storer den i cookie
    }
})

fetch('https://jc5qyxzdo8.execute-api.eu-west-1.amazonaws.com/Prod/put')
    .then(fetch('https://jc5qyxzdo8.execute-api.eu-west-1.amazonaws.com/Prod/get'))
    .then(response => response.json())
    .then(data => { document.getElementById('number').innerText = data.count
    })

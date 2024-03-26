const formulario = document.querySelector('.form-js');

formulario.addEventListener('submit', function(event) {
    event.preventDefault()
    
    const email = document.getElementById("InputEmail1").value
    const senha = document.getElementById("InputPassword1").value
    
    if (email !== "" && senha !== "") {
        axios.post('http://127.0.0.1:5000/login', JSON.stringify({ email, senha }), {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            alert(response.data)
        })
        .catch(error => {
            console.error('Erro na requisição POST', error);
        })
    } else {
        console.log("Por favor, preencha todos os campos.");
    }
});

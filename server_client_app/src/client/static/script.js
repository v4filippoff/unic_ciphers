function clearError() {
    document.getElementById("errors").innerHTML = "";
}

function showDataValidationError(data) {
    const errorsDiv = document.getElementById("errors");
    clearError();

    function addErrorBlockToDiv(text) {
        let block = document.createElement("p");
        block.innerHTML = text;
        errorsDiv.append(block);
    }

    if (typeof data['detail'] === 'string')
        addErrorBlockToDiv(data['detail']);
    else if (data['detail'] instanceof Array) {
        for (let i = 0; i < data['detail'].length; i++)
            addErrorBlockToDiv(data['detail'][i]['msg']);
    }
}

async function makePostRequest(apiUrl, data, successHandler, errorHandler) {
    clearError();
    let defaultHeaders = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    };
    const rawResponse = await fetch(window.location.origin + apiUrl, {
        headers: defaultHeaders,
        method: "POST",
        body: JSON.stringify(data)
    })
    const result = await rawResponse.json();
    if (rawResponse.status === 200)
        successHandler(result);
    else if (rawResponse.status === 422 || rawResponse.status === 400)
        errorHandler(result);
}

let createUserUrl = "/api/users/";

const registrationForm = document.getElementById("registrationForm");

registrationForm.addEventListener('submit', (event) => {
    function successHandler(data) {
        let mainBlock = document.getElementById("main");
        mainBlock.innerHTML = "";
        let successBlock = document.createElement("div");
        let message = document.createElement("h1");
        let userData = document.createElement("h3");
        let registrationButton = document.createElement("button");
        registrationButton.onclick = () => {
            location.href = window.location.origin;
        };
        registrationButton.textContent = 'Зарегистрироваться снова';
        message.textContent = "Вы успешно зарегистрировались!";
        userData.textContent = "Ваш id: " + data['id'] + ", логин: " + data['login'];
        successBlock.append(message);
        successBlock.append(userData);
        successBlock.append(registrationButton);
        mainBlock.append(successBlock);
    }

    event.preventDefault();
    let login = document.getElementById("login").value;
    let password = document.getElementById("password").value;
    makePostRequest(createUserUrl,{login: login, password: password}, successHandler, showDataValidationError)
});

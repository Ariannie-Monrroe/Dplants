


$(function() {
    $("#formValidation").validate({
        rules:{
            email:{
                required: true
            },
            password:{
                required: true
            }
        },
        messages: {
            email:{
                required:"Este campo es obligatorio",
            },
            password:{
                required:"Este campo es obligatorio",
                minlength: "El min de caracteres es de 5",
            }
        }
    })
})

const form1 = document.getElementById('form1');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form1.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs(form1);
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const validateInputs = (form) => {
    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const password2Value = password2.value.trim();

    let control1 = false
    let control2 = false
    let control3 = false
    let control4 = false


    if(usernameValue === '') {
        setError(username, 'Username es obligatorio');
        control1 = false
    } else {
        setSuccess(username);
        control1 = true
    }

    if(emailValue === '') {
        setError(email, 'Email es obligatorio');
        control2 = false
    } else if (!isValidEmail(emailValue)) {
        setError(email, 'Escribe un Email valido');
    } else {
        setSuccess(email);
        control2 = true
    }

    if(passwordValue === '') {
        setError(password, 'Contraseña es obligatoria');
        control3 = false
    } else if (passwordValue.length < 8 ) {
        setError(password, 'Password must be at least 8 character.')
    } else {
        setSuccess(password);
        control3 = true
    }

    if(password2Value === '') {
        setError(password2, 'Confirma tu contraseña');
        control4 = false
    } else if (password2Value !== passwordValue) {
        setError(password2, "Las contraseñas no coinciden");
    } else {
        setSuccess(password2);
        control4 = true
    }
    
    if(control1&&control2&&control3&&control4){
        console.log('Funciona porfavor :)');
        form.submit();
    }

};

// API 
function clima(latitud, longitud) {
    fetch("https://api.openweathermap.org/data/2.5/weather?lat="+ latitud + "&lon=" + longitud+ "&appid=da782411f0dd3e140c85a1c83494aa97")
    .then(response =>  response.json())
    .then(data => {
        console.log(data);
        let ubicacion = document.getElementById("ubicacion");
        ubicacion.innerHTML += "Ubicacion: " + data.name;

        let temperatura = document.getElementById("temperatura");
        let kelvin = 273.15;
        let celsius= data.main.temp - kelvin;
        temperatura.innerHTML = "Temperatura: " + Math.trunc(celsius) + "°"
    })
}

function ubi() {
    navigator.geolocation.getCurrentPosition(function(position){

        let latitud = position.coords.latitude;
        let longitud = position.coords.longitude;

        console.log(latitud, longitud);
        clima(latitud, longitud);
    })
}

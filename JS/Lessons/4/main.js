const email_input = document.getElementById("email_input")
const password_input = document.getElementById("password_input")
const signin_button = document.getElementById("signin_button")

signin_button.onclick = function() {
    console.log({"email": email_input.value, "password": password_input.value})
    email_input.value = null
    password_input.value = null
}

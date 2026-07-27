const subscribe_checkbox = document.getElementById("subscribe_checkbox")
const visa_button = document.getElementById("visa_button")
const mastercard_button = document.getElementById("mastercard_button")
const paypal_button = document.getElementById("paypal_button")
const submit_button = document.getElementById("submit_button")

submit_button.onclick = function() {
    let payment_result
    payment_result = {"subscribed": subscribe_checkbox.checked}
    if(visa_button.checked) {
        payment_result["payment_method"] = "visa"
    } 
    else if(mastercard_button.checked) {
        payment_result["payment_method"] = "mastercard"
    }
    else if(paypal_button.checked) {
        payment_result["payment_method"] = "paypal"
    }
    else {
        payment_result["payment_method"] = "not_selected"
    }
    console.log(payment_result)
}

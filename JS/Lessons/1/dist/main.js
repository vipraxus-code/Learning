const decrease_button = document.getElementById("decrease_button")
const reset_button = document.getElementById("reset_button")
const increase_button = document.getElementById("increase_button")
const counter_label = document.getElementById("counter_label")

let count = 0

decrease_button.onclick = function() {
    count--;
    update_count_label()
}

increase_button.onclick = function() {
    count++;
    update_count_label()
}

reset_button.onclick = function() {
    count = 0
    update_count_label()
}

function update_count_label() {
    counter_label.textContent = count
}
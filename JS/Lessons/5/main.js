const label = document.getElementById("label")
const input = document.getElementById("input")
const button = document.getElementById("button")

const minimum = 0
const maximum = 255
const answer = Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;
let attempts = 0

button.onclick = function(){
    attempts += 1
    let guess = input.value
    if(guess > answer){
        label.textContent = `Less than ${guess}`
    }
    else if(guess < answer){
        label.textContent = `Greater than ${guess}`
    }
    else{
        label.textContent = `You won! It took you ${attempts} attempts.`
    }
}
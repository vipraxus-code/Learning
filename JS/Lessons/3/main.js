let username = "";
while(username === null || username.length < 8) {
    username = prompt("Enter your username (must be a valid string 8+ characters long)")
    if(username !== null) {   
        username = username.trim()
    }
}

console.log(`Hello ${username}`)
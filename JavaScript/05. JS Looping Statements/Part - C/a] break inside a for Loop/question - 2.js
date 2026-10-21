// Simulate a simple password checker: keep asking the user for a password (using a for loop that runs maximum 5 times). If the correct password is entered, print “Access granted” and break. If all 5 attempts fail, print “Account locked”.





let correctPassword = "abc123";
let access = false;

for (let i = 1; i <= 5; i++) {
    let password = prompt("Enter password:");

    if (password === correctPassword) {
        console.log("Access granted");
        access = true;
        break;
    }
}

if (access === false) {
    console.log("Account locked");
}
// A user can login with either a correct password (passwordCorrect = true) or a valid OTP (otpValid = false). Check if login is allowed using ||.




let passwordCorrect = true;
let otpValid = false;

let loginPossible = passwordCorrect || otpValid;
console.log(loginPossible);
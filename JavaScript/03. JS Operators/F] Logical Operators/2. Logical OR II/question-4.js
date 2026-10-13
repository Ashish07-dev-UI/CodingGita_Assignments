// A form is valid if either email is given (emailGiven = true) or phone is given (phoneGiven = false). Check using ||.




let emailGiven = true;
let phoneGiven = false;

let valid = emailGiven || phoneGiven;
console.log(valid);
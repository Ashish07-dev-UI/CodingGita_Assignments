// Entry is allowed if age is above 18 (age = 16) or height is above 150 cm (height = 155). Check using ||.




let age = 16;
let height = 155;

let allowed = (age > 18) || (age > 150);
console.log(allowed);
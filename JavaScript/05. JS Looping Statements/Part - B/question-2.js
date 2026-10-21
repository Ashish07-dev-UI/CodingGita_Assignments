// Write a for loop that calculates the sum of all digits of a given number (example: 4729 → 4+7+2+9 = 22).




let num = 4729;
let count = 0;

let digits = String(num);

for(let i=0; i <= digits.length-1; i++) {
    sum += Number(digits[i]);
}

console.log(sum);
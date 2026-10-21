// Use a for loop to check whether a given number is a perfect number (a number equal to the sum of its proper divisors). Example: 28.




let num = 28;
let count = 0;

for (let i=1; i<num; i++) {
    if (num%i===0) {
        count += i;
    }
}
// console.log(count)

if (count === num) {
    console.log("Perfect number");
} else {
    console.log("Not a perfect number");
}





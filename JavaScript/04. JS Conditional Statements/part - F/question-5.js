// Write a nested ternary to find the greater of three numbers (a, b, c) without using Math.max.





let a = 4;
let b = 5;
let c = 6;

let greatest = a>b
    ? (a>c ? a : c)
    : (b>c ? b : c);

console.log(greatest);
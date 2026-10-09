let symbol1 = Symbol('id');
let symbol2 = Symbol('id');

console.log(symbol1 === symbol2);              // Output => False

let obj = {
    [symbol1]: "First Value",
    [symbol2]: "Second Value"
};

console.log(obj[symbol1]);                     // Output => First Value
console.log(obj[symbol2]);                     // Output => Second Value


// Explanation -> Even when the same description, every Symbol() creates a unique value, si symbol1 === sybol2 returns 'false'
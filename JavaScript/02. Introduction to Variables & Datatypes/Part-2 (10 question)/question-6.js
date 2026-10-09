let num = 9007199254740991;

console.log(num + 1);
console.log(num + 2);
console.log(num + 3);

let bigNum = 9007199254740991n;

console.log(bigNum + 1n);
console.log(bigNum + 2n);
console.log(bigNum + 3n);


// Difference:

// Number cannot safely represent integers beyond Number.MAX_SAFE_INTEGER.
// BigInt can represent very large integers precisely.
// Use n after the number to create a BigInt.
// You cannot directly mix Number and Big Int in arithmetic.
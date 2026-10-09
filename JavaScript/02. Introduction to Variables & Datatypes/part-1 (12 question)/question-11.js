console.log(a);     // Undefined
console.log(b);     // Reference Errors
console.log(c);     // Reference Errors

var a = 10;
let b = 20;
const c = 30;



// var a is hoisted and initialized with undefined → prints undefined.
// let b is hoisted but remains in the Temporal Dead Zone (TDZ) until initialized → ReferenceError.
// const c is also in the TDZ, but its console.log() is never reached because the error at b stops execution.
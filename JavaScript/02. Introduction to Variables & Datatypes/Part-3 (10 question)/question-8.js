let person = { name: "Amit", age: 22 };
let colors = ["red", "green", "blue"];
function sayHi() {
  return "Hi!";
}
let empty = null;

console.log(typeof person);                     // Output: Object
console.log(typeof colors);                     // Output: object
console.log(typeof sayHi);                      // Output: function
console.log(typeof empty);                      // Output: object
console.log(person.name);                       // Output: "Amit"
console.log(colors[1]);                         // Output: green
console.log(sayHi());                           // Output: Hi!
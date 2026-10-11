// A product costs ₹499. A customer has ₹500. Write conditions using >= and < to decide if the customer can buy it and if any change will be left.




let cost = 499;
let customerHas = 500;

let result = customerHas >= cost;
let changeWillLeft = cost < customerHas;

console.log(result);
console.log(changeWillLeft);
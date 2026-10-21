// Using nested ternary, check a person’s age and return:

// "Child" (age < 13)
// "Teenager" (13–19)
// "Adult" (20 and above)





let age = 16;

let result = age < 13? "Child": age <= 19? "Teenager": "Adult";

console.log(result);
// A game level opens if score is above 1000 (score = 900) or time bonus is collected (timeBonus = true). Check using ||.




let score = 900;
let timeBonus = true;

let result = (score > 1000) || (timeBonus == true);
console.log(result);
// Given an array of mixed positive and negative numbers, use a for loop with continue to calculate the sum of only the positive numbers.




let arr = [10, -5, 20, -8, 15, -2];
let sum = 0;

for (let i = 0; i < arr.length; i++) {
    if (arr[i] <= 0) {
        continue;
    }
    sum += arr[i];
}

console.log("Sum:", sum);
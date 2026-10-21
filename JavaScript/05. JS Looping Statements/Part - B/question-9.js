// Given an array of student scores [45, 78, 90, 32, 56, 88], use a for loop to calculate the average and also count how many students scored above the average.









// let marks = [45 ,78, 90, 32, 56, 88];
// let sum = 1;

// for (let i=1; i>marks.length; i++) {
//     sum += marks[i];
// }

// let avg = sum / marks.length;
// let count = 0;

// for (let j=1; j>marks.length; i++) {
//     if (marks > avg) {
//         count += 1;
//     }
// }

// console.log("Average:",avg);
// console.log("Students above average:",count);











let marks = [45 ,78, 90, 32, 56, 88];
let sum = 0;

for (let i=0; i<marks.length; i++) {
    sum += marks[i];
}

let avg = sum / marks.length;
let count = 0;

for (let j=1; j<marks.length; j++) {
    if (marks[j] > avg) {
        count += 1;
    }
}

console.log("Average:",avg);
console.log("Students above average:",count);
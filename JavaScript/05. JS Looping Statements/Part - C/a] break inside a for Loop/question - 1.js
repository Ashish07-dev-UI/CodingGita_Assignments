// Write a for loop that searches for the first occurrence of the number 7 in an array. As soon as it finds 7, print its index and stop the loop using break.




let numbers = [3, 5, 2, 7, 9, 7, 1];

for (let i=0; i<=7; i++) {
    if (numbers[i] === 7) {
        console.log("Index:", i);
        break;
    }
}
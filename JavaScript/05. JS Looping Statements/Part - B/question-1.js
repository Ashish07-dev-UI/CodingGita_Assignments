// Given an array of temperatures [28, 32, 25, 40, 18, 35], use a for loop to count how many days were hotter than 30°C.




let array = [28, 32, 25, 40, 18, 35];
let count = 0;

for(let i=0; i<=array.length-1; i++) {
    if (array[i]>30){
        count+=1;
    }
}

console.log(count);
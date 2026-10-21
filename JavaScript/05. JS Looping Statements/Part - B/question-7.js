// Print the following series using a single for loop:
// 1 2 4 8 16 32 64 128




let num = 7;
let bag = "";

for (let i = 0; i <= num; i++) {
    bag += 2**i + " "
}
console.log(bag);



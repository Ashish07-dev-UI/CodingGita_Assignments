// You drink 3 glasses of water every day. Write a program to calculate the total number of glasses you drink over 7 days. Print the cumulative total after each day.




let glasses = 3;
let day = 7

for (let i=1; i<=day; i++) {
    console.log("Day",i,":",glasses*i);
}
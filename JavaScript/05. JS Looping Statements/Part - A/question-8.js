// You want to calculate the sum of all even numbers between 2 and 30, including both 2 and 30. Write a program to calculate and print the total.




let sum=0;

for (let i=2; i<=30; i+=2){
    sum = sum + i;
}
console.log(sum);
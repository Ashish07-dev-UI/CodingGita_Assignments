// Create a for loop that prints only the numbers between 1 and 100 that are divisible by both 3 and 5, but not by 7.




for(let i=0; i<=100; i++) {
    if (i%3==0 && i%5==0 && i%7!=0) {
        console.log(i)
    }
}
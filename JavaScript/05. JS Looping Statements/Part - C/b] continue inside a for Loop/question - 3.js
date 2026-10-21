// Write a for loop that prints every character of the string "Hello World", but skips all spaces using continue.




let str = "Hello World";

for (let i = 0; i < str.length; i++) {
    if (str[i] === " ") {
        continue;
    }
    console.log(str[i]);
}
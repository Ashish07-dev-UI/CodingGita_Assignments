// Given an array of names, use a for loop to find the first name that starts with the letter “S”. Print that name and immediately stop the loop with break.





let names = ["Shu Kurunai", "Free Telahoya", "Valt Aoi", "Lui Sirosagi", "Rayuga"];

for (let i = 0; i < names.length; i++) {
    if (names[i].startsWith("S")) {
        console.log(names[i]);
        break;
    }
}
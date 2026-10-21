// Given an array of ages [12, 18, 25, 15, 30, 17, 22], use a for loop with continue to print only the ages of people who are eligible to vote (age ≥ 18).





let ages = [12, 18, 25, 15, 30, 17, 22];

for (let i = 0; i < ages.length; i++) {
    if (ages[i] < 18) {
        continue;
    }

    console.log(ages[i]);
}
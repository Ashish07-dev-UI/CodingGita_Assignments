// Write a program using switch (true) to assign class based on marks:
// ≥ 75 → Distinction
// ≥ 60 → 1st class
// ≥ 50 → 2nd class
// ≥ 35 → 3rd class
// below 35 → Failed





let marks = 65;

switch (marks) {
    case marks>=75:
        console.log("Distinction");
        break;
    case marks>=60:
        console.log("1st Class");
        break;
    case marks>=50:
        console.log("2nd Class");
        break;
    case marks>=35:
        console.log("3rd Class");
        break;
    default:
        console.log("Invalid Marks");
        break;
}
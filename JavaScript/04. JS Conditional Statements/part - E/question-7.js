// Write a program that takes a value which can be either a number or a string (0, "0", false, null, undefined) and uses switch to correctly identify each one. Explain why some values may not match as expected.




 let value = "0";

switch (value) {
    case 0:
        console.log("Number zero");
        break;

    case "0":
        console.log("String zero");
        break;

    case false:
        console.log("Boolean false");
        break;

    case null:
        console.log("Null value");
        break;

    case undefined:
        console.log("Undefined value");
        break;

    default:
        console.log("Unknown value");
}
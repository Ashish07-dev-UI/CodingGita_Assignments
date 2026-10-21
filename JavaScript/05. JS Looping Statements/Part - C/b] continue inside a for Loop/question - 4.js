// Print the multiplication table of 6 from 1 to 12, but skip the rows where the product is divisible by 5 (use continue).




for (let i = 1; i <= 12; i++) {
    let product = 6 * i;

    if (product % 5 === 0) {
        continue;
    }

    console.log(`6 x ${i} = ${product}`);
}
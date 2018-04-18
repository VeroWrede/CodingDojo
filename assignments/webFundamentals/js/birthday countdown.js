var days = 60;


if (days > 10) {
    while (days > 10) {
        console.log('still ', days, ' until my birthday');
        days -= 1;
    }
}
if (days > 1) {
    while (days > 1) {
        console.log('only ', days, ' until my birthdya!');
        days -= 1;
    }
}
console.log('tomorrow is my birthday!');



while (days > 0) {
    if (days > 10) {
        console.log('still ', days, ' until my birthday');
    }
    else {
        console.log('only ', days, ' until my birthdya!');
    }
    days -= 1;
}

console.log('tomorrow is my birthday!');

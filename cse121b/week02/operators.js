/* Write a Javascript snippet to do each of the following. Make your best guess if you don't know. Make sure to put some sort of response on each:
*/

// 1. Add two numbers

const number1 = 5;
const number2 = 10;
const totalSum = number1 + number2;
console.log(`1. Add two numbers: ${number1} + ${number2} =  ${totalSum}`);

// 2. Multiply two numbers
const totalMult = number1 * number2;
console.log(`2. Multiply two numbers: ${number1} * ${number2} = ${totalMult}`);

// 3. Subtract one from a number
const numberOfSubtraction = 1;
const totalSubtract = numberOfSubtraction - number1;
console.log(`3. Subtract one from a number: ${numberOfSubtraction} - ${number1} = ${totalSubtract}`);

//4. concatinate two strings together.
const string1 = 'The Church of Jesus Christ';
const string2 = 'of Latter-Day Saints';
const totalConcat = string1 + string2;
console.log(`4. concatinate two strings together = ${string1} ${string2}`);

//5. assign a value to a variable
let variable = 8;
console.log(`5. assign a value to a variable: variable = ${variable}`);

//6. increment the value in a variable by 3
variable += 3;
console.log(`6. increment the value in a variable by 3: variable += 3 = ${variable}`);

//7. compare two values to see if they are the same
let isTheSame = false;
if (number1 === number2) {
    isTheSame = true
    return isTheSame
}
console.log(`7. compare two values to see if they are the same: Is number1 and number2 the same?(true/false) = ${isTheSame}`); 


//8. check to see if one number is less than another number
let isSmaller = false;
if (number1 < number2){
    isSmaller = true;
    return isSmaller
}
console.log(`8. check to see if one number is less than another number: Is number1 less than number2?(true/false) = ${isSmaller}`);

//9. Check to see if two values are NOT equal
let isNotEqual = false;
if (totalSubtract  != totalMult){
    isNotEqual = true;
    return isNotEqual
    }
console.log(`9. Check to see if two values are NOT equal: Is totalSubtract and totalMult NOT equal? (true/false) ${isNotEqual}`);

//10. check to see if a value is less than 10 and greater than 0
let isLessThanTenAndGreaterThanZero = false;
if (totalSum < 10 && totalSum > 0){
    isLessThanTenAndGreaterThanZero = true;
    return isLessThanTenAndGreaterThanZero
}
console.log(`10. check to see if a value is less than 10 and greater than 0: Is totalSum < 10 && > 0?(true/false) = ${isLessThanTenAndGreaterThanZero}`);   
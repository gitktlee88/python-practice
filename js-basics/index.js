//comment
let name = 'KyungTak';  // String Literal
let age = 30; // Number Literal
let isApproved = false; // Boolean Literal
let firstName = undefined;
let selectedColor = null;
console.log(name);

let interestRate = 0.3;
// const interestRate = 0.3;
interestRate = 1;
console.log(interestRate)


// Object
let person = {
  name: 'Kim',
  age: 30
};
console.log(person);
// Dot Notation
person.name = 'John';
console.log(person);
// Braket Notation
let selection = 'name';
person[selection] = 'Mary';
console.log(person);

// Array is dynamic
let selectedColors = ['red', 'blue'];
selectedColors[2] = 'green';
console.log(selectedColors[0]);
console.log(selectedColors.length);


// Performing a task
function greet(name) {
  console.log('Hello World! ' + name);
}
greet('Lee');

// Calculating a Value
function square(num) {
  return num * num;
}
console.log(square(2));

// --- RULES for naming VARIABLE ---
//- Cannot be a reserved keyward
//- Should be meaningful
//- Cannot start with a number
//- Cannot contain a space or hyphen
//- Are case-sensitive

 //  < copy by value >          < copy by reference >
 // Value Types (Primitives)    Reference Types
 // String                      Object
 // Number                      Array
 // Boolean                     Function
 // undefined
 // null

//             Languages
// static                string name = 'John';
// (statically-typed)
//
// Dynamic               let name = 'John';
// (Dynamiccally-typed)

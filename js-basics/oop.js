// Let and const have a block scope
// but var has function scope or global scop
//ES5
var num = 10;
for (var num = 0; num < 3; num++) {
  console.log(num); //0 1 2
}
console.log(num); //3

//
var y = 1;         // global scope
function x() {
  console.log(y);
  // var y = 4;    // function scope
}
x()

// Hoisting is a JavaScript mechanism where
// variables and function declarations are moved
// to the top of their scope before code execution.


//ES5
console.log(a); // undefined
var a = 5;

// let and const hoist but you cannot access them
// before the actual declaration is evaluated at runtime.
//ES6
// console.log(b);  //ReferenceError: b is not defined
// let b = 6;
//
// console.log(c);  //ReferenceError: c is not defined
// const c = 7;


//Encapsulation: as an employee object
// - reduce complexity + increase reusability
let employee = {
  baseSalary: 30_000,
  overtime: 10,
  rate: 20,
  getWage: function() {
    return this.baseSalary + (this.overtime*this.rate);
  }
};

console.log(employee.getWage());

// Abstraction:
// - reduce complexity + isolate the impact of changes

// Inheritance:
// - eleminate redundant code

// Poly+Morphism: ( many+form)
// - refactor ugly switch/case statements


///////////////////////////////////////////
// Factory function vs Constructor function
// Factory
function createCircle(radius) {
  return {
    radius: radius,
    draw: function() {
      console.log('draw func from Factory')
    }
  };
}
const circle = createCircle(1);
circle.draw();

//////////////////////////////////////////
// Constructor Function like class in Java
function Circle(radius) {
  // console.log('this points', this)
  this.radius = radius;
  this.draw = function() {
    console.log('draw func from Constructor')
  }
}
// Circle.call({}, 1);          # same result as below.
// Circle.apply({}, [1,2,3,]);  # same result as below.
const another = new Circle(1);
//               ^-- creates empty object, new points this

another.draw();

// add new property in Circle object
circle.location = { x: 1};     // dot notation
circle['location'] = { x: 1};  // bracket notation
const propertyName = 'center location';
const propertyName2 = 'center-location';
circle[propertyName] = { x: 1};
// Dynamiccally delete a property
delete circle.propertyName2;


for (let key in circle) {
  if (typeof circle[key] !== 'function')
  console.log(key, circle[key]);
}

const keys = Object.keys(circle);
console.log(keys);

if ('radius' in circle)
console.log('Circle has a radius.')


// Abstraction example:
function Circle2(radius) {
  this.radius = radius;

  let defaultlocation = { x:0, y:0};
  let computeOptimumLocation = function(factor) {
    // ...
  }

  // closure function's variable is temporary scope.
  this.draw = function() {
    let x, y;    // will be recreated everytime
                 // and die when leave out of the funciion
    computeOptimumLocation(0.1);

    console.log(this.radius, 'draw func from Circle2')
  };
}

const circle2 = new Circle2(10);
circle2.draw();

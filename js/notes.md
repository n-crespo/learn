# Modern JavaScript Development

## Unit 1

- `let` > `var` (block scoping) (hoisting)
- backticks (``) for better strings
- `const` isn't actually `const` (kinda)
  - just no reassignment
- simultaneous assignment from arrays and objects with `[]` and `{}`
  - called deconstructing

## Unit 2

- fat arrow functions look cool (and better support `this`), see below
  - nested `this` causes problems, define it in correct scope
  - arrow function has "lexical scope built in"

```javascript
let message = {
  hello: "Hello",
  names: ["Sue", "Joe"],
  showMessage: function () {
    this.names.forEach(function (name) {
      console.log(this.hello + " " + name); // <--- this doesn't work
    });
  },
};

let message = {
  hello: "Hello",
  names: ["Sue", "Joe"],
  showMessage: function () {
    let self = this; // <--- this is the workaround
    this.names.forEach(function (name) {
      console.log(self.hello + " " + name);
    });
  },
};

let message = {
  hello: "Hello",
  names: ["Sue", "Joe"],
  showMessage: function () {
    this.names.forEach((name) => {
      console.log(this.hello + " " + name); // <--- wow! (it works)
    });
  },
};
```

- deconstructing syntax can be used for optional positional arguments
  - `= {}` is not necessary for it to be optional

```javascript
function showMessage(who, { p1 = "Hello", p2 = "World" } = {}) {
  console.log(who + " says " + p1 + " " + p2);
}
showMessage("Trailhead", { p1: "hi", p2: "hi" }); // this works (must be an object)
showMessage("Trailhead"); // this also works
```

- functions with as many parameters you want with `rest` (shown as `...`)
- final argument becomes an array

```javascript
function showContact(firstName, lastName, ...titles) {
  console.log(
    firstName + " " + lastName + ", " + titles[0] + " and " + titles[1],
  );
}
```

- combine arrays better with the spread (`...`) operator

```javascript
array1 = [...array1, ...array2];
```

## Unit 3

Use `class` for _real_ classes and more normal constructors/function
implementations (below)

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }
  printName() {
    console.log(this.name);
  }
}
```

The above is still a function though...

```javascript
console.log(typeof Animal); // Display "function"
```

**IMPORTANT:** Omitting the `let` or `var` or `const` keyword will default to a
global variable.

### Static Functions

You can make functions that don't require instances of an object:

```javascript
class SuperClass {
  static test() {
    return "something";
  }
}
console.log(SuperClass.test()); // Displays "something"
```

### Expression Defined Classes

You can define/create (somewhat) temporary classes with variable assignment:

```js
let SuperClass = class {
  static test() {
    return "test";
  }
};
console.log(SuperClass.test()); // Displays "test"
```

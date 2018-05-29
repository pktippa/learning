function* gen_func(){
  
}

const genFuncVar = gen_func();
// Prints {}
console.log(genFuncVar);
// Prints { value: undefined, done: true }
console.log(genFuncVar.next());

console.log('-----------------------')

function* gen_func2(){
  yield;
}

const genFuncVar2 = gen_func2();
// Prints {}
console.log(genFuncVar2);

// Prints { value: undefined, done: false }
// See here the done is false, we have to call next() again 
// to complete the execution of generator function
console.log(genFuncVar2.next());

// Calling next again
// Prints { value: undefined, done: true } see the done is true now
console.log(genFuncVar2.next());

console.log('-----------------------')

function* gen_func3(){
  yield 10;
}

const genFuncVar3 = gen_func3();

// Prints { value: 10, done: false }
// 10 is the value that is been returned by yield
console.log(genFuncVar3.next());
// Prints { value: undefined, done: true }
// Now all the commands in gen_func3 are completed
console.log(genFuncVar3.next());

console.log('-----------------------')

function* gen_func4() {
  yield 15;
  // Executes and prints this when .next() is called 2nd time
  console.log('In gen_func4');
  yield 20;
  return 25;
}

const genFuncVar4 = gen_func4();

// Prints 1.  { value: 15, done: false }
console.log('1. ', genFuncVar4.next())
// Prints 2.  { value: 20, done: false }
console.log('2. ', genFuncVar4.next())
// Prints 3.  { value: 25, done: true }
console.log('3. ', genFuncVar4.next())
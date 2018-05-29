# EcmaScript 6

## Default Parameters

```js
// Parameter 'b' will have a default value of 1
function multiply(a, b = 1) {
  return a * b;
}

console.log(multiply(5, 2));
// expected output: 10

console.log(multiply(5));
// expected output: 5
```

## Copying Objects without mutation

```js
const obj1 = {
  fname: 'pradeep',
  lname: 'kumar'
};
// Need to pass an empty object {} as first arg
const newObj = Object.assign({}, obj1, {lname: 'tippa'});

console.log(obj1);
// expected output: {fname: 'pradeep', lname: 'kumar'}

console.log(newObj);
// expected output: {fname: 'pradeep', lname: 'tippa'}
```

## Shorthand object notation

```js
var a = 'foo', b = 42, c = {};
var o = {a, b, c};

console.log(o);
// output {a:'foo', b: 42, c: {}}
```

## Triple Dot - Spread notation

Bot `App1` and `App2` are same.

```js
function App1() {
  return <Greeting firstName="Ben" lastName="Hector" />;
}

function App2() {
  const props = {firstName: 'Ben', lastName: 'Hector'};
  return <Greeting {...props} />;
}
```

For Creating new object

```js
var obj = {a: 1, b:2, c:4}
// all properties get copied automatically 
// and only selected properties can be changed
var obj2 = {...obj, a:3}
```

## Generators

https://medium.com/@hidace/javascript-es6-generators-part-i-understanding-generators-93dea22bf1b

[Script](generators.js)

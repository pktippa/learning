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
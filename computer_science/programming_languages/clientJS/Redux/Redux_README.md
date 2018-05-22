# Redux

## Actions

`Actions` are payloads of information that send data from your application to your store. They are the only source of information for the store. You send them to the store using `store.dispatch()`.

`Actions` are plain JavaScript objects. Actions must have a `type` property that indicates the type of action being performed. Types should typically be defined as `string constants`. Once your app is large enough, you may want to move them into a separate module.

```js
const ADD_TODO = 'ADD_TODO';

// Action
{
  type: ADD_TODO,
  text: 'Build the first todo'
}
```

## Reducer

The reducer is a pure function that takes the previous state and an action, and returns the next state.

InitialState is reducer call will be `undefined`. So have a initial state object state to return from the reducer

Splitting the bigger code into smaller reducer's and having each reducer maintaining its part of the global state is good.

```js
function reduceFunc(state) {
  return Object.assign({}, state, {lname: 'tippa'});
}
```

## Walk through example

[Step by Step Guide](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a)
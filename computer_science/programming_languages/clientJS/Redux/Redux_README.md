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

## Examples

[Step by Step Guide](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a)

* [Todos](https://github.com/pktippa/react-redux-example-todos)
* [Real World](https://github.com/pktippa/react-redux-example-real-world)

## Dispatch

Dispatch (`dispatch()`) takes `action` as input, gets the `currentState` (first time its get populated with `INIT` action which makes sure all reducers return the default initial state ), gets the `currentReducer` -> `combination()` from the reducers combined at the application startup, 

`redux/es/createStore.js` -> `dispatch` function

```js
currentState = currentReducer(currentState, action);
```

now combination loop through the reducers registered and runs each reducer, 

`redux/es/combineReducers.js` -> `combineReducers` function -> `return function combination() {`

```js
var nextStateForKey = reducer(previousStateForKey, action);
```

now reducer does its job to take state and action and returns new state.


We have to map state to properties and dispatch to properties to see the changes in the user interface

A container connects to a Component.

When connecting we can pass mapping state to props and dispatch to props.

```js
import { connect } from 'react-redux'
import { setVisibilityFilter } from '../actions'
import Link from '../components/Link'

const mapStateToProps = (state, ownProps) => ({
  active: ownProps.filter === state.visibilityFilter
})

const mapDispatchToProps = (dispatch, ownProps) => ({
  onClick: () => dispatch(setVisibilityFilter(ownProps.filter))
})

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Link)
```

A container can also be a Component.

```js
const SimpleLink = (
  <a href="#"/>
)

export default connect()(SimpleLink)
```
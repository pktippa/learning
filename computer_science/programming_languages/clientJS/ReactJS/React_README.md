# ReactJS

## Official Tutorial

```
$ npm install -g create-react-app
# create-react-app tic-tac-toe
```

## React Component

A component takes in parameters, called `props`, and returns a hierarchy of views to display via the `render` method.

components may accept arbitrary props, including primitive values, React elements, or functions.

```js
class ShoppingList extends React.Component {
  render() {
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}</h1>
        <ul>
          <li>Instagram</li>
          <li>WhatsApp</li>
          <li>Oculus</li>
        </ul>
      </div>
    );
  }
}

// Example usage: <ShoppingList name="Mark" />
```

React component accepts inputs via `props` by using the attributes and returns the React Elements describing what should appear on the screen.

## React DOM

React DOM compares the element and its children to the previous one, and only applies the DOM updates necessary to bring the DOM to the desired state.

## React Element

The `render`(above) method returns a description of what you want to render, and then `React` takes that description and renders it to the screen. In particular, `render` returns a `React element`, which is a lightweight description of what to render.

React element is a real JavaScript object that you can store in a variable or pass around your program.

JSX produces "React Elements"

You can think of them as descriptions of what you want to see on the screen.

Reacct Elements are "immutable"

# State

React components can have `state` by setting `this.state` in the constructor, which should be considered private to the component

When you want to aggregate data from multiple children or to have two child components communicate with each other, move the state upwards so that it lives in the parent component. The parent can then pass the state back down to the children via props, so that the child components are always in sync with each other and with the parent.

Component `state` is private we cannot update the Parent component `state` directly from the child component, the usual pattern is pass down a function from Parent to Child component that gets called to invoke it on action of child component. We call components like this controlled components.

Don't use state at all to build this static version

Is it passed in from a parent via props? If so, it probably isn’t state.

Does it remain unchanged over time? If so, it probably isn’t state.

Can you compute it based on any other state or props in your component? If so, it isn’t state.

# Constructor

In JavaScript classes, you need to explicitly call `super();` when defining the constructor of a subclass.

```js
class Square extends React.Component {
    constructor (props) {
        super(props);
        this.state = {
            value : null,
        };
    }
}
```

# Functional Components

React supports a simpler syntax called `functional components` for component types that only consist of a `render` method. Rather than define a `class` extending `React.Component`, simply write a `function` that takes `props` and `returns` what should be rendered.

Earlier with class and React Component:

```js
class Square extends React.Component {
    render () {
        return (
            <button className="square" onClick={() => this.props.onClick()}>
                {this.props.value}
            </button>
        );
    }
}
```

With `Functional Components`

```js
function Square(props) {
    return (
        <button className="square" onClick={props.onClick}>
            {props.value}
        </button>
    );
}
```

# Key

Regarding list of items or array or iterator references

`key` is a special property that's reserved by `React`.There is no way for a component to inquire about its own key. cannot be accessible as `this.props.key`

When a key is added to the set, a component is created; when a key is removed, a component is destroyed. Keys tell React about the identity of each component, so that it can maintain the state across rerenders. If you change the key of a component, it will be completely destroyed and recreated with a new state.

Component keys don’t need to be globally unique, only unique relative to the immediate siblings.

# render

Render function will always get called whenever there is a change in `state`. Ex:

```js
constructor(props) {
    super(props);
    this.state = {
        employee: true,
    }
}

handleClick() {
    console.log('changing state of employee');
    this.setState(
        {
            employee: !this.state.employee
        }
    );
}

handleAnother() {
    console.log('No changes are done to state here');
}
render() {
    console.log('Render method called')
    <button onClick={() => this.handleClick()}>this calls render</button>
    <button onClick={() => this.handleAnother()}>this does not call render</button>
}
```

# Composition vs Inheritance

Use Composition rather than Inheritance.

Props and composition give you all the flexibility you need to customize a component’s look and behavior in an explicit and safe way. 

```js
function FancyBorder(props) {
  return (
    <div className={'FancyBorder FancyBorder-' + props.color}>
      {props.children}
    </div>
  );
}
function Dialog(props) {
  return (
    <FancyBorder color="blue">
      <h1 className="Dialog-title">
        {props.title}
      </h1>
      <p className="Dialog-message">
        {props.message}
      </p>
      {props.children}
    </FancyBorder>
  );
}

class SignUpDialog extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.handleSignUp = this.handleSignUp.bind(this);
    this.state = {login: ''};
  }

  render() {
    return (
      <Dialog title="Mars Exploration Program"
              message="How should we refer to you?">
        <input value={this.state.login}
               onChange={this.handleChange} />

        <button onClick={this.handleSignUp}>
          Sign Me Up!
        </button>
      </Dialog>
    );
  }

  handleChange(e) {
    this.setState({login: e.target.value});
  }

  handleSignUp() {
    alert(`Welcome aboard, ${this.state.login}!`);
  }
}
```
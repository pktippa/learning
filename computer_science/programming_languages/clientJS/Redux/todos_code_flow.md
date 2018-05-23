* Container -> Component -> connect flow

* Page refresh flow

    // Redux Related
    first combineReducers function call in "index.js" in "reducers"

    ```js
    export default combineReducers({
        todos,
        visibilityFilter
    })
    ```
    combineReducers is in "node_modules/redux/es/combineReducers.js"

    ```js
    assertReducerShape(finalReducers);
    ```

    then went to "todo.js" under reducers, with action.type = "@@redux/INIT" and also with type random
    then went to "visibilityFilter.js" under reducers, same as for "todo.js"

    return function comnation() gets returned when imported using
    ```js
    export default combineReducers({
        todos,
        visibilityFilter
    })
    ```
    now the combination() is the "rootReducer" in src\index.js
    ```js
    import rootReducer from './reducers'
    ```

    Executing createStore by passing rootReducer
    ```js
    const store = createStore(rootReducer)
    ```

    redux/es/createStore.js -> createStore method

    ```js
    dispatch({ type: ActionTypes.INIT });
    ```

    createStore function returns the Object with dispatch, subscribe, getState, replaceReducer and others

    // React related now for rendering

    src/index.js

    ```js
    render(
        <Provider store={store}>
            <App />
        </Provider>,
        document.getElementById('root')
    )
    ```

    note: A component contain other compnents included and also other containers

    Now App will try to execute, in which it internally calls AddTodo, VisibleTodoList, Footer

    VisibleTodoList has two functions are passed as parameters to connect (import { connect } from 'react-redux')


* Click on "Add todo" button flow

    It is a form , generates form submit action

    calls "addtodo" action in index.js under "actions" folder

    returns a new JSON object as action

    calls "dispatch" function in "createStore.js" in node_modules\redux\es\

    which calls currentReducer which got populated as combination function from combineReducer.

    Now reducer does its purpose which is it takes state and action as input and gives the next state.

    we have two reducers we registerd initially
    first reducer "todos" calls with 

    state = [], action= {"type":"ADD_TODO","id":0,"text":"pradeep"}

    now adds by going to case 'ADD_TODO' based on action type

    returns [{"type":"ADD_TODO","id":0,"text":"pradeep"}]

    Next reduer "visibitilyFilter" calls with

    state = "SHOW_ALL" same as action above

    since that action is not mapped in switch case of "visibitilyFilter" it returns default

    after currentReducer we have listeners, in which one of it is "onStateChanged"

    which is in connectAdvanced.js 

    it calls run -> makeSelectorStateful -> run -> sourceSelector as pureFinalPropsSelector in 

    selectFactory selectorFactory.js react-redux/es/connect/ 
    
    handleSubSequentCalls -> calls "handleNewState" function

    which calls "mapStateToProps" which is for our "getVisibleTodos" in VisibleTodoList container

    it compares previous state and new state and get properties (TODO - need further)
    via state we are updating the properties

    Now the control goes to FilterLink.js
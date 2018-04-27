import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

/*
class Square extends React.Component {

  render() {
    return (
      <button className="square" onClick={() => this.props.onClick()}>
        {this.props.value}
      </button>
    );
  }
}
*/
/** With functional components */

function Square(props) {
  return (
    <button className='square' onClick={props.onClick}>
      {props.value}
    </button>
  );
}

class Board extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      squares: Array(9).fill(null),
      xIsNext: true,
    }
  }
  /*
   // Moving the handleClick to the Game class
  handleClick(i) {
    const squares = this.state.squares.slice();
    // Checking if there is already a winner or position is already filled
    if (calculateWinner(squares) || squares[i]) {
      return;
    }
    squares[i] = this.state.xIsNext? 'X': 'O'
    this.setState({squares: squares, xIsNext: !this.state.xIsNext})
  }*/

  renderSquare(i) {
    return <Square value={this.props.squares[i]} onClick={() => this.props.onClick(i)}/>;
  }

  render() {
    /*
    // Moving to the Game Class
    const winner = calculateWinner(this.state.squares);
    let status;
    if (winner) {
      status = 'Winner: ' + winner;
    } else {
      status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
    }
    */

    return (
      <div>
        {/*
        // Commented out after implemented history for Game class
        <div className="status">{status}</div>
        */}
        <div className="board-row">
          {this.renderSquare(0)}
          {this.renderSquare(1)}
          {this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}
          {this.renderSquare(4)}
          {this.renderSquare(5)}
        </div>
        <div className="board-row">
          {this.renderSquare(6)}
          {this.renderSquare(7)}
          {this.renderSquare(8)}
        </div>
      </div>
    );
  }
}

class Game extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      history: [{
        squares: Array(9).fill(null),
      },],
      stepNumber: 0,
      xIsNext: true,
      /*
      // Only for testing the render reloading
      sample: false,
      */
    }
  }
  handleClick(i) {
    const history = this.state.history.slice(0, this.state.stepNumber + 1);
    const current = history[history.length - 1]
    const squares = current.squares.slice();
    // Checking if there is already a winner or position is already filled
    if (calculateWinner(squares) || squares[i]) {
      return;
    }
    squares[i] = this.state.xIsNext? 'X': 'O'
    this.setState(
      {
        history: history.concat([{squares: squares}]),
        stepNumber: history.length,
        xIsNext: !this.state.xIsNext,
      })
  }

  jumpTo(move) {
    this.setState({
      stepNumber: move,
      xIsNext: (move % 2) === 0
    });
  }

  sampleClick() {
    console.log('in sample click');
    // Modifying state will trigger the render method
    /*this.setState(
      {
        sample: true,
      }
    )*/
  }

  render() {
    const history = this.state.history;
    console.log('in render method')
    const current = history[this.state.stepNumber];
    const winner = calculateWinner(current.squares);
    const moves = history.map((step, index) => {
      const desc = index ? 'Go to #' + index : 'Go to game start'
      return (
        <li key={index}>
          <button onClick={() => this.jumpTo(index)}>{desc}</button>
        </li>
      );
    })

    let status;
    if (winner) {
      status = 'Winner: ' + winner;
    } else {
      status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
    }
    return (
      <div className="game">
        <div className="game-board">
          <Board squares={current.squares} onClick={(i) => this.handleClick(i)}/>
        </div>
        <div className="game-info">
          <div>{status}</div> {/* uncommented after the history implmented needed in Game class*/}
          <ol>{moves}</ol>
        </div>
        {/*
        // Sample check if the render method is called or not
        <div className="sample-data">
          <button onClick={() => this.sampleClick()}/>
        </div>
        */}
      </div>
    );
  }
}

// ========================================

ReactDOM.render(
  <Game />,
  document.getElementById('root')
);

// Help method to identify whether there is a winner or not
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}